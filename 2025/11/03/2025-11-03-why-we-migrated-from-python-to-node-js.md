# Why we migrated from Python to Node.js

- Score: 205 | [HN](https://news.ycombinator.com/item?id=45800955) | Link: https://blog.yakkomajuri.com/blog/python-to-node

- TL;DR
    - A week after launch, Skald rewrote its Django backend to Node.js/Express, arguing Python’s bolted-on async and Django’s caveats slowed LLM-heavy, concurrent I/O. Node unified their existing worker with the API, improved ergonomics, and yielded ~3x throughput; MikroORM replaced Django’s ORM. They skipped FastAPI, distrusting Python’s async ecosystem. HN debates premature optimization vs removing tech debt early, proposes Celery/channels or nginx within Python, and suggests Elixir/BEAM for first-class concurrency.

- Comment pulse
    - Premature rewrite → PostHog scales on Django; 3 days could go to customers. — counterpoint: ergonomics matter; async Python became tech debt; happier devs yields speed.
    - Use Python patterns instead → Celery/channels/WebSockets avoid HTTP blocking; FastAPI exists. — counterpoint: for quick parallelism, Celery/threads add overhead; Node’s Promise.all is trivial.
    - Try Elixir/BEAM → built-in concurrency, observability, zero-downtime. — counterpoint: smaller ecosystem, hiring risk, compile-time friction, limited LLM codegen support.

- LLM perspective
    - View: Early rewrite optimized for async ergonomics and unified services; trade Python ML ecosystem for operational simplicity around I/O concurrency.
    - Impact: Faster iteration for LLM API orchestration; lower latency under bursty parallel calls; more maintainable code without sync/async shims.
    - Watch next: Publish open benchmarks vs FastAPI/SQLAlchemy; track P95 latency and cost/core; evaluate Python ML microservice when models move in-house.
