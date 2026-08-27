# What the hell have you built

- Score: 300 | [HN](https://news.ycombinator.com/item?id=45832803) | Link: https://wthhyb.sacha.house/

### TL;DR

A tiny satirical page asks why a product serving twelve users needs fifteen microservices, eight databases, three Kubernetes environments, four queues, a service mesh, and a two-hour CI pipeline with six tests. Its prescription is one server and PostgreSQL, perhaps Redis, with complexity added only after demand proves necessary. The discussion treats the joke as a critique of engineering incentives: elaborate architecture can provide résumé value, hiring justification, or comfortable technical work while teams avoid harder questions about users, sales, legal constraints, and product viability.

### Comment pulse

- Several commenters argued even Redis was premature, sharpening the page’s point about reflexive infrastructure choices.
- Others noted the satire itself ships through a modern frontend toolchain, either as irony or evidence that tools are not architecture.

### LLM perspective

- View: Architecture is an economic and organizational choice, not merely a catalogue of technically valid components.
- Impact: Small teams can recover delivery speed by matching infrastructure to measured demand and operational capacity.
- Watch next: Actual workload, service objectives, deploy time, on-call burden, and a credible deletion plan for components.
