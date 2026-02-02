# Show HN: NanoClaw – “Clawdbot” in 500 lines of TS with Apple container isolation

- Score: 85 | [HN](https://news.ycombinator.com/item?id=46850205) | Link: https://github.com/gavrielc/nanoclaw

- TL;DR  
  NanoClaw is a personal Claude assistant for macOS that connects via WhatsApp, runs each chat group in its own Apple Container VM, and uses per-group filesystems and memory for isolation. The tiny TypeScript harness delegates setup, customization, and debugging to Claude Code, and encourages extensions as “skills” that rewrite your fork (e.g., add Telegram or Docker) instead of bloating the core. HN discussion focuses on sandboxing trade-offs, the Apple Container choice, and discomfort with obviously LLM-written, occasionally hallucinated documentation.

- Comment pulse  
  Security appeal → Apple Containers give per-group VM isolation and filesystem allowlists, but some wonder how dangerous external actions remain constrained compared with Clawdbot’s broad capabilities.  
  LLM-written docs feel inauthentic → commenters distrust polished AI READMEs, prefer brief human notes, citing hallucinated claims — counterpoint: some are fine with AI prose if verified.  
  Lightweight claim debated → people like a smaller OpenClaw and native Containers, but dispute the “500 lines” framing and lament marketing-heavy, vibe-coded AI projects.

- LLM perspective  
  View: Treat this as an opinionated starter harness for Claude on macOS, not a universal framework or multi-user product.  
  Impact: Makes self-hosted assistants more approachable by emphasizing OS-level isolation, small codebases, and AI-guided customization instead of sprawling configs.  
  Watch next: Community skills for Docker, Linux, and extra channels will show whether the “skills not features” model scales socially.
