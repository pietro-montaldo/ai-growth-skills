"""Clay code step "Read company and signal" for the clay-company-signals skill.

Turns one audience signal event on a company (JobPost, NewHire or News) plus the
company's Audiences record into flat fields for the rest of the workflow.

Inputs to wire on the node (sourceNodeId = the trigger node):
  signal_type   $.signal.signalType
  signal_data   $.signal.data
  company_id    $.fields.id
  company_name  $.fields['Company name']
  domain        $.fields.Domain
  company_linkedin  $.fields['LinkedIn URL']
  last_added    $.fields['Signals: last added']
  icp_card      optional, a company field that names the ICP card
  source_<name> optional, one input per source field, for example
                source_lookalike = $.fields['Lookalike campaign'].
                The first non-empty one in SOURCE_ORDER names the source.

JobPost events carry data.jobPostData (title, url, company_name, domain, company_url,
posted_at) but no job description. NewHire and News shapes can differ, so person and
article fields are read defensively. Check the first real event and adjust.
"""

from datetime import datetime, timedelta, timezone

GUARD_DAYS = 90


def text(value):
    return "" if value is None else str(value).strip()


def first(obj, keys):
    """First non-empty value in obj for any of keys (case-insensitive)."""
    if not isinstance(obj, dict):
        return ""
    lower = {str(k).lower(): v for k, v in obj.items()}
    for key in keys:
        value = lower.get(key.lower())
        if isinstance(value, (str, int, float)) and text(value):
            return text(value)
    return ""


def dicts(obj, depth=0):
    """obj and every nested dict, shallowest first."""
    if depth > 4 or not isinstance(obj, (dict, list)):
        return []
    found = [obj] if isinstance(obj, dict) else []
    children = obj.values() if isinstance(obj, dict) else obj
    for child in children:
        found.extend(dicts(child, depth + 1))
    return found


NAME_KEYS = ("full_name", "fullName", "name", "person_name", "personName")
FIRST_KEYS = ("first_name", "firstName")
LAST_KEYS = ("last_name", "lastName")
TITLE_KEYS = ("job_title", "jobTitle", "title", "latest_title", "current_title", "position")
LINKEDIN_KEYS = ("linkedin_url", "linkedinUrl", "linkedInUrl", "profile_url", "profileUrl", "url")
START_KEYS = ("start_date", "startDate", "started_at", "job_start_date", "date_started")


def person_from(data):
    """Best guess at the hired person in a NewHire payload."""
    best = None
    for candidate in dicts(data):
        name = first(candidate, NAME_KEYS)
        if not name:
            name = " ".join(p for p in (first(candidate, FIRST_KEYS), first(candidate, LAST_KEYS)) if p)
        url = first(candidate, LINKEDIN_KEYS)
        if url and "linkedin.com/in/" not in url.lower():
            url = ""
        if name and (url or first(candidate, TITLE_KEYS)):
            best = {"name": name, "title": first(candidate, TITLE_KEYS), "linkedin": url,
                    "start": first(candidate, START_KEYS)}
            break
    if best is None:
        best = {"name": "", "title": "", "linkedin": "", "start": ""}
    if not best["linkedin"]:
        for candidate in dicts(data):
            url = first(candidate, LINKEDIN_KEYS)
            if "linkedin.com/in/" in url.lower():
                best["linkedin"] = url
                break
    if not best["start"]:
        for candidate in dicts(data):
            best["start"] = first(candidate, START_KEYS)
            if best["start"]:
                break
    return best


def parse_date(value):
    value = text(value)
    if not value:
        return None
    for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(value[:19], fmt).date()
        except ValueError:
            continue
    try:
        return datetime.strptime(value[:10], "%Y-%m-%d").date()
    except ValueError:
        return None


SOURCE_ORDER = ["visitor", "lookalike"]  # edit to match the source_<name> inputs you wire


def handler(context):
    raw_type = text(context.get_input("signal_type"))
    data = context.get_input("signal_data") or {}
    if not isinstance(data, dict):
        data = {}

    if raw_type == "JobPost" or "jobPostData" in data:
        signal_type = "job_post"
    elif raw_type == "NewHire":
        signal_type = "new_hire"
    elif raw_type == "News":
        signal_type = "news"
    else:
        signal_type = "other"

    source = "manual"
    for name in SOURCE_ORDER:
        if text(context.get_input("source_" + name)):
            source = name
            break

    job = data.get("jobPostData") if isinstance(data.get("jobPostData"), dict) else {}
    job_title = text(job.get("title"))
    job_url = text(job.get("url") or data.get("url"))

    empty = {"name": "", "title": "", "linkedin": "", "start": ""}
    hire = person_from(data) if signal_type == "new_hire" else empty

    headline = ""
    if signal_type == "news":
        for candidate in dicts(data):
            headline = first(candidate, ("title", "headline"))
            if headline:
                break

    if signal_type == "job_post":
        detail = "Job post: " + (job_title or "untitled role") + (" · " + job_url if job_url else "")
    elif signal_type == "new_hire":
        detail = "New hire: " + (hire["name"] or "unknown") + ", " + (hire["title"] or "title unknown")
        if hire["start"]:
            detail += " (started " + hire["start"][:10] + ")"
    elif signal_type == "news":
        detail = "News: " + (headline or "untitled") + (" · " + job_url if job_url else "")
    else:
        detail = "Signal: " + (raw_type or "unknown")

    today = datetime.now(timezone.utc).date()
    last = parse_date(context.get_input("last_added"))
    added_recently = bool(last and last > today - timedelta(days=GUARD_DAYS))

    domain = text(context.get_input("domain")).lower()
    for prefix in ("https://", "http://", "www."):
        if domain.startswith(prefix):
            domain = domain[len(prefix):]
    domain = domain.split("/")[0]

    company_id = context.get_input("company_id")
    try:
        company_id = str(int(float(company_id)))
    except (TypeError, ValueError):
        company_id = text(company_id)

    return {
        "signal_type": signal_type,
        "source": source,
        "icp_card": text(context.get_input("icp_card")),
        "signal_detail": detail[:500],
        "job_title": job_title,
        "job_url": job_url,
        "news_headline": headline,
        "hire_name": hire["name"],
        "hire_title": hire["title"],
        "hire_linkedin": hire["linkedin"],
        "hire_start_date": hire["start"],
        "company_id": company_id,
        "company_name": text(context.get_input("company_name")) or text(job.get("company_name")),
        "domain": domain or text(job.get("domain")).lower(),
        "company_linkedin": text(context.get_input("company_linkedin")) or text(job.get("company_url")),
        "added_recently": added_recently,
        "last_added": last.isoformat() if last else "",
        "today": today.isoformat(),
    }
