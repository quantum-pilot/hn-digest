# What the hell have you built

- Score: 300 | [HN](https://news.ycombinator.com/item?id=45832803) | Link: https://wthhyb.sacha.house/

- TL;DR
    - Engineers often overengineer early projects—microservices, cloud-native stacks, extra caches—not because needs demand it, but to avoid unglamorous work or signal sophistication. HN threads recount resume-driven architectures and interviews rewarding buzzwords over fit, contrasted with pragmatic monolith-first approaches. A lively subthread debates caching: Postgres or in‑memory vs Redis/memcached, with scale and simplicity trade‑offs. Some note the irony of using modern front-end stacks to preach minimalism. The underlying message from a 2013 meme: minimize complexity until real constraints appear.
    - Content unavailable; summarizing from title/comments.

- Comment pulse
    - Overengineering is procrastination → avoids sales/legal/customer work while feeling productive; maturity means prioritizing impact over "fun" architectures.
    - Resume-driven development → hiring screens reward trendy stacks, pressuring candidates to mirror preferences; some firms de-emphasize language experience.
    - Redis debate → Postgres or in-memory often suffice; Redis/memcached add speed under high read load — counterpoint: stateful caches risk bad designs and consistency assumptions.

- LLM perspective
    - View: Default to a monolith with a simple DB; delay caching/distribution until profiling reveals bottlenecks.
    - Impact: Early-stage teams ship faster; hiring managers refocus on fundamentals over tool checklists.
    - Watch next: Set thresholds: p95 latency, peak QPS, cost per user; test with load; document when to introduce Redis, queues, or services.
