# Claude Code now reads AGENTS.md if there is no Claude.md

- Score: 479 | [HN](https://news.ycombinator.com/item?id=49760187) | Link: https://code.claude.com/docs/en/changelog

### TL;DR

Claude Code 2.1.277 now reads `AGENTS.md` as project instructions when no `CLAUDE.md` exists. Users can change the selected file through “Project instructions” in `/config`; the fallback is not yet available on Bedrock, Vertex, or Foundry. This removes a small compatibility barrier for repositories shared across coding agents. HN users welcomed movement toward a common convention, described previously maintaining symlinks between instruction files, and noted that Claude Code still does not discover skills stored under `.agents/skills`.

### Comment pulse

- Shared instructions reduce repository clutter → teams using multiple agents no longer need duplicate files or compatibility symlinks for basic guidance.
- The fallback fixes awkward behavior → Claude previously noticed `AGENTS.md` yet could claim no project instructions existed without explicit prompting.
- Compatibility remains incomplete → `.agents/skills` discovery is still unsupported, prompting users to maintain hooks or symlinks.

### LLM perspective

- View: A fallback convention is useful interoperability, though `CLAUDE.md` still retains precedence.
- Impact: Multi-agent projects can maintain one instruction source with fewer synchronization errors.
- Watch next: Track hosted-platform rollout, nested-file semantics, skills-directory support, and whether other harnesses converge on the convention.
