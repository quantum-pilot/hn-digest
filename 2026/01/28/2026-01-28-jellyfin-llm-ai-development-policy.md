# Jellyfin LLM/"AI" Development Policy

- Score: 116 | [HN](https://news.ycombinator.com/item?id=46801976) | Link: https://jellyfin.org/docs/general/contributing/llm-policies/

## TL;DR

Jellyfin has formalized a strict but LLM-tolerant development policy. Any direct communication in their ecosystem (issues, PR descriptions, comments, forum posts) must be written by humans, with a narrow exception for clearly labeled translation help. LLM-assisted code is allowed only if contributors fully understand, test, and can personally explain changes, keep PRs small and focused, and clean up “slop.” Third‑party LLM-built tools are allowed but must be clearly labeled and respect licenses. HN commenters largely welcome this as protection against low‑effort “vibe-coded” spam.

---

## Comment pulse

- Ban LLM-written communication → improves clarity, authenticity, and reviewability, while still allowing AI for translation and editing.

- Maintainers see floods of messy, multi-issue LLM PRs → slows bugfixing, threatens open PR models — counterpoint: responsibility norms already existed pre-LLM.

- Some want standardized “Agent Policies” for AI tools → akin to PEP-8 or licenses; others say contributors should just read each project’s existing guidelines.

---

## LLM perspective

- View: Treat LLMs as power tools, not autonomous contributors; humans remain the accountable authors of both text and code.

- Impact: Projects gain cover to close slop quickly; serious contributors must integrate testing, review, and explanation into AI-assisted workflows.

- Watch next: Standardized LLM contribution policies and tooling that surfaces project rules to AI agents before generating patches.
