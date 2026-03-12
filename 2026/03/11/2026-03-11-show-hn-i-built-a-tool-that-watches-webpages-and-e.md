# Show HN: I built a tool that watches webpages and exposes changes as RSS

- Score: 139 | [HN](https://news.ycombinator.com/item?id=47337607) | Link: https://sitespy.app

## TL;DR
A new tool, Site Spy, monitors arbitrary webpages and exposes changes as RSS feeds, focusing on element-level tracking, readable text diffs, and history. It uses a real browser behind the scenes, so it copes better with JavaScript-heavy sites than simple HTML pollers, but can still struggle with anti-bot and complex login flows. HN discussion compares it to open-source options like changedetection.io and urlwatch, and debates whether RSS, email, or direct push notifications are the right primary interface.

*Content unavailable; summarizing from title/comments.*

## Comment pulse
- Strong execution for reporters and monitors → browser-based rendering plus text diffs addresses JS-heavy sites better than naive scrapers, though anti-bot and auth flows remain brittle.

- Comparison to changedetection.io/urlwatch → open-source, self-hosted tools are mature and free; Site Spy trades that for smoother browser extension workflow — counterpoint: skepticism about pricing/novelty.

- RSS vs alerts split → power users like RSS for workflows; others want email/push for urgent events, suggesting products should offer multiple channels and let users choose.

## LLM perspective
- View: Element-level, browser-based monitoring with diff views plus RSS is a pragmatic bridge between scrapers and traditional feeds.

- Impact: Helps journalists, researchers, and “slot/stock” hunters monitor hostile or JS-heavy sites with less custom scripting.

- Watch next: Reliability on anti-bot sites, pricing vs OSS, and richer integrations (webhooks, APIs, email-to-RSS bridges) will determine adoption.
