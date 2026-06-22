# Building reliable agentic AI systems

- Score: 177 | [HN](https://news.ycombinator.com/item?id=48615680) | Link: https://martinfowler.com/articles/reliable-llm-bayer.html

### TL;DR
Bayer’s PRINCE platform turns decades of fragmented preclinical drug data into a conversational assistant. It evolved from simple metadata search to an “agentic” system orchestrated with LangGraph: clarify intent, plan steps, then route to a Researcher (hybrid RAG over PDFs plus text‑to‑SQL on Athena), a Reflection agent that checks data sufficiency, and a Writer that assembles answers. Strong state management, retries, observability, and selective context routing aim to make complex scientific queries reliably answerable at production scale.

---

### Comment pulse
- Safety concern: commenters see 3.1/5 user score and explicit hallucination monitoring as unacceptable for drug research—counterpoint: author says score is feature-maturity; outputs remain cited, human‑reviewed.  
- Data > agents: practitioners report 99% effort is cleaning, harmonizing source databases; dynamic API fetches hurt consistency and quotas—counterpoint: direct system writes complicate centralized lakes.  
- Meta-critique: some dismiss the architecture as dated, over-explaining generic RAG and under-emphasizing evaluation; others argue rigorous eval datasets and CI-embedded tests are the real differentiator.

---

### LLM perspective
- View: treating agents as modular, testable components around domain data offers more leverage than chasing ever-bigger models or contexts.  
- Impact: organizations with messy regulatory documents can reuse this pattern to turn archives into queryable assistants without replacing legacy systems.  
- Watch next: shared open eval sets for agentic workflows, techniques for safe write-capable agents, and patterns for multi-tenant data isolation.
