# Open source Kanban desktop app that runs parallel agents on every card

- Score: 148 | [HN](https://news.ycombinator.com/item?id=48239413) | Link: https://www.kanbots.dev/

## TL;DR
KanBots is an open‑source, local‑first desktop Kanban app where each card can run its own AI coding agent (Claude Code or Codex) in an isolated git worktree. It adds orchestration features—personas, decision prompts, autopilot, cost caps, GitHub/Sentry integration—and a paid cloud tier only for multiuser collaboration, not code hosting. HN commenters are intrigued but skeptical of unsupervised multi‑agent workflows, worrying about reviewing large AI-generated diffs, preferring small, supervised tasks, and comparing KanBots to Vibe Kanban and Windsurf-style tools.

## Comment pulse
- Unsupervised overnight agents feel unreviewable → big diffs, subtle misunderstandings, and organizational pressure to skip reviews undermine code quality and engineer pride.  
- Many prefer AI for tiny, <20‑line changes → manageable review scope; multi‑agent, long‑running plans feel overwhelming and hard to reconcile.  
- Local‑first, no‑telemetry desktop design is praised → seen as minimum bar for adopting agentic dev tools; users recall Vibe Kanban, request VS Code/remote‑dev integrations.  

## LLM perspective
- View: Framing agents as Kanban work items formalizes supervision—decisions, budgets, personas—rather than treating them as disposable chats.  
- Impact: Helps disciplined solo devs using GitHub issues; large orgs still need process, testing, and governance layered on top.  
- Watch next: Real-world benchmarks of defect rates, review times, and cost per feature versus traditional development and IDE-integrated agents.
