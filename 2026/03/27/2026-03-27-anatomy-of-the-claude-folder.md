# Anatomy of the .claude/ folder

- Score: 349 | [HN](https://news.ycombinator.com/item?id=47543139) | Link: https://blog.dailydoseofds.com/p/anatomy-of-the-claude-folder

## TL;DR
Article explains how Claude Code’s .claude folder controls behavior: project vs global configs, CLAUDE.md instructions, modular rules, commands/skills, agents, and permissions via settings.json. It recommends short, focused instructions, path‑scoped rules, custom slash commands for common workflows, and narrowly tooled sub‑agents, plus a staged setup: start with /init, then permissions, then rules/skills. HN discussion debates elaborate setups versus “plain Claude,” notes skills’ value in huge or bespoke systems, raises CI/agent security, and points out commands are now merged into skills.

## Comment pulse
- Complex .claude setups resemble productivity porn; minimal config plus “plan then execute” often wins—counterpoint: deep skills/toolchains are a step‑change in huge, distributed or custom systems.  
- Some advocate starting with empty .claude, only self‑authored skills, no random packages; others value shared rules/permissions as guardrails when many developers use agentic tools.  
- Several argue CLAUDE.md should be tiny with links, not long “gotchas”; note skills now subsume commands, and doubt cross‑vendor config standards given model‑specific prompting differences.  

## LLM perspective
- Treat .claude like infra: evolve from pain points (thrashing, repetition, unsafe commands) instead of designing an elaborate system upfront.  
- Biggest gains are in large, long‑lived codebases and compliance workflows; personal projects need only a lean CLAUDE.md and few skills.  
- Tools should add agent‑mode profiles with stricter defaults, and explore skill/rule specs so workflows survive switching IDEs or model providers.
