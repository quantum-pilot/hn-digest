# Qwen 3.8-Flash-Next releasing tomorrow (125B a6B)

- Score: 334 | [HN](https://news.ycombinator.com/item?id=49432317) | Link: https://modelscope.cn/models/Qwen/Qwen3.8-Flash-Next

### TL;DR

The supplied ModelScope page exposes only navigation and login text, so substantive details come from HN discussion of an imminent Qwen 3.8-Flash-Next release described as a 125B-parameter mixture-of-experts model with 6B active parameters. Commenters expect it to make 128GB Strix Halo, GB10, or Mac Studio systems more useful for local inference, but warn that memory bandwidth, large contexts, heat, and provider capacity remain constraints. Interest also extends to smaller future Qwen-family models.

### Comment pulse

- Large unified-memory machines gain a plausible workload → sparse MoE activation may make 125B local inference usable.
- Hardware capacity is not throughput → GPUs retain bandwidth advantages, while context growth can consume 128GB quickly.
- Hosted Qwen reliability remains uneven → users report flaky capacity and provider-routing complexity through OpenRouter.

### LLM perspective

- View: Active-parameter count makes the release promising, but memory movement will determine practical speed.
- Impact: Local-model users may gain capability without multi-GPU rigs, accepting slower inference and power costs.
- Watch next: Compare quantizations, context scaling, tokens per second, and provider availability after release.
