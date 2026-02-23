# How I use Claude Code: Separation of planning and execution

- Score: 867 | [HN](https://news.ycombinator.com/item?id=47106686) | Link: https://boristane.com/blog/how-i-use-claude-code/

### TL;DR
Author describes a disciplined Claude Code workflow that strictly separates “thinking” from “typing.” Every task starts with deep codebase research written to `research.md`, then a detailed `plan.md`. The human annotates that plan inline through multiple “don’t implement yet” cycles, turning it into a precise spec plus granular TODO list. Only then does Claude “implement it all” in one boring, typechecked pass, within a single long session. HN debates whether this is robust engineering, prompt superstition, or overgrown waterfall.

---

### Comment pulse
- Main benefit is exposing hidden assumptions early → plans and reviews become a debugging surface for architecture and constraints, not just syntax.  
- “Deeply / intricacies” wording supposedly steers models to expert-like corpus regions → skeptics call this superstition without rigorous prompt-effect statistics — counterpoint: practitioners report consistent, empirical gains.  
- Several prefer phased execution, persistent knowledge bases, and explicit test planning → avoid monolithic code dumps and teach the model reusable project rules.

---

### LLM perspective
- View: This pattern effectively turns the model into an execution engine for living specs, mirroring good human software design practices.  
- Impact: Best suited to complex, long-lived codebases where architectural stability and domain nuance matter more than rapid throwaway prototyping.  
- Watch next: IDE/workflow tools that first-class `research.md`/`plan.md`/status docs and measure defect rates versus ad-hoc chat-driven coding.
