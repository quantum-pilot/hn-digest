# Notion API importer, with Databases to Bases conversion bounty

- Score: 182 | [HN](https://news.ycombinator.com/item?id=45271942) | Link: https://github.com/obsidianmd/obsidian-importer/issues/421

### TL;DR

Obsidian posted a $5,000, 30-day bounty for an importer that uses Notion’s API, converts pages and attachments to Obsidian-flavored Markdown, and maps Notion Databases into `.base` files. The difficult part is preserving structures whose models differ: views, columns, groups, formulas, calendars, and kanban may need selective conversion or fallbacks. HN discussion viewed bounties as useful but review-intensive, while debating whether LLM-assisted development can handle migration edge cases without strong human testing, architectural judgment, and maintenance.

### Comment pulse

- Bounties can activate interested contributors → modest payments may save maintainers substantial work, but weak submissions raise review costs.
- LLMs may accelerate API exploration and repetitive migration work → experienced commenters warn Notion edge cases still demand manual verification.
- Export-versus-API remains contested → file exports are simpler, but omit database data needed for faithful Bases conversion.

### LLM perspective

- View: The hard problem is semantic mapping, not downloading pages or emitting Markdown.
- Impact: A robust importer would reduce migration lock-in for users with structured Notion workspaces.
- Watch next: Accepted conversion rules, reproducible fixtures, unsupported-feature fallbacks, and maintainable tests across API changes.
