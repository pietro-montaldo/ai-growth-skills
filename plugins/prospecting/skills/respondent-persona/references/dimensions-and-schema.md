# Dimensions and schema

## The dimensions

Profile every respondent on these five. Each bucket list is fixed so the spread is countable. Anything that does not fit, or that research could not establish, is `unknown`.

### Seniority
- `executive` (C-level, VP, founder, owner, partner)
- `senior` (head, director, principal, lead)
- `mid` (manager, senior individual contributor)
- `junior` (analyst, associate, coordinator, entry)
- `student` (student, intern, no professional role)
- `unknown`

### Function
- `marketing`, `sales`, `product`, `engineering`, `data`, `operations`, `finance`, `hr`, `consulting`, `founder_exec`, `creative`, `other`, `unknown`

(`founder_exec` is for generalist founders or owner-operators whose function is "run the company". Use a specific function when the role is specialised.)

### Industry
- `software_saas`, `agency_services`, `ecommerce_retail`, `finance_fintech`, `healthcare`, `education`, `media_content`, `manufacturing`, `nonprofit_gov`, `other`, `unknown`

### Company size (headcount)
- `solo` (1)
- `micro` (2 to 10)
- `small` (11 to 50)
- `mid` (51 to 200)
- `large` (201 to 1000)
- `enterprise` (1000+)
- `unknown`

### Region
- `north_america`, `western_europe`, `eastern_europe`, `latam`, `mena`, `sub_saharan_africa`, `south_asia`, `east_asia`, `oceania`, `unknown`

## respondents.json schema

```json
{
  "meta": {
    "source": "path or description of the list",
    "project_slug": "2026-..-..-respondent-persona",
    "total_rows": 0,
    "dropped": 0,
    "researched": 0,
    "sampled": false,
    "sample_size": null
  },
  "respondents": [
    {
      "name": "",
      "email": "",
      "company": "",
      "company_source": "self_reported | email_domain | research | unknown",
      "seniority": "executive|senior|mid|junior|student|unknown",
      "function": "marketing|sales|product|engineering|data|operations|finance|hr|consulting|founder_exec|creative|other|unknown",
      "industry": "software_saas|agency_services|ecommerce_retail|finance_fintech|healthcare|education|media_content|manufacturing|nonprofit_gov|other|unknown",
      "company_size": "solo|micro|small|mid|large|enterprise|unknown",
      "region": "north_america|western_europe|eastern_europe|latam|mena|sub_saharan_africa|south_asia|east_asia|oceania|unknown",
      "confidence": "high|medium|low",
      "evidence": "one short line on what the read is based on, or 'no web result'"
    }
  ]
}
```

Notes:
- `confidence` is the sub-agent's overall read for that person. `high` = self-reported or a clear named source. `medium` = reasonable inference from a found page. `low` = thin or indirect signal.
- `evidence` keeps the persona auditable. One line, specific. "Title from company About page" beats "found online".
- The build script counts every dimension field, including `unknown`, so the spread always sums to the researched total.
