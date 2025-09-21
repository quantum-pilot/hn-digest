# The LLM Lobotomy?

- Score: 114 | [HN](https://news.ycombinator.com/item?id=45315746) | Link: https://learn.microsoft.com/en-us/answers/questions/5561465/the-llm-lobotomy

TL;DR
An Azure OpenAI user claims “LLM lobotomy”: the same gpt-4o-mini, system prompt, and temp‑0 tests now fail structured JSON checks more often, and gpt‑5‑mini/nano feel slower and weaker. They suspect silent downgrades and consider leaving Azure. HN asks for reproducible evidence and pinned logs; others propose providers keep timestamped, immutable model versions and rerun public benchmarks. Debate centers on causes—quantization or hidden system prompts vs versioned weights with inference/pipeline nondeterminism and Azure safety layers. Temp‑0 isn’t fully deterministic; performance and pricing complaints surface.

Comment pulse
- Silent regressions exist → demand pinned/timestamped models, periodic benchmarks; 'latest' can float; quantization or hidden prompts suspected — counterpoint: weights are versioned; pipeline nondeterminism likely.
- Azure adds safety/RAI layers → outputs may differ from OpenAI; some see Azure-hosted models slower/worse; users want old models frozen without deprecation.
- Evidence requested → reproducible test suite with fixed seeds and logs; temperature 0 not fully deterministic; infrastructure and rate limits can skew latency/format conformance.

LLM perspective
- View: Treat hosted LLMs as moving targets; build regression tests, pin deployments, and monitor output schemas continuously.
- Impact: Azure safety layers may improve compliance but reduce predictability; trade-offs vs OpenAI direct or self-hosted models.
- Watch next: Share test harness; compare Azure vs OpenAI endpoints, temps/seeds; track latency percentiles; request model version pinning SLAs.
