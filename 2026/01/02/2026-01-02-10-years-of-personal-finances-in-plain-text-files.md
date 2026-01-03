# 10 years of personal finances in plain text files

- Score: 415 | [HN](https://news.ycombinator.com/item?id=46463644) | Link: https://sgoel.dev/posts/10-years-of-personal-finances-in-plain-text-files/

### TL;DR
- The author has tracked all personal finances for 10 years using Beancount: a double-entry system with plain-text ledgers in git, updated monthly in 30–45 minutes.  
- CSV statements are run through custom Python importers for German banks, then manually/automatically balanced; historical years are split into separate files, with ~10k transactions and ~500 attached PDFs.  
- HN commenters praise Beancount and the author’s book, share similar PTA (plain-text accounting) setups, but debate tradeoffs vs Quicken-style automatic syncing and whether “plain text” itself really matters.

---

### Comment pulse
- Double-entry as key idea → prevents money “appearing from nowhere”; some needed Kleppmann’s explanation, others find it trivially obvious — counterpoint: graph-theory framing seems unnecessary to some.  
- Plain-text accounting workflows → scripts + build-system-like pipelines for CSV/PDF imports, version control, reproducibility; can iteratively improve rules and regenerate all history.  
- Lock-in vs convenience → PTA avoids proprietary blobs and EOL pain, but Quicken’s automated multi-account syncing is hard to give up for fraud detection and daily reconciliation.

---

### LLM perspective
- View: Plain-text + double-entry + importers forms a durable “data substrate” for personal finance, independent of any vendor UI or app.  
- Impact: Power users, freelancers, and retirees gain auditability, tax readiness, and resilience against product shutdowns or format changes.  
- Watch next: Better open-source sync connectors, privacy-preserving local LLM helpers for rule-writing, and friendlier UIs atop Beancount/hledger-style backends.
