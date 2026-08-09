# The "Vibe Coding" Wall of Shame

- Score: 120 | [HN](https://news.ycombinator.com/item?id=47566491) | Link: https://crackr.dev/vibe-coding-failures

### TL;DR

Crackr AI catalogs 32 alleged AI-coding incidents across outages, data exposure, developer-tool vulnerabilities, and supply-chain attacks, then argues the shared failure is shipping generated code without understanding or review. Its headline cases include destructive agents, exposed databases, prompt-injection flaws, malicious packages, and insecure scaffolding; it also cites studies reporting widespread CSRF, SSRF, and secret-handling failures. However, the collection does not consistently establish “vibe coding” as the cause. HN readers found branding errors, weak or missing sources, unsupported Amazon impact figures, and ordinary tool or CI compromises relabeled as AI-generated failures.

### Comment pulse

- A Google employee found an unofficial Gemini tool presented with Google branding and no clear evidence AI introduced its vulnerability.
- Critics traced the top Amazon claim to a vendor advertisement that apparently did not substantiate the stated 99% order-volume loss.
- Readers favored shaming unsafe engineering regardless of authorship — counterpoint: others argued ubiquitous AI use makes the category analytically meaningless.

### LLM perspective

- **View:** This is a useful incident index but an unreliable causal dataset; association, product vulnerability, and vibe coding are conflated.
- **Impact:** Bad taxonomy can weaken legitimate security warnings by turning preventable control failures into culture-war evidence.
- **Watch next:** Primary-source verification, explicit causality criteria, corrected affiliations, denominator data, and comparisons against human-coded baselines.
