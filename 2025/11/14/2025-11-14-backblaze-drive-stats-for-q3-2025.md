# Backblaze Drive Stats for Q3 2025

- Score: 158 | [HN](https://news.ycombinator.com/item?id=45926383) | Link: https://www.backblaze.com/blog/backblaze-drive-stats-for-q3-2025/

- TL;DR
  - Backblaze’s Q3 2025 Drive Stats tracked 328,348 data drives: quarterly AFR rose to 1.55% (Q2: 1.36%) while lifetime AFR stayed near 1.31%. Quartile outlier analysis flagged three models above 5.88% AFR, including Toshiba’s 16TB at 16.95%—explained by firmware maintenance that temporarily marked drives as “failed,” not mechanical issues. Aging, small-population Seagate 10TB/14TB models also spiked. A new 24TB Toshiba entered the fleet; four models posted zero failures. HN debates actionability, applauds transparency, and suggests per-IO metrics and diversified buying over chasing “best” SKUs.

- Comment pulse
  - Backblaze patterns differ from typical users → per-byte read/write AFR would be more comparable — counterpoint: still aids fleet planning and validates local anomaly spikes.
  - Chasing low-AFR SKUs is impractical → supply vanishes and batches vary; diversify across vendors to reduce correlated failures; vetted used models can outperform random new.
  - Open datasets build durable goodwill → engineers recommend vendors they trust; some worry cost-cutting or financial turbulence could curtail reports and erode advantage.

- LLM perspective
  - View: Backblaze’s failure definition is operational; quarter-bound windows let maintenance events masquerade as failures, skewing short-term AFR.
  - Impact: Ops should weight rates by drive-days and IO intensity; prioritize lifetime trends and confidence intervals over quarterly spikes.
  - Watch next: Track per-GB AFR, firmware rollout audit trails, and HDD supply shifts from hyperscaler demand; compare SAS vs SATA error isolation.
