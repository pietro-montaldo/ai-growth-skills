"""Clay code step "Email lines" for the clay-company-signals skill.

Writes the first name, last name, opener and proof line the campaign copy uses.
Fill in the CONFIG block from the user's GTM context before pasting it into Clay.

Inputs to wire on the node:
  full_name, title, person_source   from "Chosen person"
  company_name, signal_type, job_title, source   from "Read company and signal"
  industry   $.fields.Industry on the trigger node
"""

# CONFIG: fill these in with the user.
JOB_POST_TOPIC = "<the tool or topic the job post signal looks for>"
PROOF_DEFAULT = "<what you offer to send, for example: how we set it up for a team like yours>"
# Optional: a second proof line for one kind of company. Leave the set empty to skip it.
PROOF_SPECIAL = "<a second case, for one kind of company>"
SPECIAL_INDUSTRIES = set()  # Clay industry names in lower case, for example {"marketing services"}
SPECIAL_SOURCES = set()  # sources that always get the special proof, for example {"lookalike"}


def text(value):
    return "" if value is None else str(value).strip()


def handler(context):
    full_name = text(context.get_input("full_name"))
    parts = full_name.split()
    first_name = parts[0] if parts else ""
    last_name = " ".join(parts[1:])
    company = text(context.get_input("company_name"))
    title = text(context.get_input("title"))
    signal_type = text(context.get_input("signal_type"))
    person_source = text(context.get_input("person_source"))

    if signal_type == "job_post":
        opener = "Saw your %s job post mentions %s." % (text(context.get_input("job_title")), JOB_POST_TOPIC)
    elif signal_type == "new_hire" and person_source == "new hire" and title:
        opener = "Saw you recently joined %s as %s." % (company, title)
    else:
        opener = ""

    industry = text(context.get_input("industry")).lower()
    source = text(context.get_input("source"))
    special = industry in SPECIAL_INDUSTRIES or source in SPECIAL_SOURCES
    return {
        "first_name": first_name,
        "last_name": last_name,
        "company_name": company,
        "opener": opener,
        "proof": PROOF_SPECIAL if special else PROOF_DEFAULT,
    }
