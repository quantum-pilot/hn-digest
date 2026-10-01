# I could've accessed 17T Microsoft records

- Score: 310 | [HN](https://news.ycombinator.com/item?id=49883970) | Link: https://blog.faav.net/how-i-couldve-accessed-17-trillion-microsoft-records

### TL;DR

A 16-year-old researcher found Microsoft’s internal Titan analytics API accepted login-token claims without verifying their signature, enabling administrator-level SQL queries. Metadata indicated 17.3 trillion rows were technically reachable across connected analytics systems, but that estimate included historical, duplicated and derived data; the researcher did not dump those records, access customer PII or correlate users, instead limiting validation to metadata and bounded samples. Microsoft restricted the endpoint by September 9, awarded $5,000, and exercised editorial control over the coordinated write-up.

### Comment pulse

- Many considered Microsoft’s editorial control inappropriate → Others argued coordinated editing is normal when a bounty enables responsible public disclosure.
- Readers called the $5,000 award stingy → Counterarguments said bounty prices reflect exploitability and operational value, not headline-scale theoretical exposure.
- Developers criticized accepting unsigned identity claims → Existing internal authentication libraries were cited as safeguards that teams still must adopt.

### LLM perspective

- View: Layered authorization is meaningless when the foundational identity proof is not authenticated.
- Impact: Central analytics gateways can amplify one validation failure across otherwise separate datasets.
- Watch next: Microsoft’s remediation should include service-wide audits for deferred identity-library compliance.
