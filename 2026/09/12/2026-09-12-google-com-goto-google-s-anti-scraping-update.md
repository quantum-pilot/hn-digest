# google.com/goto: Google's anti-scraping update

- Score: 648 | [HN](https://news.ycombinator.com/item?id=49668386) | Link: https://www.autom.dev/blog/google-search-goto-links

### TL;DR

Scraping provider Autom reports that logged-out and private Google searches increasingly replace readable destination links with opaque `/goto` redirects. Resolving each target requires another request to Google and reading the Location header, raising latency, crawler cost, and detectability compared with parsing result HTML. Autom says it updated its API pipeline accordingly and interprets the change as anti-scraping enforcement, though the rollout may remain experimental. HN criticized broken link transparency, tracking, slower navigation, and barriers favoring large crawlers over independent search tools.

### Comment pulse

- Link shimming weakens user control → hovering, copying, archiving, and diagnosing destinations become dependent on Google's redirect service.
- Extra resolution requests penalize constrained networks → each result can introduce another server round trip and possible stall.
- Independent indexing faces structural barriers → blocking automated crawlers entrenches major search engines; counterpoint: downloadable datasets cover some specialized sources.

### LLM perspective

- View: An anti-scraping measure also changes the human-readable contract of hyperlinks, imposing costs beyond automation.
- Impact: Small indexers, accessibility tools, archivists, and low-bandwidth users bear more friction than well-funded scraping vendors.
- Watch next: Rollout coverage, browser behavior, redirect latency, alternative URL extraction, and effects on independent search services.
