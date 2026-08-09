# Full Disclosure: A Third (and Fourth) Azure Sign-In Log Bypass Found

- Score: 280 | [HN](https://news.ycombinator.com/item?id=47448994) | Link: https://trustedsec.com/blog/full-disclosure-a-third-and-fourth-azure-sign-in-log-bypass-found

### TL;DR

TrustedSec disclosed two more Entra ID sign-in logging bypasses, bringing its total since 2023 to four. Repeating a valid `openid` scope roughly 10,000–35,000 times, or supplying an approximately 50,000-character User-Agent, could return a Graph bearer token without producing the expected portal or Log Analytics sign-in record. Microsoft fixed both; the researcher says the likely database-field overflow remains unconfirmed and criticizes the moderate rating and absent bounty. HN focused on fail-open audit pipelines, broader distrust of Azure logs, and authentication complexity.

### Comment pulse

- Authentication succeeded while logging apparently failed → readers suspected oversized fields broke a separate audit insertion without blocking token issuance.
- Azure’s audit trail drew broader distrust → commenters shared stale-interface and misleading-log experiences beyond these specific bypasses.
- Microsoft’s response frustrated researchers → fixes arrived after reproduction, but severity, recognition, and incentives remained contested.

### LLM perspective

- **View:** Security logging must fail visibly and independently verify completeness whenever authentication and audit storage are decoupled.
- **Impact:** Defenders cannot treat Entra sign-in logs alone as authoritative evidence of account activity.
- **Watch next:** Root-cause disclosure, regression fuzzing, schema hardening, bounty policy, and adoption of Graph-activity correlation queries.
