# Control the Ideas, Not the Code

- Score: 203 | [HN](https://news.ycombinator.com/item?id=48891184) | Link: https://antirez.com/news/169

- TL;DR  
Antirez argues that in an LLM-driven world developers should specify architecture, constraints, and concepts, then let agents generate and maintain the code, largely unread. Commenters report models gravitate toward familiar frameworks and styles, so “controlling ideas” requires heavy constraint, iteration, and review. Many feel sidelined or redefined as project managers, worrying about trust, bugs, and how juniors will learn. Others share shipped systems built mostly by LLMs, seeing code-reading as optional but curation, testing, and execution as central.  
*Content unavailable; summarizing from title/comments.*

- Comment pulse  
  - LLMs resist unusual architectures, drifting to popular stacks; “idea control” demands tight constraints on tools and APIs—counterpoint: strong constraints can push models out-of-distribution.  
  - Some embrace agentic coding, barely typing, but still catch cascading bad decisions; they reject fully trusting unread code, seeing that as abandoning real engineering.  
  - Others say ideas at design-level matter most; LLMs cheaply turn them into products, even for non-programmers, but long-term maintainability and developer education remain open questions.

- LLM perspective  
  - View: Coding shifts from keystrokes to specifying invariants, interfaces, and tests; “idea control” is really rigorous requirements and constraint engineering.  
  - Impact: Senior engineers become architecture and quality stewards; juniors may need sandboxed projects or curricula emphasizing debugging AI-generated systems.  
  - Watch next: Tooling that enforces constraints, traces agent decisions, and measures real-world reliability of LLM-built systems versus traditional teams.
