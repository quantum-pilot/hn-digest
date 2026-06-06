# CISA Admin Leaked AWS GovCloud Keys on GitHub

- Score: 402 | [HN](https://news.ycombinator.com/item?id=48190454) | Link: https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/

### TL;DR
A CISA contractor kept a public GitHub repo containing AWS GovCloud admin keys, plaintext passwords for dozens of internal systems, and access to CISA’s software supply chain. The repo appears to have been used as a personal sync space, with GitHub’s secret‑scanning explicitly disabled; experts verified the keys still worked for 48 hours after disclosure. CISA says it sees no confirmed compromise yet, while observers debate whether this is individual malpractice, systemic oversight failure, or both.

### Comment pulse
- Outrage at passwords.csv, weak creds, and non‑response to GitGuardian → seen as gross negligence, not excusable by tight budgets or contractor status.  
- Practitioners say secret leakage via Git is common → argue for enforced org‑wide scanners and note CISA’s 2025 staff purges likely weakened oversight.  
- LLMs flagged as parallel exfiltration risk → secrets in .env or logs can silently reach training data—counterpoint: dev secrets should already be low‑impact.

### LLM perspective
- View: Core failure is treating GitHub as personal scratch space for production secrets instead of assuming every sync path is adversarial.  
- Impact: Gov and regulated sectors will face mandates: enforced secret scanning, short‑lived creds, bans on unmanaged personal repos for work.  
- Watch next: Expect guidance on LLM use in secure environments: internal models, red‑teaming prompts, and guardrails like OS‑level agents restricting file access.
