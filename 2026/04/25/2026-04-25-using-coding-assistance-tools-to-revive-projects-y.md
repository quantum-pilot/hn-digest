# Using coding assistance tools to revive projects you never were going to finish

- Score: 148 | [HN](https://news.ycombinator.com/item?id=47902525) | Link: https://blog.matthewbrunelle.com/its-ok-to-use-coding-assistance-tools-to-revive-the-projects-you-never-were-going-to-finish/

## TL;DR
The author resurrects an abandoned personal project—a shim that exposes YouTube Music via the OpenSubsonic API—by leaning heavily on Claude Code. With a small FastAPI scaffold, an OpenAPI spec, and clear conventions in a CLAUDE.md file, the LLM rapidly stubs endpoints, iterates against real client logs, adds caching and persistence, and delivers a usable “Sub-standard” service in an evening. They argue AI coding tools are ideal for “wish it existed” side projects, as long as you still tackle hard “learning” projects yourself.

## Comment pulse
- LLMs as game-dev co-pilots → revive old Godot prototypes, implement gameplay loops, procedural systems, even lore; feels collaborative and keeps momentum—counterpoint: some find this anthropomorphism unsettling.
- Personal tools finally ship → weather/clock UIs, notetakers, GraphiQL variants, alarm logic; for solo apps, “code quality be damned” makes LLM output good enough.
- AI vs cheap labor → one user compares this to outsourcing side projects to low-cost freelancers or patronage, but now the “junior dev” is an always-available model.

## LLM perspective
- View: Define specs, conventions, and tests up front; LLMs excel at long-tail endpoint work and glue code.
- Impact: Biggest gains for hobbyists and solo devs with clear ideas but limited time or UI/platform expertise.
- Watch next: IDE-native agents that track project context, plus practices to balance assisted shipping with deliberate skill-building.
