# Experimenting with Local LLMs on macOS

- Score: 383 | [HN](https://news.ycombinator.com/item?id=45168953) | Link: https://blog.6nok.org/experimenting-with-local-llms-on-macos/

- TL;DR
    - A pragmatic macOS guide to running local LLMs: use llama.cpp or LM Studio, pick 4-bit models sized to your RAM, and accept trade-offs (GPU-bound speed, hallucinations). It covers model/runtimes (GGUF vs MLX), reasoning/vision/tool-use via MCPs, safety (data exfiltration), and practical tips (context compaction). HN debates Apple’s ANE sitting idle, realistic laptop limits, concrete local uses (private notes, automation, offline help), and whether home “AI boxes” or privacy-first cloud wins near term.

- Comment pulse
    - Hardware reality → GPU via Metal, ANE idle; 12–20B near 16GB limit; big Mac Studios can host larger models—counterpoint: cost impractical for most.
    - Practical use → Local excels at private workflows: journaling with Obsidian, on-device automation, classification/summarization, offline help; hallucinations make editing tasks risky without strict prompts and checks.
    - Trajectory → Optimists expect local to replace cloud; skeptics cite hardware gap and rely on secure/private cloud; Apple urged to expose ANE or improve Core ML.

- LLM perspective
    - View: Local models are best as controlled components: deterministic formatting, retrieval-augmented, and tool-limited; avoid open-ended generation for facts or delicate edits.
    - Impact: Developers adopt MCP sandboxes and eval harnesses; consumers try small reasoning or home servers; Apple pressured to expose/improve ANE.
    - Watch next: Track ANE/Core ML transformer support, GGUF vs MLX performance on M4, and releases of sub-20B reasoning VLMs with reliable tool-use.
