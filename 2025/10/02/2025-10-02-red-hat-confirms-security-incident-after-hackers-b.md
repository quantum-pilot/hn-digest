# Red Hat confirms security incident after hackers breach GitLab instance

- Score: 231 | [HN](https://news.ycombinator.com/item?id=45448772) | Link: https://www.bleepingcomputer.com/news/security/red-hat-confirms-security-incident-after-hackers-claim-github-breach/

### TL;DR

Red Hat confirmed that an unauthorized party accessed and copied data from a self-managed GitLab Community Edition instance used by its consulting division. The instance contained engagement reports with project specifications, example code, and internal communications. Extortion group Crimson Collective separately claimed theft of 570GB across 28,000 repositories and access to credentials and downstream systems; Red Hat did not verify those claims. The company isolated the instance, added hardening, contacted authorities and customers, and said products and its software supply chain were unaffected.

### Comment pulse

- Readers mocked the attackers reportedly receiving a templated vulnerability-report response to an extortion attempt.
- Several corrected early confusion: this involved Red Hat's self-managed GitLab instance, not GitHub or GitLab's hosted platform.

### LLM perspective

- View: Confirmed consulting-data theft is serious even without evidence that Red Hat's product supply chain was compromised.
- Impact: Engagement repositories can concentrate customer architecture and operational context useful for follow-on attacks.
- Watch next: Customer notifications, token rotation, forensic scope, access path, dwell time, and verified downstream misuse matter.
