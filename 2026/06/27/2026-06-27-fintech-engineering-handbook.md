# Fintech Engineering Handbook

- Score: 451 | [HN](https://news.ycombinator.com/item?id=48696982) | Link: https://w.pitula.me/fintech-engineering-handbook/

### TL;DR
The handbook aims to collect “standard” fintech engineering practices—money representation, immutability, logging, and PII handling—but commenters find it uneven and sometimes misleading. Most discussion centers on how to represent monetary values (integers, fixed‑point, doubles, BigDecimal, strings, mantissa+exponent) and the pitfalls of JSON numbers. Engineers also debate how far to push event sourcing versus simpler append‑only audit logs, and warn that any generic handbook must be subordinated to domain realities and jurisdiction‑specific compliance rules.  
*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Money representation is domain‑specific → consumer ledgers favor integers/fixed‑point; quant pricing accepts doubles; others prefer decimals or mantissa+exponent for interoperability and precision—counterpoint: insisting on integers everywhere is unrealistic.

- Event sourcing vs logs → some want full event sourcing for anything touching money; others succeed with append‑only audit trails, effectively‑once processing, and explicit data lineage handling vendor updates.

- Trust and compliance → some praise the consolidation of knowledge; others suspect LLM authorship and stress that legal/KYC/AML rules can’t be derived from a generic online handbook.

---

### LLM perspective
- View: Treat “how to store amounts” as a protocol design problem; make representation explicit per API, asset, and counterparty.

- Impact: Fintech teams must budget early for precision, reconciliation, lineage, and legal retention instead of retrofitting after growth or regulation.

- Watch next: Community-driven JSON/Protobuf money schemas (mantissa+exponent+currency), reference libraries, and clearer regulatory guidance on separating PII from immutable financial history.
