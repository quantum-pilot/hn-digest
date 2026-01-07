# Opus 4.5 is not the normal AI agent experience that I have had thus far

- Score: 245 | [HN](https://news.ycombinator.com/item?id=46515696) | Link: https://burkeholland.github.io/posts/opus-4-5-change-everything/

## TL;DR
A senior dev describes Claude Opus 4.5 as the first AI agent that reliably ships real apps: a Windows utility, a screen recorder/editor, and two Firebase‑backed iOS business tools, all built largely by the model orchestrating CLIs, infra, auth, and CI. This pushes him to an “AI‑first” view of programming where code is written and maintained for LLMs, not humans. HN replies range from “agents are already super‑teammates in production” to “they’re still toy‑grade, hallucination‑prone, and rarely survive the last 20% to production.”

---

## Comment pulse
- Agents as force multipliers → Teams wire Claude/Opus into repos, linting, PR review, docs, and ticket triage; much maintenance becomes automated scheduled workflows.  
- Limits and failure modes → Hallucinated CLIs/features, stuck debugging, poor UI reasoning; great at boilerplate, backends, and analysis, but not yet rivaling top humans on complex systems.  
- From toys to products → LLMs accelerate prototypes, but motivation, UX/context, deployment, and maintenance still bottleneck; many “vibe‑coded” projects stall before production hardening.

---

## LLM perspective
- View: Treat models as primary readers/writers of code; humans design specs, architecture, and constraints, then supervise and audit.  
- Impact: Solo devs and small teams gain leverage; commodity CRUD work devalues, while product sense, security, and operations gain importance.  
- Watch next: Robust security review agents, reproducible agent workflows, and case studies of long‑lived, revenue‑generating systems built and maintained mostly by AI.
