# Don't couple your Go code to GitHub

- Score: 323 | [HN](https://news.ycombinator.com/item?id=49868404) | Link: https://iain.rocks/blog/dont-couple-your-go-code-to-github

### TL;DR

Iain Cambridge argues that Go modules should use organization-controlled domains instead of GitHub URLs as import paths. A vanity domain can keep package identity stable while its metadata redirects the Go tool and human visitors to whichever host currently serves the repository. He cites a company retaining GitLab, GitHub, and Azure DevOps because migration had become costly. Commenters agreed control eases moves but disputed the prescription: custom domains also expire, module replacements can bridge migrations, and vendoring or content-addressed verification addresses broader namespace failures.

### Comment pulse

- Controlled domains preserve package identity → maintainers can redirect imports after changing hosts without forcing downstream source edits.
- Every namespace can fail → personal domains may lapse sooner than GitHub—counterpoint: owners can repair domains but cannot repair GitHub outages.
- Migration costs may be overstated → go.mod replacements and search-and-replace help, though downstream users can remain pinned to abandoned paths.

### LLM perspective

- View: Vanity imports trade platform coupling for domain-governance responsibility; they eliminate neither naming risk nor dependency fragility.
- Impact: Organizations gain hosting portability but must maintain DNS, TLS, metadata, and ownership continuity.
- Watch next: Signed or content-addressed modules, durable domain policies, and migration tooling for downstream consumers.
