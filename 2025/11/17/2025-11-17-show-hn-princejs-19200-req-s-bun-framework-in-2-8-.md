# Show HN: PrinceJS – 19,200 req/s Bun framework in 2.8 kB (built by a 13yo)

- Score: 109 | [HN](https://news.ycombinator.com/item?id=45957402) | Link: https://princejs.vercel.app

### TL;DR

PrinceJS is an MIT-licensed Bun web framework by a thirteen-year-old developer, offering radix routing, TypeScript and Zod validation, middleware, OpenAPI docs, sessions, streaming, uploads, cron, JSX, and deployment adapters. Its site reports about 18,000 requests per second and a roughly 5 kB compressed bundle. Commenters praise the polished documentation and readable wrapper, but caution that server bundle size matters little, benchmark rates look unusually low, missing route cases distort comparisons, and maintainability may be a stronger pitch than speed.

### Comment pulse

- Reviewers recommended isolated router modules, unit tests, standard hardware, latency disclosure, and capability-matched benchmarks.
- A source review alleged JWT accepts arbitrary tokens and rate limiting mishandles missing forwarded IPs, making current security defaults unsafe.

### LLM perspective

- View: Shipping a coherent project is impressive; security correctness must precede performance marketing.
- Impact: Early adopters risk authentication flaws unless middleware receives tests, threat modeling, and expert review.
- Watch next: JWT validation fixes, route coverage, reproducible benchmarks, multi-node cron semantics, and test expansion.
