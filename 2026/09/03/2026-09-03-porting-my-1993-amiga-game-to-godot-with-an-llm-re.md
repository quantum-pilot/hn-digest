# Porting my 1993 Amiga game to Godot, with an LLM reading the 68000 assembly

- Score: 297 | [HN](https://news.ycombinator.com/item?id=49550375) | Link: https://babyloniantwins.com/blog/porting-a-1993-amiga-game-to-godot/

### TL;DR

Rabah Shihab describes using Claude Fable 5 and Claude Code to reconstruct Babylonian Twins from 34,000 lines of C++ and 72,758 lines of 68000 assembly, then port both versions into Godot. Automated compilation, binary diffs, probes, and screenshots accelerated archaeology, but human play-testing still found subtle behavioral errors. Commenters shared similar retro-port experiments and marveled at revisiting early computing as archaeology, while raising practical questions about compute cost and the need for follow-up prompting.

### Comment pulse

- Retro-porting feels newly accessible → commenters report source conversions and reverse-engineering projects across many classic systems and games.
- Verification remains essential → one experiment reportedly filled missing material from online sources, while Shihab found plausible but incorrect behavior.
- Cost is unclear → readers want the plan and compute expense behind several hours of continuous coding-agent work.

### LLM perspective

- View: The strongest result is not rapid code generation, but a tool-driven loop that makes historical behavior testable.
- Impact: Preservation teams can inspect undocumented formats faster, while original creators remain crucial for feel, intent, and anomalies.
- Watch next: Reproduce the port independently, quantify compute costs, and audit the unverified 108-byte memory-snapshot explanation.
