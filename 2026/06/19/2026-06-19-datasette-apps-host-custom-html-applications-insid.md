# Datasette Apps: Host custom HTML applications inside Datasette

- Score: 137 | [HN](https://news.ycombinator.com/item?id=48593731) | Link: https://simonwillison.net/2026/Jun/18/datasette-apps/

### TL;DR

Datasette Apps embeds self-contained HTML, CSS, and JavaScript interfaces beside their data, inside sandboxed iframes that cannot access parent secrets. A strict CSP blocks unapproved outbound requests, while a MessageChannel bridge exposes allow-listed read-only SQL and specific stored write queries; queries and errors remain visible. Copyable schema-aware prompts make LLM generation convenient but optional. An AI security review found and prompted a fix for CSP-based data exfiltration. HN discussion treated the pattern as a possible successor to fixed SaaS dashboards, provided security and source management mature.

### Comment pulse

- Generated interfaces may replace fixed dashboards → commenters distinguished rigid “cathedral” app builders from flexible “bazaar” layers that expose data and SDK guarantees.
- Co-locating interface and data simplifies deployment → prior JSON-API frontends could hit CORS; filesystem storage would improve Git-based revision control.
- Browser primitives reduced custom sanitizer work → commenters praised iframe sandboxing and CSP, yet wanted extensive testing because one subtle escape could expose private data.

### LLM perspective

- **View:** The key primitive is least-authority UI code: generated frontends receive narrow data capabilities instead of ambient application credentials.
- **Impact:** Data teams can ship bespoke exploration and workflow tools faster; admins become policy authors for queries and network access.
- **Watch next:** Audit sandbox escapes, permission inheritance, CSP changes, stored-query parameterization, Git workflows, and behavior under multi-user concurrency.
