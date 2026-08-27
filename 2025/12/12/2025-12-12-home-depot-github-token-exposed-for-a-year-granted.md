# Home Depot GitHub token exposed for a year, granted access to internal systems

- Score: 260 | [HN](https://news.ycombinator.com/item?id=46247000) | Link: https://techcrunch.com/2025/12/12/home-depot-exposed-access-to-internal-systems-for-a-year-says-researcher/

### TL;DR

Researcher Ben Zimmermann found a Home Depot employee's GitHub token publicly exposed since early 2024. He says it could modify hundreds of private repositories and exposed credentials touching cloud infrastructure, fulfillment, inventory, and development pipelines. Home Depot ignored several private reports and lacked a published vulnerability-reporting channel; the token disappeared and was revoked only after TechCrunch contacted the company. Home Depot did not say whether logs could determine if anyone else used the credential during its roughly year-long exposure.

### Comment pulse

- Readers expect legal review to suppress details, but argue a disclosure channel could have shortened exposure by weeks.
- GitHub and Anthropic receive praise for automatically revoking leaked keys; experiences with other providers show inconsistent detection and remediation.

### LLM perspective

- View: The deepest failure was not one leaked token, but excessive scope combined with ineffective external reporting.
- Impact: Repository compromise could bridge into operational systems when code, secrets, and pipelines share long-lived credentials.
- Watch next: Demand audit findings, token-scope reduction, secret scanning, rotation automation, and a formal disclosure program.
