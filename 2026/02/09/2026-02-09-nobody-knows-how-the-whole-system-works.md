# Nobody knows how the whole system works

- Score: 276 | [HN](https://news.ycombinator.com/item?id=46941882) | Link: https://surfingcomplexity.blog/2026/02/08/nobody-knows-how-the-whole-system-works/

### TL;DR
Article argues modern systems are so layered and distributed that no individual can grasp them end‑to‑end, citing telephony, CPUs, operating systems, and web stacks. Abstractions and partial, sometimes wrong, mental models are unavoidable; interviews should probe how people handle their knowledge limits, not expect omniscience. The contentious twist is generative AI: it amplifies productivity while pushing us further from underlying mechanisms. HN commenters debate when abstraction becomes dangerous, how AI reshapes “ownership,” and whether dependency churn is the real systemic risk.

### Comment pulse
- LLMs risk devs understanding neither business goals nor code internals, becoming ticket-clickers. — counterpoint: others say AI frees attention for core problem-solving.  
- Abstractions without understanding are normal; concern is LLMs stopping people learning build them. Some suggest DSL-first systems, easier for humans and AIs to reason about.  
- Biggest practical failure mode is dependency churn: hundreds of libraries with unstable interfaces, poor EOL tracking, and security issues—far scarier than ignorance of transistor physics.  

### LLM perspective
- View: Treat “nobody understands everything” as design constraint; encode ownership boundaries, escalation paths, and failure modes explicitly.  
- Impact: Developer roles tilt toward system modeling, interface definition, and risk assessment, while routine coding increasingly becomes AI-orchestrated infrastructure.  
- Watch next: empirical studies on AI-written production incidents, dependency lifecycles, and training practices that preserve deep expertise under high-level tooling.
