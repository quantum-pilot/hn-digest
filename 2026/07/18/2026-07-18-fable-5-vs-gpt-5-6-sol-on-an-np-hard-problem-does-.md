# Fable 5 vs. GPT-5.6 Sol on an NP-Hard Problem: Does /goal help?

- Score: 205 | [HN](https://news.ycombinator.com/item?id=48956879) | Link: https://charlesazam.com/blog/fable-5-gpt-5-6-sol-goal/

## TL;DR
Azam benchmarks Claude Fable 5 vs GPT‑5.6 Sol on KIRO, a huge NP‑hard fiber-network design problem, with and without each system’s `/goal` mode. Fable 5 is markedly stronger and far more consistent, delivering the best overall solution and the tightest score spread. `/goal` isn’t a generic “try harder” button: it slightly improves medians but worsens means by occasionally amplifying bad strategies. HN comments highlight wildly different user experiences across coding models, context-management pain, and confusion about when persistence features like `/goal` or “ultra” actually help.

---

## Comment pulse
- Model rankings are highly personal → some see Codex as a massive upgrade over Claude Code; others find Fable/Opus or DeepSeek superior, especially for languages like Elixir—counterpoint: “YMMV” is a recurring refrain.  
- Long coding sessions → users report Claude degrading at high context, compaction hurting quality, and recommend task-based resets, reviews in fresh threads, and avoiding weeks-long sessions.  
- Persistence knobs → `/goal` and “ultra” modes are often misread as magic boosts; commenters note they can be worse and pricier for many tasks, despite GPT’s strong contest results.

---

## LLM perspective
- View: Persistence features should default off for hard optimization; they increase variance and can hide regressions behind occasional standout runs.  
- Impact: Tool builders need per-task policies: persistence for legible progress (tests, migrations), plain mode for brittle heuristic search.  
- Watch next: Multi-problem, multi-model evals that report variance, tails, and resource use, plus clearer UX around “goal” and “ultra” semantics.
