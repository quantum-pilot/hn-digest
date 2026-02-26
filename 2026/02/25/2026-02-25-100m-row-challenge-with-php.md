# 100M-Row Challenge with PHP

- Score: 164 | [HN](https://news.ycombinator.com/item?id=47149752) | Link: https://github.com/tempestphp/100-million-row-challenge

### TL;DR
PHP community contest: parse a 7 GB CSV (100M page-visit rows) into a JSON aggregation of per-path, per-day visit counts as fast as possible. Entrants fork a repo, implement `Parser::parse()`, validate locally, then submit PRs; organizers benchmark on a modest 2‑vCPU DigitalOcean droplet with fixed extensions, JIT disabled, and no FFI. Prizes include JetBrains licenses and collectible Elephpants. HN discussion spans PHP optimization war stories, “right tool for the job” critiques, shell/sqlite alternatives, and JSON escaping quirks.

---

### Comment pulse
- PHP perf challenge is fun and educational → original 5‑day script optimized to 30 s inspired this—counterpoint: real bottleneck is system/IO, not PHP syntax tricks.  
- Some use this to advocate Go/Rust for serious data work → better tooling, stdlib, performance—counterpoint: thread drift from a language-specific community event.  
- Practitioners share baselines: naive Unix pipeline takes ~22 min, sort dominates; others nitpick JSON `\/` escaping as PHP/json_encode legacy behavior.

---

### LLM perspective
- View: This neatly tests streaming, aggregation, and memory discipline in PHP under realistic constraints, not microbenchmarks.  
- Impact: PHP devs gain concrete perf patterns; results may influence frameworks, libraries, and “PHP is slow” perceptions.  
- Watch next: Compare best PHP solutions vs Go/Rust/Unix pipelines on same dataset to separate language limits from implementation skill.
