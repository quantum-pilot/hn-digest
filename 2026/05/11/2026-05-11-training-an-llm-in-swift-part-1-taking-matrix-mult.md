# Training an LLM in Swift, Part 1: Taking matrix mult from Gflop/s to Tflop/s

- Score: 209 | [HN](https://news.ycombinator.com/item?id=48085685) | Link: https://www.cocoawithlove.com/blog/matrix-multiplications-swift.html

### TL;DR
Gallagher rewrites Karpathy’s `llm.c` GPT‑2-style trainer in Swift, then pushes handwritten matrix multiplies from ~2.8 Gflop/s (painfully slow) to ~1.1 Tflop/s on an M3 Max. He systematically removes Swift `Array` CoW overhead with `MutableSpan`, enables FMA via Swift Numerics’ `Relaxed` math, uses loop tiling and `InlineArray`, adds multithreading with `DispatchQueue.concurrentPerform`, then taps undocumented AMX instructions and finally Metal GPU kernels (with tiling). The goal is educational: show how real ML libraries squeeze performance, not replace them. HN focuses on the rarity of such deep Swift-performance writeups, FMA correctness flags, and GPU vs CPU tuning complexity.

---

### Comment pulse
- Swift performance guide → Rare, high-quality deep dive into Swift optimization; nostalgia for Gallagher’s earlier Cocoa/Swift posts as canonical explanations.  
- FMA vs fast-math → Use `-ffp-contract=fast` for FMA without `-ffast-math`’s broader, risky rewrites—counterpoint: compilers still overvalue legacy bitwise reproducibility.  
- GPU performance gap → Peak FLOPs overstate real throughput; tuned kernels and ecosystems (e.g., CUDA) matter—counterpoint: some argue GPU tuning isn’t much harder than CPUs.

---

### LLM perspective
- View: This is a template for methodical performance work: profile, change one thing, validate, repeat across the whole stack.  
- Impact: Swift/Apple‑silicon devs gain a concrete roadmap for bridging from naive code to near-library-level ML performance.  
- Watch next: Compare against Accelerate/BNNS/MPSGraph/CoreML; add mixed precision, batching, and larger models to stress real-world training throughput.
