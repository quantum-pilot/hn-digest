# The new rules of context engineering for Claude 5 generation models

- Score: 121 | [HN](https://news.ycombinator.com/item?id=49051361) | Link: https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models

## TL;DR
Anthropic explains how Claude 5 models made most of Claude Code’s giant system prompts obsolete: they removed 80% of the prompt with no regression. The new “context engineering” advice is to stop overconstraining models and instead rely on their judgment, better tool interfaces, progressive disclosure of instructions, and rich code‑like references. CLAUDE.md and Skills should be lighter, modular guides that load when needed, while auto‑memory and artifacts handle longer‑term context. HN replies are skeptical about Opus 5 quality and vendor lock‑in.

---

## Comment pulse
- Opus 5 feels worse than 4.x → more mistakes, accidental deletions, verbosity, and higher token use; simplification looks like lock‑in via proprietary tooling.  
- Context engineering vs programming → joke that “designing a precise language” is just programming; LLM usage implies current languages still poorly match human problem domains.  
- Split workflows → some prefer minimal prompts and manual edits; others distrust auto‑memory and stick to explicit context files—counterpoint: centralized CLAUDE.md can encode persistent preferences once.

---

## LLM perspective
- View: Stronger models shift value from giant system prompts to tool design, modular skills, and high‑fidelity code/spec references.  
- Impact: Agent builders must treat context layout, routing, and memory boundaries as core product design, not one‑off prompt hacks.  
- Watch next: Benchmarks of Opus 5 vs 4.x on real workflows, configurable/inspectable memory, and open, portable harness formats to reduce lock‑in fears.
