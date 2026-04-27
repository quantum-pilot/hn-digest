# SWE-bench Verified no longer measures frontier coding capabilities

- Score: 231 | [HN](https://news.ycombinator.com/item?id=47910388) | Link: https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/

### TL;DR
OpenAI argues its curated SWE-bench Verified coding benchmark has broken down: many “hard” tasks have buggy or misaligned tests, while leading models clearly memorized problems and gold patches from training data. That means rising scores mostly track data leakage, not genuine software-engineering skill, so OpenAI will stop reporting them and prefers SWE-bench Pro and private, human-scored evals. HN discussion ranges from SWE-bench authors’ defense and new benchmarks to broader doubts that any public benchmark can resist gaming or contamination.

---

### Comment pulse
- SWE-bench creators say Verified’s near-saturation is expected and new suites (Multilingual, Multimodal, CodeClash, AlgoTune, SWE-rebench) are coming—but critics note flawed tests weaken comparisons.  
- Several argue any public benchmark will enter training data; with strong marketing incentives, they favor private, rotating, or dynamic evaluations over static leaderboards.  
- Others draw parallels to SPEC, database, and ELT-Bench “benchmarketing” wars, noting structural bias, git-history leaks, and low-quality patches mean we “get the benchmarks we deserve.”

---

### LLM perspective
- View: Treat coding benchmarks as short-lived hints, not ground truth; emphasize longitudinal user studies and qualitative developer feedback instead.  
- Impact: Buyers, regulators, and management should avoid over-indexing on single scores when choosing models or claiming “agentic coding” breakthroughs.  
- Watch next: Shared third-party eval consortia with confidential tasks, contamination checks, and messy long-context repo challenges closer to real-world engineering.
