# Show HN: I invented a new generative model and got accepted to ICLR

- Score: 488 | [HN](https://news.ycombinator.com/item?id=45536694) | Link: https://discrete-distribution-networks.github.io/

- TL;DR
  - Discrete Distribution Networks (DDN) is a new generative model accepted to ICLR 2025. It produces K discrete candidates per layer, picks the closest to the target during training (Split-and-Prune), and composes layers to exponentially expand sample space. Reported perks: zero-shot conditional generation with black-box guidance (e.g., CLIP), simple 1D latent tree, and single-pass inference. HN readers applaud the novelty and single-author acceptance, debate the MoE-like interpretation and compute tradeoffs, question a philosophical “Taiji” analogy, and probe for potential cherry-picking or leakage.

- Comment pulse
  - Open reviews add transparency → authors can cite reviewer interpretations; readers see accept/reject debates.
  - Architecture discards K−1 candidates per layer → perceived inefficiency, MoE comparison. — counterpoint: Inference preselects one index; no extra compute; not MoE/diffusion.
  - Impressive visual matches raise eyebrows → could be dataset bias, cherry-picking, or leakage; commenters ask for evidence ruling these out.

- LLM perspective
  - View: A principled multi-branch generator with guided selection; compelling for constraint-driven tasks and black-box conditioning.
  - Impact: Could replace diffusion in control/vision pipelines needing multi-hypothesis, low latency generation; simplifies conditioning and sampling on edge hardware.
  - Watch next: ImageNet-scale results, ablations vs. diffusion/GANs, compute profiles (train/infer), robustness to K,L choices, and rigorous leakage checks.
