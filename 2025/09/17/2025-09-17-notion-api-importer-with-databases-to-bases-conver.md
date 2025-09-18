# Notion API importer, with Databases to Bases conversion bounty

- Score: 182 | [HN](https://news.ycombinator.com/item?id=45271942) | Link: https://github.com/obsidianmd/obsidian-importer/issues/421

- TL;DR
  - Obsidian posted a $5k, 30‑day bounty to build a Notion API importer that converts Notion Databases into Obsidian Bases (.base YAML), with full Markdown/attachments support and testable, reproducible imports using Notion’s new data‑source API. The goal fills gaps left by Notion’s file exports, especially for databases. HN debates bounties’ effectiveness and fairness, whether LLM‑assisted dev suits this migration, and the Notion API’s quirks and limits. Some envision eventual two‑way sync; others warn about AI‑generated PR spam and brittle, edge‑case‑riddled code.

- Comment pulse
  - Small bounties catalyze contributors → $500–$1k can save maintainers a week, despite review overhead; not a living wage but effective motivation.
  - LLMs fit migration tasks → good at exploring APIs, enumerating edge‑cases, iterating tests — counterpoint: Notion API idiosyncrasies break agents; humans must fix edge cases.
  - Notion API frustrates → limited, non‑parity with UI; Markdown export misses databases. Some want two‑way sync, but conflict‑resolution is hard; maintainers report brittle AI‑generated PRs.

- LLM perspective
  - View: Build a mapping matrix and loss report; treat views as filters; serialize formulas as fields or frozen values with provenance.
  - Impact: Lower switching costs for teams; more Obsidian adoption; increased pressure on Notion to improve exports, YAML frontmatter, and API parity.
  - Watch next: Validate data‑source object quirks, rate limits, pagination; ship conformance fixtures; measure property coverage, attachment fidelity, idempotent re‑runs.
