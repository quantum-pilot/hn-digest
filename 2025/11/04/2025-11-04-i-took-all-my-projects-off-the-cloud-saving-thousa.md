# I took all my projects off the cloud, saving thousands of dollars

- Score: 207 | [HN](https://news.ycombinator.com/item?id=45816041) | Link: https://rameerez.com/send-this-article-to-your-friend-who-still-thinks-the-cloud-is-a-good-idea/

- TL;DR
  - An indie developer moved workloads from AWS to Hetzner VPS/bare metal, dropping monthly infra from ~$1,400 to <$120 while improving performance, arguing most small/medium apps don’t need managed cloud features. He blames lock‑in and marketing for 10–100x markups, says datacenters are robust, and that AI makes Linux ops tractable; Cloudflare can cover edge needs. HN highlights cloud’s convenience, compliance, burst capacity, and engineering‑time tradeoffs; many recommend using credits for MVPs, then migrating to portable, dedicated servers to rein in egress and costs.

- Comment pulse
  - Cloud conveniences → managed services/compliance enable quick assembly and burst capacity; engineering time can dwarf hardware savings — counterpoint: AWS docs/ops overhead also expensive.
  - MVP then migrate → use credits/free tiers to validate, keep architectures portable, later move off to cut egress and RI lock‑in.
  - Dedicated servers sweet spot → hourly bare‑metal/VPS deliver predictable price/performance without colocation hassles; compute improved 100x while cloud prices lag.

- LLM perspective
  - View: Evaluate TCO including engineering time, risk, and egress; steady workloads favor fixed-price VPS/dedicated over managed services.
  - Impact: Indie devs/SMBs can slash costs fast; infra teams must justify managed services with compliance, burst needs, or staffing constraints.
  - Watch next: Track portable stacks, CDN/caching adoption, fair egress pricing; publish benchmarks comparing Hetzner/Linode/DO vs AWS C6 for representative workloads.
