# Attention at Constant Cost per Token via Symmetry-Aware Taylor Approximation

- Score: 144 | [HN](https://news.ycombinator.com/item?id=46886265) | Link: https://arxiv.org/abs/2602.00294

- TL;DR  
    - Paper recasts transformer self‑attention as a polynomial kernel using a symmetry‑aware Taylor expansion, then exploits tensor symmetries to maintain only a fixed‑size recurrent state instead of an n‑token KV cache. This yields linear‑in‑sequence, constant‑per‑token compute and memory, while matching standard attention to roughly float16 precision with 4 Taylor terms in experiments. HN discussion praises the math but questions theoretical limits, sharp “needle in haystack” behavior, and the lack of downstream benchmarks on real models.

- Comment pulse  
    - Attention must be fundamentally quadratic → prior work and lower bounds suggest exact, lossless attention can’t be sub‑n²; this seems another approximate, potentially paper‑mill variant.  
    - Method matches linear‑attention trick → rewrite softmax(QK)V as Q'(KV), so only aggregated KV features are stored; complexity linear — counterpoint: aggregation discards per‑token information.  
    - Approximation may blur sharp attention → Taylor truncation could weaken needle‑in‑haystack focus and long‑range recall; commenters propose testing on pretrained and newly trained models.

- LLM perspective  
    - View: Treat this as a promising, math‑driven linear‑attention variant, not yet a production‑ready replacement for full quadratic attention.  
    - Impact: If validated, could cut KV‑cache memory, extend contexts, and reduce inference costs for streaming and on‑device models.  
    - Watch next: Run on Llama‑class models, map accuracy vs Taylor order, and test hybrids with sparse attention for needle‑in‑haystack tasks.
