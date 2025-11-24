# 73% of AI startups are just prompt engineering

- Score: 219 | [HN](https://news.ycombinator.com/item?id=46024644) | Link: https://pub.towardsai.net/i-reverse-engineered-200-ai-startups-73-are-lying-a8610acab0d3

- TL;DR  
  The author probes ~200 funded “AI startups” by inspecting network calls and binaries, finding about 73% just call third‑party LLM APIs (mainly OpenAI and Anthropic) behind thin UIs or workflow shells while marketing “proprietary” AI. He argues many have weak moats and are exposed to provider pricing and policy shifts. HN commenters resonate with the prevalence of prompt‑demo theater, debate whether scaffolding/evals count as real innovation, question parts of the methodology, and note wrappers can still be legit if honestly sold.

- Comment pulse  
  - Most “AI agents” are fragile prompt scripts → months of tooling work, but few reliable deployments; flashy demos impress management, not practitioners.  
  - “Just prompt engineering” misses the hard parts → good evals, tool-calling scaffolding, caching; — counterpoint: commenters say most corporate AI projects skip rigorous evals entirely.  
  - Some doubt the study’s rigor and network-inspection method → API calls from frontends are insecure; yet many agree wrapper startups overstate novelty, echoing AI-bubble concerns.

- LLM perspective  
  - View: The core problem is overstated originality and opaque dependency on a few LLM vendors, not API reuse itself.  
  - Impact: Founders anchored on single providers inherit their risk profile; investors may back interchangeable tools without durable differentiation.  
  - Watch next: Look for startups owning data, workflows, or specialized models; API price shifts will quickly stress test prompt-only businesses.
