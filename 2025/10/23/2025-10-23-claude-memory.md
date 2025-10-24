# Claude Memory

- Score: 328 | [HN](https://news.ycombinator.com/item?id=45684134) | Link: https://www.anthropic.com/news/memory

- TL;DR
    - Anthropic added optional, privacy-controlled memory to Claude: project-scoped context, a user-editable memory summary, admin off-switches, and Incognito chats that never write to memory. Initially for Team/Enterprise, it’s now rolling out to Pro/Max. Anthropic says it safety-tested against over-accommodation and misuse. HN reception is mixed: power users value precise, one-shot prompting and worry memory makes the black box murkier, contaminates outputs, and persists mistakes; others want structured presets/checklists so the model recalls environments and preferences without re-explaining every session.

- Comment pulse
    - Experts prefer one-shot prompts; persistent memory adds hidden inputs, confounds debugging, and degrades outputs—plan-mode/prompt refinement seen as safer and more token-efficient.
    - Desire explicit controls: per-workspace presets, checkbox check-ins, environment verification; frustration when tools ignore preferences (e.g., npm vs pnpm) despite 'skills' or .md instruction files.
    - Reliability worries: chats drift, bad info sticks in memory; 'AI psychosis' risk noted—counterpoint: consistency can aid usability but demands clearer safety results.

- LLM perspective
    - View: Continuity is useful, but experts need transparent, scoped, reversible memory with visible diffs and per-turn controls.
    - Impact: Best for recurring workflows and teams; advanced users may prefer incognito plus prompt libraries, project workspaces, and checklists.
    - Watch next: Measure session-to-session accuracy drift, memory contamination rates, and rollback efficacy; ship environment detection prompts and admin/compliance audit logs.
