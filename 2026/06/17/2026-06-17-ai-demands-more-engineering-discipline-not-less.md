# AI demands more engineering discipline. Not less

- Score: 329 | [HN](https://news.ycombinator.com/item?id=48570948) | Link: https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline

## TL;DR
Majors argues that once AI made “median engineer–quality” code cheap and fast, code stopped being the core asset and became a disposable cache of understanding. The real product is system behavior in production plus the human knowledge encoded as specs, tests, invariants, and observability. Nondeterministic AI components therefore require *more* engineering discipline—richer evaluation harnesses, tighter feedback loops, and better architecture/behavior artifacts—not a laissez-faire collapse of rigor. HN commenters worry about unreadable AI sludge, unseen tech debt, and where meaningful human work now lives.

---

## Comment pulse
- AI makes everyone look prolific → distinguishing deep understanding from copypasta is harder; orgs risk drowning in plausible artifacts and unprecedented technical debt.  
- Reading AI sludge is exhausting → better to treat prompts, plans, and behavioral tests as the durable artifact; giant LLM diffs are effectively unreviewable.  
- Perfect specs may be as hard as code → yet much modern work is compositional, so “good-enough” models plus LLMs already accelerate useful, non-exotic systems.

---

## LLM perspective
- View: The real leverage is in encoding tacit knowledge into specs, evals, observability, and regeneration workflows; codegen is increasingly commoditized.  
- Impact: SREs, QA, and tech leads gain prominence; hiring must weight system thinking and evaluation design over raw coding output.  
- Watch next: Tools that version prompts/sessions as first-class artifacts, standardized eval-in-prod frameworks, and postmortems explicitly tagging AI-induced complexity or debt.
