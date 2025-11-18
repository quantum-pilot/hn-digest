# Show HN: PrinceJS – 19,200 req/s Bun framework in 2.8 kB (built by a 13yo)

- Score: 109 | [HN](https://news.ycombinator.com/item?id=45957402) | Link: https://princejs.vercel.app

- TL;DR
  - PrinceJS is a 2.8 kB Bun web framework by a 13‑year‑old, claiming ~19k req/s with an Express‑like API. HN praises the initiative and documentation, but asks for rigorous, reproducible benchmarking, clearer tradeoffs behind the speed claim, stronger modular design and tests, and safer defaults. Commenters argue some included features and metrics aren’t relevant server‑side, and suggest focusing the project around developer experience while tightening correctness, security, and methodology. Many still see strong portfolio value.
  - Content unavailable; summarizing from title/comments.

- Comment pulse
  - Benchmark rigor → use oha, report latency, and explain odd Hono/Elysia results; Bun often reaches 80–100k req/s.
  - Implementation tradeoffs/scope → defineProperty slower; eager parsing; wildcards missing; cron doesn't fit multi-node; gzipped size irrelevant; modularize + test — counterpoint: DX may be the draw.
  - Security/defaults/docs → JWT not verified; x-forwarded-for can cause shared rate limits; baked-in email provider reduces flexibility; docs’ animations distract; explain “why fast” and tradeoffs.

- LLM perspective
  - View: Position as DX‑first, batteries‑optional bun.serve wrapper; make performance a constraint, not the headline.
  - Impact: With tests/security, good for hobby APIs, learning, and reproducible benchmarking tutorials; elevates a young maintainer’s portfolio.
  - Watch next: Publish oha/k6 with latency histograms and VM spec; benchmark router vs Elysia precompile; microbench defineProperty; adopt standard‑schema; document trusted‑proxy rate‑limiting.
