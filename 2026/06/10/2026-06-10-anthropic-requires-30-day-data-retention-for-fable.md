# Anthropic requires 30 day data retention for Fable and Mythos

- Score: 605 | [HN](https://news.ycombinator.com/item?id=48464258) | Link: https://support.claude.com/en/articles/15425996-data-retention-practices-for-mythos-class-models

- TL;DR  
  Anthropic will require 30‑day logging of prompts and outputs for its highest‑risk “Mythos‑class” models (e.g., Fable/Mythos 5, currently suspended), including for enterprise customers that previously had zero‑data‑retention. They say short‑term storage is needed to detect cross‑request attacks and won’t be used for training. HN discussion centers on broken ZDR expectations, harder B2B trust/comms, IP and code‑leak risks with agentic tools, and aggressive safety filters that frequently downgrade or block work.

- Comment pulse  
  - 30‑day retention for ZDR orgs → erodes prior “no logs” promises; some expect client loss and suspect government/intel access — counterpoint: terms still ban training.  
  - Agentic coding tools upload repos and secrets → worries about IP theft and key leaks; others claim most startup code isn’t unique enough to matter.  
  - Over‑sensitive safety filters on Fable/Mythos → legitimate bio, medical, and even generic PyTorch work gets blocked or downgraded, making high‑end models unusable for some workflows.

- LLM perspective  
  - View: Treating top‑tier models as “covered” with mandatory logs mirrors high‑risk system regulation; more vendors will copy this segmentation.  
  - Impact: Security‑sensitive enterprises may cap usage at weaker ZDR models or migrate to self‑hosted/open‑weight systems for critical code and data.  
  - Watch next: If clouds mirror these models with in‑account logs, and whether regulators scrutinize broad “safety” justifications for retaining data.
