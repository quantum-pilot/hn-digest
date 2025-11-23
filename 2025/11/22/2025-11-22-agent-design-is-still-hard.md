# Agent design is still hard

- Score: 333 | [HN](https://news.ycombinator.com/item?id=46013935) | Link: https://lucumr.pocoo.org/2025/11/21/agents-are-hard/

### TL;DR
Building reliable LLM agents is still largely bespoke engineering. Ronacher argues generic “agent SDKs” (e.g., high-level wrappers over OpenAI/Anthropic) break down once you hit real tool use: provider-specific quirks, caching semantics, and tool formats force you back to raw APIs and your own loop. His stack emphasizes explicit cache points, reinforcement messages on every tool call, failure isolation (subagents + context editing), a shared virtual filesystem for all tools, an explicit “output tool,” and careful model choice. Testing/evals remain the hardest unsolved problem. HN replies echo: abstractions churn fast, thin custom loops often beat frameworks, and many products risk being worse than baseline Claude/ChatGPT.

---

### Comment pulse
- Agent patterns/SDKs change weekly → many “clever” designs quickly obsolete; sometimes best move is to wait and avoid building around transient quirks — counterpoint: over-waiting means never learning or shipping.  
- Practitioners report SDK pain → high-level “one interface” layers leak; several revert to hand-rolled ReAct-style loops, while others lean into Claude Code despite lock-in risks.  
- Split future vision → some advocate minimal custom frameworks and open tooling; others expect agent platforms to converge into heavy “game engine”-style stacks for most serious products.

---

### LLM perspective
- View: The real difficulty is lifecycle: state, failures, reinforcement, and evals—far beyond “tool calling” API ergonomics.  
- Impact: Teams that treat agents like distributed systems (observability, caching, isolation) will outperform prompt-only or SDK-driven efforts.  
- Watch next: Native agent features from providers: standardized shared state, safe context editing, richer traces, and first-class evaluation pipelines.
