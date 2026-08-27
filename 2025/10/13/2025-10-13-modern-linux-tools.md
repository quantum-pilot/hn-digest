# Modern Linux tools

- Score: 200 | [HN](https://news.ycombinator.com/item?id=45566548) | Link: https://ikrima.dev/dev-notes/linux/linux-modern-tools/

### TL;DR

The captured source exposes a “Modern Linux Tools” page and its categories, but not the substantive replacement table, so the useful detail comes primarily from HN discussion. Commenters debated adopting newer utilities such as ripgrep, fd, jq, fzf, bat, and hyperfine versus mastering classic tools available on nearly every server. Advocates valued speed and friendlier defaults on personal development machines; administrators stressed portability across remote systems. Several wanted every recommendation to state its concrete problem rather than merely claim modernity or implementation language.

### Comment pulse

- Portability favors classics → administrators cannot assume preferred utilities exist across hundreds of heterogeneous remote systems.
- Local productivity favors selective upgrades → developers consider ripgrep, fd, jq, and fzf valuable enough to install alongside standard tools.
- Labels are weak justification → readers wanted explicit problems solved, not “modern,” “better,” or “written in Rust.”

### LLM perspective

- View: This is not replacement versus tradition; it is choosing where installation cost earns repeated workflow savings.
- Impact: Developers can optimize owned environments while retaining baseline fluency for unfamiliar machines and recovery situations.
- Watch next: Evaluate candidates by measurable speed, ergonomics, portability, packaging, and unique capability rather than popularity.
