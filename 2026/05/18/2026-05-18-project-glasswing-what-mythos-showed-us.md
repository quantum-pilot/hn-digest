# Project Glasswing: what Mythos showed us

- Score: 266 | [HN](https://news.ycombinator.com/item?id=48179732) | Link: https://blog.cloudflare.com/cyber-frontier-models/

## TL;DR
Cloudflare used Anthropic’s Mythos Preview, a security-focused LLM, to scan over 50 internal repos and found it a step-change from generic models: it can chain multiple low-severity bugs into realistic exploit paths and autonomously generate, compile, and run PoCs, greatly improving triage quality. Generic “point an agent at a repo” approaches failed, so they built a multi-stage, highly parallel harness with adversarial validation and reachability tracing. Mythos shows inconsistent, emergent guardrails, and Cloudflare argues that architecture and isolation matter more than just “patch faster.”

## Comment pulse
- “Different kind of tool” claim → feels like marketing; post rehashes Mythos launch and lacks concrete metrics — counterpoint: the harness design is substantively new.  
- AI-written vibe → phrasing and tone suggest LLM-assisted corporate copy; some note Cloudflare blogs are increasingly AI-edited, though still technically respectable.  
- Interesting bits → emergent, inconsistent refusals even in a gated security model, and explicit adversarial-review harness, are seen as genuinely useful takeaways.  

## LLM perspective
- View: The real innovation is the orchestrated harness: many narrow tasks, adversarial review, and reachability analysis, not Mythos alone.  
- Impact: Security teams will need pipeline and architectural changes, not just faster scanners or auto-patching, to handle dual-use “cyber frontier” models.  
- Watch next: Quantitative benchmarks vs human red teams, open-source harness patterns, and vendor offerings that expose Mythos-like workflows as managed services.
