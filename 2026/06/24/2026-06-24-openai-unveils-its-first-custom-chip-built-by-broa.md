# OpenAI unveils its first custom chip, built by Broadcom

- Score: 464 | [HN](https://news.ycombinator.com/item?id=48663324) | Link: https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/

### TL;DR

OpenAI introduced Jalapeño, its first custom inference processor, co-developed with Broadcom and still under test. The company claims substantially better performance per watt than current alternatives, emphasizing low-cost real-time coding workloads and vertical optimization across chips, kernels, memory, networking, scheduling, models, and products. Training is still expected to rely on Nvidia hardware, but cheaper recurring inference could improve economics and reduce dependency. HN found the strategy credible yet challenged vague claims about nine-month development, AI-assisted design, and efficiency, asking for milestones, benchmarks, deployment timelines, and manufacturing details.

### Comment pulse

- AI-assisted design lacks falsifiable detail → commenters distinguished routine HDL and verification help from genuinely novel chip optimization.
- Broadcom may supply more than design expertise → commenters pointed to reusable accelerator IP and possible foundry or memory allocation advantages.
- Inference specialization targets the larger recurring bill → supporters expect long-term efficiency gains — counterpoint: fast model and Nvidia cycles could obsolete custom silicon.

### LLM perspective

- **View:** Owning the workload makes specialization rational, but proprietary claims are meaningful only against shipping competitors at deployment time.
- **Impact:** Successful inference silicon could lower token costs and shift bargaining power from GPU vendors toward vertically integrated model providers.
- **Watch next:** Publish process node, memory system, interconnect, latency, throughput, watts, supported models, software stack, and rack-scale availability.
