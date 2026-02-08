# Software factories and the agentic moment

- Score: 123 | [HN](https://news.ycombinator.com/item?id=46924426) | Link: https://factory.strongdm.ai/

## TL;DR
StrongDM describes a “software factory” where LLM agents, not humans, write and review code from specs and rich, end‑to‑end “scenarios.” Quality is measured via probabilistic “satisfaction” across scenario runs inside a Digital Twin Universe of cloned SaaS APIs, enabling huge volumes of offline validation. They argue teams should aggressively spend on tokens (≈$1k/day/engineer) and abandon Software‑1.0 assumptions. HN readers like the compounding-correctness and fake‑service testing ideas but question the costs, hype, and unresolved validation problem.

## Comment pulse
- Token spend as productivity metric is divisive → some see $1k/day as absurd marketing, others equate it to replacing a junior engineer’s cost.  
- Validation is bottleneck → generation is easy; trust still needs human experts, multi-agent checks, traffic replay, or formal methods to compare intent vs behavior.  
- Hype vs substance → critics mock repackaged mocks and scant code; others say LLMs make many API fakes trivial—counterpoint: no quality or defect metrics yet.

## LLM perspective
- View: Treat “no human-written code” as a forcing function to redesign specs, testing, and observability, not as dogma.  
- Impact: If factories work, junior dev roles shrink while scenario designers, validators, and DTU maintainers become core high-leverage engineering specializations.  
- Watch next: Benchmarks comparing factory-built vs human-built systems on defects, latency, and throughput at fixed spend on compute plus labor.
