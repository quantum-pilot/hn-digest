# Kimi K3 Is Competitive with Fable; Kimi K3 and Fable Is SoTA

- Score: 167 | [HN](https://news.ycombinator.com/item?id=48999291) | Link: https://fireworks.ai/blog/kimik3-fable

## TL;DR
Fireworks benchmarks open-weight Kimi K3 against closed Fable 5 on ~1,030 “agentic” tasks (SWE, terminal, algorithmic, multi-language, legal). Raw accuracy is nearly tied, but K3 is far cheaper, especially on long terminal workflows. Using oracle routing—always picking the cheapest correct model after running both—yields 93% task success and 1.5–50× lower cost than Fable alone, with K3 handling 72–96% of traffic. HN likes cheap Chinese/open models and routing ideas but notes the oracle router is only a theoretical upper bound.

---

## Comment pulse
- Chinese/open models are attractive → DeepSeek and Kimi praised for speed, coding help, and being self-hostable; caching plus cheap infra can make inference “almost free”.
- Oracle routing is an upper bound → Fireworks runs both models then picks cheapest correct; real routers must predict—counterpoint: still shows building workload-specific routers is valuable.
- Openness vs safety → K3 seen as cheaper, less overcautious than US labs; debate whether releasing weights is “open source” and how it aids even closed providers.

---

## LLM perspective
- View: Multi-model routing plus a strong open default looks like the emerging pattern; single-model “SoTA” stacks will increasingly feel inefficient.
- Impact: Teams will need logging, labeling, and monitoring focused on routing decisions, not just per-model benchmarking or prompt engineering.
- Watch next: Standardized router benchmarks, vendor-native routing APIs, and open-source router frameworks trained on real production workloads.
