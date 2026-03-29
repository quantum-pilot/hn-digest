# Paper Tape Is All You Need – Training a Transformer on a 1976 Minicomputer

- Score: 131 | [HN](https://news.ycombinator.com/item?id=47518568) | Link: https://github.com/dbrll/ATTN-11

## TL;DR

A hobbyist implements a genuine transformer—1 layer, 1 attention head, 1,216 parameters—in PDP‑11 assembly, training it to reverse 8‑digit sequences entirely on 1970s‑class hardware. Using a hand‑rolled fixed‑point math stack, lookup‑table softmax and cross‑entropy, and carefully tuned per‑layer learning rates, the model fits in 32KB and reaches 100% accuracy in 5.5 minutes. Hacker News readers highlight how capable old machines already were, arguing that ideas and algorithms, more than raw compute, delayed such experiments.

---

## Comment pulse

- Author hangs out in thread → answers questions on PDP‑11, fixed‑point design; sparks others to try similar ML/assembly projects on vintage or homebrew CPUs.  
- “5.5 minutes on a PDP‑11” → commenters note 80s Crays could have trained multi‑million‑parameter LMs; hardware wasn’t the bottleneck—counterpoint: data, tooling, and theory still mattered.  
- Readers see this as perspective reset → modern ML could have run in the 70s at small scale; inspires “minimal interface” AI ideas, even tape‑only agents.

---

## LLM perspective

- View: This is a concrete proof that core transformer mechanics survive under extreme memory, precision, and instruction‑set constraints.  
- Impact: Encourages serious exploration of ultra‑small, fixed‑point, table‑driven models for embedded and retrocomputing contexts.  
- Watch next: Benchmarks of similar architectures on 8‑bit or RISC‑V MCUs; open libraries of fixed‑point kernels and LUT designs.
