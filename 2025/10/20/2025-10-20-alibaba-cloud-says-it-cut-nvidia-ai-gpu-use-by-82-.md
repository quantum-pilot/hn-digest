# Alibaba Cloud says it cut Nvidia AI GPU use by 82% with new pooling system

- Score: 322 | [HN](https://news.ycombinator.com/item?id=45643163) | Link: https://www.tomshardware.com/tech-industry/semiconductors/alibaba-says-new-pooling-system-cut-nvidia-gpu-use-by-82-percent

### TL;DR

Alibaba Cloud says its Aegaeon inference scheduler reduced GPUs for a production beta from 1,192 to 213 while serving dozens of intermittently requested models. Rather than reserving an accelerator per model, Aegaeon packs multiple models together and reallocates compute at token granularity, reporting 1.5-to-ninefold goodput gains over ServerlessLLM and MuxServe. The headline's 82% reduction applies to the tested pool, not necessarily Alibaba's entire 30,000-GPU fleet, and the article says transferability beyond Alibaba's integrated network and serving stack remains unproven.

### Comment pulse

- Readers emphasized that the large savings targeted “cold” models receiving a small share of marketplace requests.
- One extrapolation argued that fleet-wide savings could be far smaller than the headline percentage.
- Discussion connected hardware constraints with incentives for scheduling and utilization research.

### LLM perspective

- View: Aegaeon's result is chiefly an utilization win for sparse multi-model demand, not equivalent hardware acceleration.
- Impact: Better pooling could defer accelerator purchases and make long-tail model catalogs economically viable.
- Watch next: Reproduction across networks, model mixes, latency objectives, and non-Alibaba serving stacks.
