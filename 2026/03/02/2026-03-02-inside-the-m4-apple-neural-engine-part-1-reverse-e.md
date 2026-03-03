# Inside the M4 Apple Neural Engine, Part 1: Reverse Engineering

- Score: 247 | [HN](https://news.ycombinator.com/item?id=47208573) | Link: https://maderix.substack.com/p/inside-the-m4-apple-neural-engine

TL;DR
- Reverse-engineering Apple’s M4 Neural Engine, the author (with Claude as coding/analysis partner) bypasses CoreML to talk directly to the ANE via private `_ANEClient` and `_ANEInMemoryModel` APIs. They map the full stack, decode the MIL→E5 compilation pipeline, show that ANE runs parameterized graph “microcode” rather than classic instructions, and expose deep queues, DVFS controls, and IOSurface-based zero-copy I/O. Discussion focuses on practical acceleration for open-source ML, Apple’s marketing TOPS claims, prior Asahi work, and whether to trust LLM-assisted systems research.

Comment pulse
- ANE in open-source stacks is rare → NPUs are vendor-specific; this work may enable targeted ANE support rather than generic numpy/sklearn speedups.
- Apple’s “38 TOPS” is challenged → measurements show lower real throughput; using marketing-style INT8×2 accounting is called misleading.
- Some see LLM co-authorship as unreliable → others note humans already generate bad or irreproducible research; all reverse engineering demands independent replication.

LLM perspective
- View: This unlocks ANE as a first-class accelerator, not just a hidden CoreML backend.
- Impact: Local ML frameworks, Asahi Linux, and performance hackers gain a documented, scriptable path to ANE.
- Watch next: Independent reproduction of APIs/benchmarks, open-source ANE kernels, and integration into projects like llama.cpp and PyTorch backends.
