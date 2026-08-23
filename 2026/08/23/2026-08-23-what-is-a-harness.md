# What Is a Harness?

- Score: 245 | [HN](https://news.ycombinator.com/item?id=49409092) | Link: https://earendil.com/posts/what-is-a-harness/

### TL;DR

An agent harness is software surrounding a model with four elements: a system prompt, callable tools, an agentic loop that lets the model inspect results and continue, and a translation layer across providers. Interfaces may be terminal, chat, or email; locally owned harnesses can preserve sessions and let users alter instructions, tools, workflows, and models. The article uses Pi’s 5,000-plus extensions to argue this layer strengthens user agency, though it also promotes Earendil’s product. Commenters reported minimal tools and guardrails can outperform prescriptive skills, while debating handoffs, commoditization, and hype.

### Comment pulse

- Accounting agents performed better with internal CLI tools and deterministic guardrails than 2,000-line skills that overconstrained novel requests.
- Handoff proposals ranged from portable chat histories and markdown artifacts to durable workflows and orchestrators spanning people, models, and interfaces.
- Enthusiasts call harnesses the value layer—counterpoint: skeptics expect commodity software and see another fashionable label for tool-using applications.

### LLM perspective

- View: Harness design determines operational behavior and user control without changing the underlying model’s learned capabilities.
- Impact: Provider-neutral local layers can reduce lock-in, but portability depends on session formats, tool compatibility, and state management.
- Watch next: Cross-interface handoffs, durable recovery, permission guardrails, extension quality, provider switching, and evidence comparing minimal versus prescriptive designs.
