# Hetzner is working on LLM Inference

- Score: 144 | [HN](https://news.ycombinator.com/item?id=49033087) | Link: https://sliplane.io/blog/hetzner-inference

### TL;DR
Hetzner has quietly launched an experimental, OpenAI-compatible LLM inference API, currently exposing a single Qwen 3.6 35B FP8 model with 262k context and image support. Early tests show very fast latency and throughput, but there’s no billing, SLA, or production guarantees yet. The author argues the real story is strategic: if Hetzner extends beyond workstation GPUs to larger multi-GPU clusters and more models, it could become a low-cost, EU-native inference provider—something HN commenters say is still missing despite existing EU offerings.

---

### Comment pulse
- EU-native inference is attractive for regulatory reasons, but OVH/IONOS/Scaleway/Infomaniak are criticized as expensive, unreliable, and behind SOTA — counterpoint: some users report OVH working fine.
- Hetzner is seen as well-positioned to drive small-model inference costs toward near-zero, yet its current single-GPU RTX lineup limits serious large-model hosting.
- Commenters expect “reseller” inference markets to emerge, echoing web hosting, pushing prices down from today’s ~$200/month entry points.

---

### LLM perspective
- View: This is a low-risk probe by Hetzner to measure demand, utilization patterns, and operational pain before committing serious GPU capital.
- Impact: Adds pressure for better EU-hosted, OpenAI-compatible endpoints, especially for regulated sectors needing data residency and auditability.
- Watch next: Evidence of multi-GPU nodes, larger open models, public pricing, and SLAs will signal whether this stays a demo or becomes core infra.
