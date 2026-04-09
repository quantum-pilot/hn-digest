# MegaTrain: Full Precision Training of 100B+ Parameter LLMs on a Single GPU

- Score: 248 | [HN](https://news.ycombinator.com/item?id=47689174) | Link: https://arxiv.org/abs/2604.05091

### TL;DR
MegaTrain shows how to train 100B+ parameter LLMs in full precision on a single GPU by parking model weights and optimizer states in large CPU RAM and streaming them layer‑by‑layer to the GPU. A double‑buffered pipeline and stateless layer templates keep the GPU saturated while minimizing device memory. It outperforms DeepSpeed ZeRO‑3 with CPU offload on some setups. HN readers are excited about bigger “single‑GPU” models but highlight the need for H200‑class hardware, question novelty, and debate real practicality.

### Comment pulse
- Hobbyists hope CPU‑offloading ideas let 8–10 GB GPUs train larger, specialized models → could personalize tools or business agents locally.  
- Skeptics say similar schemes already exist and remain slow → limited real‑world value; other tricks like Muon, quantization may outperform.  
- Critique of “single GPU” framing → H200 plus 1.5 TB RAM is expensive, though still cheaper and simpler than 128‑GPU clusters — counterpoint: rentable.

### LLM perspective
- View: Makes ultra‑large, full‑precision experiments feasible for single‑node setups, but not for typical consumer PCs.  
- Impact: Benefits labs and enterprises exploring huge contexts or prototypes without allocating multi‑GPU clusters.  
- Watch next: Open tooling, support for commodity GPUs, and comparisons versus multi‑GPU mixed‑precision training on cost and wall‑clock time.
