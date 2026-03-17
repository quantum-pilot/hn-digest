# How I write software with LLMs

- Score: 468 | [HN](https://news.ycombinator.com/item?id=47394022) | Link: https://www.stavros.io/posts/how-i-write-software-with-llms/

### TL;DR
The author describes a concrete workflow for “LLM-first” software development: a strong “architect” model collaborates with the human to design features, a cheaper “developer” model implements them, and 1–3 different “reviewer” models critique diffs. He shows a full transcript of adding email support to his agentic system Stavrobot, emphasizing that his job has shifted from writing functions to steering architecture and catching blind spots. This works well when he understands the tech; it fails when he doesn’t.

---

### Comment pulse
- Multi-agent vs single model → Many argue a single strong model with good prompts rivals complex architect/developer/reviewer setups—counterpoint: multiple models find different issues and allow cost control.  
- Orchestration patterns → Some use richer pipelines (planner, executor, QA) and external tools like Notion; others see role-splitting as transient scaffolding that models will soon absorb.  
- Human skill still central → Results depend more on user expertise, task decomposition, and giving LLMs validation hooks than on fancy prompt rituals or anthropomorphic agent hierarchies.

---

### LLM perspective
- View: Multi-model, role-split workflows help most when projects are large, architectures matter, and token cost differentials are significant.  
- Impact: Strong developers become system designers, spec writers, and reviewers; weaker devs risk becoming button-pushers for brittle agent setups.  
- Watch next: Benchmarks comparing single-model vs orchestrated systems, IDE-integrated orchestrators, and patterns for safe side-effect isolation in agent workflows.
