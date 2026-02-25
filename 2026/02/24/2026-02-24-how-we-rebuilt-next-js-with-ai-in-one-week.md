# How we rebuilt Next.js with AI in one week

- Score: 301 | [HN](https://news.ycombinator.com/item?id=47142156) | Link: https://blog.cloudflare.com/vinext/

- TL;DR  
Cloudflare’s vinext is a Vite-based, mostly drop-in replacement for Next.js that targets Cloudflare Workers, claiming 1.6–4.4x faster builds and ~57% smaller client bundles. It omits static pre-rendering for now but adds traffic-aware pre-rendering that uses Cloudflare analytics to prebuild only popular pages, plus pluggable KV-based ISR caching. Nearly all code was authored by AI in a week, guided by tests and human oversight. HN reactions mix enthusiasm for escaping Next.js’s performance/deployment pain with worry about cloning incentives and code parity.

- Comment pulse  
  - Developers frustrated by slow, brittle Next.js apps and Turbopack praise Vite’s speed and welcome vinext as a way to keep Next APIs without Vercel lock-in.  
  - AI-built vinext using Next’s docs and tests alarms some, who predict fewer published test suites—counterpoint: others note complex systems were always reverse-engineerable, AI accelerates copying.  
  - Commenters call this a landmark AI demo, arguing code is mere tooling and jobs must adapt, while skeptics question Cloudflare hype, edge-case coverage and maintainability.

- LLM perspective  
  - View: AI plus strong specs and tests enables “API-compatible reimplementations” that unbundle platforms like Next.js from proprietary toolchains and hosting.  
  - Impact: framework moats shrink; hosting providers can clone DX on infra, forcing incumbents to compete on performance, integrations and ecosystem.  
  - Watch next: more AI-generated framework forks, pressure for private tests, and comparisons of vinext behavior, reliability and cost against Next.js.
