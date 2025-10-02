# Building the heap: racking 30 petabytes of hard drives for pretraining

- Score: 232 | [HN](https://news.ycombinator.com/item?id=45438496) | Link: https://si.inc/posts/the-heap/

- TL;DR
  - Standard Intelligence built a 30 PB on‑prem “heap” for video pretraining, optimizing for cost and bandwidth over durability. With 2,400 used HDDs in NetApp JBODs, 10 cheap head nodes, and a tiny Rust/nginx/SQLite stack, they saturate ~100 Gbps and spend ~$29.5k/month all‑in (incl. depreciation), versus ~$270k on Cloudflare R2 and $1.13M on AWS S3 with egress. Key lessons: radical simplicity, nearby colo, avoid daisy‑chaining, plan networking/IPMI. HN debates cloud convenience vs atrophied on‑prem skills and notes private‑pricing counterpoints.

- Comment pulse
  - Cloud convenience eroded on‑prem skills → DIY re-learns muscle, cuts costs at petabyte scale — counterpoint: private S3 deals exist; compare against negotiated rates.
  - Containers curb “pets” → Docker/K8s keep racked servers cattle-like; easier redeployments than old VMs.
  - Colocation negotiation limited → Broad outreach; prices matched quotes; only terms and one-time fees moved.

- LLM perspective
  - View: Use low-durability, high-throughput storage for ML pretraining; simple bespoke software over complex distributed stacks.
  - Impact: Enables non-hyperscalers to amass huge video datasets; more budget goes to compute.
  - Watch next: Quantify loss/corruption impact on model quality; share BOM/scripts; test denser 90-bay builds and 400G backbones.
