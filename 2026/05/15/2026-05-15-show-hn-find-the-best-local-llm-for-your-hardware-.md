# Show HN: Find the best local LLM for your hardware, ranked by benchmarks

- Score: 277 | [HN](https://news.ycombinator.com/item?id=48146369) | Link: https://github.com/Andyyyy64/whichllm

- TL;DR  
    - whichllm is a CLI tool that inspects your hardware and recommends the best local LLMs that actually fit and run well, instead of just the largest that loads. It pulls live data from HuggingFace, merges multiple benchmark sources (LiveBench, Artificial Analysis, Aider, vision evals, Chatbot Arena, Open LLM Leaderboard), and adjusts scores by recency, evidence quality, quantization, speed, and VRAM fit. It can simulate GPUs for purchase planning, auto-run models, and generate ready-to-use Python snippets.

- LLM perspective  
    - View: This turns “which model should I use?” from guesswork into a repeatable, benchmark-driven hardware-aware decision.  
    - Impact: Helpful for individual developers, small teams, and homelab users standardizing on local models without constant leaderboard-chasing.  
    - Watch next: Support for more backends, finer task profiles, and side-by-side latency/quality comparisons across full chat sessions, not just static benchmarks.
