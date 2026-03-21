# MacBook M5 Pro and Qwen3.5 = Local AI Security System

- Score: 152 | [HN](https://news.ycombinator.com/item?id=47457107) | Link: https://www.sharpai.org/benchmark/

## TL;DR

Aegis’s HomeSec-Bench evaluates LLMs on 96 home-security–specific tasks (tool use, event deduplication, triage, prompt-injection resistance, etc.). On a MacBook Pro M5, Qwen3.5-9B (quantized) achieves 93.8%—close to OpenAI’s GPT-5.4 cloud models—at ~25 tok/s and sub‑second first-token latency, all fully local with no API costs or data exfiltration. Hacker News discussion is split between excitement about private, household “AI appliances” and skepticism about benchmark difficulty, marketing spin, hardware requirements, and the real robustness of the security and injection tests.

---

## Comment pulse

- Vision: a dedicated, long-lived “family AI server” owning all data and home context → feels like the new household appliance — counterpoint: rapid hardware progress makes decades-long bets dubious.

- Benchmark skepticism: tasks seem easy, focused on Qwen; many workloads could run faster/cheaper on smaller or specialized models, even older laptops or phones.

- Cost and rigor: some claim $2.5k+ entry; others show 9B quantized models running fine on ~$500 machines; prompt-injection tests and marketing tone seen as weak spots.

---

## LLM perspective

- View: Domain-specific, end-to-end benchmarks for agents (not chat) are valuable, but must clearly disclose task difficulty and coverage.

- Impact: Strengthens the case for local-first security and automation products on consumer hardware, plus careful multi-model orchestration.

- Watch next: Independent reproductions, expanded threat-model tests (prompt injection, MITM), and standardized energy/thermal measurements for always-on local inference.
