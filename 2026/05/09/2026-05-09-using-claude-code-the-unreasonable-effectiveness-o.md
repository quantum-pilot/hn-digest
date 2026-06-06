# Using Claude Code: The unreasonable effectiveness of HTML

- Score: 405 | [HN](https://news.ycombinator.com/item?id=48071940) | Link: https://twitter.com/trq212/status/2052809885763747935

## TL;DR
HTML is emerging as a surprisingly powerful “lingua franca” for working with LLMs: it’s universal, executable in any browser, and lets models embed UI, logic, and visuals in a single file. HN commenters describe using one-page `index.html` apps (with inline JS/CSS) as throwaway tools, prototypes, dashboards, and design sandboxes, often generated or tweaked by Claude. Debate centers on tradeoffs versus Markdown: HTML is richer but more verbose, harder for humans to hand-edit, and riskier and costlier in tokens.

*Content unavailable; summarizing from comments and context.*

---

## Comment pulse
- Single-file HTML apps as LLM target → Easy to run, share, and iterate; great for quick calculators, internal tools, and design prototypes.

- HTML vs Markdown for co-authoring → Markdown is more human-friendly for specs and revisions; HTML favors delegating structure and polish to the model — counterpoint: modern editors make HTML editing trivial.

- Tradeoffs and strategy → HTML is less token-efficient and has more security surface; richer semantics may justify cost and help tool lock-in for vendors.

---

## LLM perspective
- View: HTML is an ideal “compiled artifact” format; Markdown remains better as the human-editable source.

- Impact: Speeds up internal tools, prototypes, and documentation UIs for engineers, analysts, and product teams.

- Watch next: Better HTML-aware editors, safer sandboxes, and workflows that auto-transform Markdown plans into interactive HTML artifacts.
