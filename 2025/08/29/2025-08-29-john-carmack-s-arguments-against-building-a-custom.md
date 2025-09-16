# John Carmack's arguments against building a custom XR OS at Meta

- Score: 527 | [HN](https://news.ycombinator.com/item?id=45066395) | Link: https://twitter.com/ID_AA_Carmack/status/1961172409920491849

- TL;DR
  - John Carmack argued Meta shouldn’t build a bespoke XR OS (XROS): it distracted core teams, multiplied tech stacks, delayed shipping, and wouldn’t beat commodity drivers/hardware. HN commenters largely agree, citing modern silicon complexity and the impracticality of writing drivers; propose piggybacking on Linux or LKL, focusing on performance-critical XR layers. Others romanticize an isolated “monastic” reboot of computing, but critics note stakeholder misfit and decades of wheel‑reinvention. Discussion also touches on Meta org politics, ex‑Microsoft OS hires, and HR conflicts over blunt technical pushback.
  - Content unavailable; summarizing from title/comments.

- Comment pulse
  - Custom XR OS was a distraction → multiple stacks and reorg politics slowed core XR work; some teams chased empire-building after Microsoft hires.
  - Don’t write your own OS → modern hardware/docs make drivers infeasible; use Linux drivers or LKL to ship sooner — counterpoint: vendors should document; Intel NICs prove.
  - Isolationist ‘monastic order’ sounds visionary → but without stakeholders you miss needs; decades risk reinventing wheels and incompatibility with real apps.

- LLM perspective
  - View: Make XR a thin, performance-obsessed platform: strict HAL, user‑mode drivers, and ruthless feature cuts to hit latency/thermals.
  - Impact: Reduces driver churn, isolates vendor code, accelerates updates, and improves app portability via OpenXR-first design.
  - Watch next: Public latency/power benchmarks, HAL/driver SDKs for partners, and signs Meta deepens co-design with Qualcomm/Broadcom.
