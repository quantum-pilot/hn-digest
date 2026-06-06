# Bun's experimental Rust rewrite hits 99.8% test compatibility on Linux x64 glibc

- Score: 360 | [HN](https://news.ycombinator.com/item?id=48073680) | Link: https://twitter.com/jarredsumner/status/2053047748191232310

### TL;DR
Bun’s creator used Anthropic’s Claude Mythos to spin up an experimental Rust rewrite of the JS runtime that already passes 99.8% of Bun’s Linux x64 glibc test suite, reportedly in about six days. The Bun author stresses it’s a throwaway experiment, not a committed rewrite. HN discusses Rust as an excellent but brittle target for LLM-generated code, compares similar Rust+LLM ports (TypeScript, Postgres), and debates Bun’s direction, Anthropic’s influence, and whether AI-driven rewrites improve reliability or just increase “slop.”

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Rapid Rust port via LLMs is impressive → strong test suite + existing codebase make translation an ideal AI use case; others report similar success with TS and Postgres.  
- Growing distrust of Bun → Zig-to-Rust pivot plus Anthropic acquisition seen as political/marketing, not technical — counterpoint: maintainers provided concrete technical motivations and call it an experiment.  
- Rust vs Zig and AI/compute → some expect fewer memory bugs with Rust; others argue language isn’t the root problem and compute access won’t stay an enduring moat.

---

### LLM perspective
- View: AI-assisted ports will become routine for mature projects with good tests; the real bottleneck shifts to architecture and maintainability.  
- Impact: Small teams gain leverage to attempt rewrites once reserved for big orgs, but community trust and governance decisions become more visible risks.  
- Watch next: Concrete benchmarks vs Zig Bun, `unsafe` usage audits, long-term bug rates, and transparent accounting of AI cost and process.
