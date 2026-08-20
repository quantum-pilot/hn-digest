# Claude: System Prompts

- Score: 758 | [HN](https://news.ycombinator.com/item?id=49319556) | Link: https://platform.claude.com/docs/en/release-notes/system-prompts

### TL;DR

Anthropic documents the core system prompts used by Claude’s web and mobile apps, which supply current information and behavioral guidance; they do not govern API calls. The page provides dated versions from Claude 3 through Claude 5 and says models from the 4.6 generation onward use one fixed snapshot per model ID. Commenters welcomed the audit trail but found it incomplete without tool definitions or Claude Code prompts. They also debated whether lengthy instructions waste attention, explain inconsistent brevity, or provide necessary environmental and safety constraints.

### Comment pulse

- Community-maintained diffs help audit behavioral changes, but missing tool schemas and Claude Code prompts obscure actual capabilities.
- Long instructions may consume context and attention—counterpoint: explicit environment, safety, and edge-case rules can avoid repeated inference.
- Crisis overrides split users between fears of unwanted paternalism and reports of genuinely valuable intervention.

### LLM perspective

- View: Transparency requires interpreting prompts, tools, model snapshots, and policy layers together; prompt text alone is incomplete.
- Impact: Developers can separate wrapper changes from model changes, though consumer-app behavior still will not map directly to API use.
- Watch next: Publish tool definitions, test prompt ablations, disclose safety evaluations, and provide machine-readable diffs.
