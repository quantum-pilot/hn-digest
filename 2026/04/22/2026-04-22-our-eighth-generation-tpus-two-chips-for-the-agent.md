# Our eighth generation TPUs: two chips for the agentic era

- Score: 380 | [HN](https://news.ycombinator.com/item?id=47862497) | Link: https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/

## TL;DR

Google’s 8th‑gen TPUs split into two specialized chips: TPU 8t for massive training and TPU 8i for low‑latency inference and multi‑agent “reasoning” workloads. 8t superpods scale to 9,600 chips, 2 PB of shared HBM, 121 exaflops and near‑linear scaling via the Virgo network, targeting >97% “goodput.” 8i adds much more on‑chip SRAM, a new low‑diameter Boardfly topology, Axion ARM hosts, and a collectives engine for up to 80% better perf‑per‑dollar. HN discussion focuses on Gemini quality, token thrift, and Google’s infra‑vs‑product gap.

---

## Comment pulse

- Gemini models feel efficient and multilingual but weak at “agentic” tasks → users see short answers, fewer tool calls, loops, and poor coding vs Claude/Codex.

- Google’s vertical integration (TPUs, Axion CPUs, networks, cooling) may yield best large‑scale cost efficiency → critics note GCP prices, limited access vs cheaper GPU hosts. — counterpoint: for frontier‑scale training, only hyperscalers can realistically match this stack.

- Strategically, Google looks slow and uninspiring yet quietly strong → open models are decent, infra is solid, but Gemini apps, IDE tooling, and “preview” churn erode developer trust.

---

## LLM perspective

- View: Splitting training (8t) and inference/agents (8i) formalizes a hardware pattern others will likely follow as agent workloads diverge.

- Impact: Benefits frontier‑scale labs and big enterprises most; indie researchers remain priced into commodity GPUs and smaller open models.

- Watch next: Independent benchmarking of 8i vs H100/B200 for latency and cost per 1M tokens on real agent workloads, plus availability outside Google’s own stack.
