# The local LLM ecosystem doesn’t need Ollama

- Score: 596 | [HN](https://news.ycombinator.com/item?id=47788385) | Link: https://sleepingrobots.com/dreams/stop-using-ollama/

- TL;DR
    - The piece argues Ollama rode llama.cpp’s work to popularity, then obscured attribution, introduced a slower, buggier forked backend, misnamed distilled DeepSeek‑R1 models, and added lock‑in via Modelfiles, hashed storage, and a curated registry. A later pivot to cloud models and a token‑leak CVE further undercut its “local, private” image. Commenters largely corroborate the history, debate whether Ollama’s UX wins justify its behavior, and highlight direct llama.cpp stacks and GUIs as better long‑term options.

- Comment pulse
    - Ollama’s UX solved “just run a model” → trivial install and pulls; others felt llama.cpp GUIs now match this. — counterpoint: convenience ≠ ethics.
    - Timeline resonates with FOSS‑minded readers → confirms years of weak attribution, regressions, misleading DeepSeek naming; motivates trying llama.cpp, LM Studio, llamafile, etc.
    - MIT license meaning disputed → some see only legal minimum; others expect moral reciprocity, yet note Gerganov chose MIT and mainly requested proper credit.

- LLM perspective
    - View: Treat Ollama as a convenience layer with liabilities; serious local deployments should standardize on llama.cpp or equivalent engines.
    - Impact: Tooling choices shape privacy, performance, portability; teams risk regressions and lock‑in when delegating everything to a single VC‑backed wrapper.
    - Watch next: Maturity of llama.cpp router/web UI, llamafile, LM Studio, Jan; clearer benchmarks and security reviews for cloud‑connected ‘local’ runtimes.
