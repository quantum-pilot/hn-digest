# Learning Software Architecture

- Score: 514 | [HN](https://news.ycombinator.com/item?id=48106024) | Link: https://matklad.github.io/2026/05/12/software-architecture.html

### TL;DR
Matklad argues software architecture is mostly learned through practice and constrained by social structures, not formal design methods. Using rust-analyzer, he shows how technical choices (simple builds, isolated crashy features, stricter “spine”) were driven by contributor incentives: core hackers vs weekend warriors. He urges occasionally shaping incentives, but usually adapting to them, noting experiments can unexpectedly become critical infrastructure. He recommends talks, essays, and a few books over any single canonical text, while HN adds heuristics and classic architecture literature.

### Comment pulse
- Design heuristics → coherent idea, minimal surprise, explicit state, single data truth, naming, and costs guide systems—counterpoint: every rule depends heavily on context.  
- Best architecture training → maintain large multi-team systems across several orgs; compare designs; observe incentives like billable-hours and promotions favoring greenfield over long-term maintenance.  
- Architecture references → Shaw and Garlan, Mary Shaw’s work, hexagonal architecture, REST, and Architecture of Open Source Applications emphasize history, constraints, and connectors over components.  

### LLM perspective
- View: Architecture emerges from incentives plus constraints; leaders should design contribution pathways as deliberately as module boundaries and data models.  
- Impact: Researchers and scientists can treat “scientific code” as social systems, aligning tooling with publication timelines and transient contributor availability.  
- Watch next: Study how build friction, test latency, and review policies affect contributor retention and architectural quality in open tools.
