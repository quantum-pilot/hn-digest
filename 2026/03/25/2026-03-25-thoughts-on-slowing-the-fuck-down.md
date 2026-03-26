# Thoughts on slowing the fuck down

- Score: 614 | [HN](https://news.ycombinator.com/item?id=47517539) | Link: https://mariozechner.at/posts/2026-03-25-thoughts-on-slowing-the-fuck-down/

- TL;DR  
  An experienced coding-agent framework author argues that fully autonomous agents are rapidly turning codebases into brittle, over-complex messes. Agents repeat the same design and code-smell mistakes at machine speed, lack global understanding, and amplify bad patterns, while humans relinquish the bottlenecks and pain that normally trigger cleanup. He advocates “slowing down”: humans should design architecture, tightly scope agent tasks, and review critical code. HN adds debates on software-as-engineering, AI vendor lock-in, and how organizational culture shapes failure rates.

- Comment pulse  
  - Tool panic repeats every era; the real axis is “what are you building” and whether decisions follow evidence (engineering) or vibes/authority.  
  - Agentic development risks deep AI-vendor lock-in and future price hikes; later humans may struggle to understand AI-shaped codebases — counterpoint: hardware should cut inference costs.  
  - Ops veterans say software was always messy; automation and AI just accelerate deployments, so without error budgets or Andon-cord culture, outages surface faster and louder.  

- LLM perspective  
  - View: Treat agents as fast but uneducated juniors; constrain scope, require design docs, and mandate human review for user-facing change.  
  - Impact: Organizations that institutionalize error budgets, incident learning, and codebase ownership will extract lasting value from agents; others amplify chaos.  
  - Watch next: Whole-repo indexing, semantic search, and verifiable refactoring pipelines could raise agentic recall and tame complexity in large systems.
