# Software is made between commits

- Score: 316 | [HN](https://news.ycombinator.com/item?id=48492533) | Link: https://zed.dev/blog/introducing-deltadb

## TL;DR
Zed’s blog argues that modern software is shaped more by the ongoing conversation with humans and AI agents than by final commits. Their new DeltaDB system versions every fine-grained edit (“delta”) and directly links it to the chat that produced it, so you can jump from any conversation snippet to the exact code state (and vice versa). The goal is agent-centric, real‑time collaboration that reduces pull‑request ceremony, while Git remains for CI and external integration. HN debates whether this is powerful, redundant, or invasive.

---

## Comment pulse

- Commits as narrative units → Many prefer small, curated commits that tell a clean story; intermediate “soup” is noise. — counterpoint: dense histories aid bisecting and debugging.  

- Git already supports this → Frequent auto‑commits plus `--no-ff`, `--first-parent`, and better UIs can model “conversation” history without inventing a new backend.  

- Feels like surveillance → Capturing every edit and thought process is seen as intrusive, tool‑lock‑in heavy, and likely to entrench sloppy commits and AI‑centric workflows.

---

## LLM perspective

- View: Treating code+conversation as a unified artifact matches how AI coding partners already work; DeltaDB formalizes that stream.  

- Impact: Strongest for teams leaning heavily on agents, remote pairing, and continuous review; privacy‑sensitive orgs may resist always‑on capture.  

- Watch next: Concrete UX: filters over deltas, privacy controls, Git interoperability, and whether agents demonstrably debug/maintain better using this rich history.
