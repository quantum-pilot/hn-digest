# The 49MB web page

- Score: 232 | [HN](https://news.ycombinator.com/item?id=47390945) | Link: https://thatshubham.com/blog/news-audit

### TL;DR

A New York Times page triggered 422 requests and about 49 MB of transfer over two minutes, illustrating how ad auctions, trackers, video, overlays, layout shifts, sticky elements, and engagement gates overwhelm the article itself. The author proposes delayed or serialized prompts, reserved dimensions, lazy ads, pausable video, local dismissal state, and text-first alternatives. HN agreed the experience is hostile but qualified the headline: one measurement attributed roughly 36 MB of 44.5 MB to journalistic video, not advertising, and noted newsrooms’ desperate ad economics.

### Comment pulse

- Test under constrained hardware and networks → powerful developer machines conceal CPU, bandwidth, and layout costs experienced by ordinary readers.
- Incentives drive the clutter → publishers monetize less-savvy visitors while ad blockers remove the audience most hostile to tracking.
- The critique has its own irony → commenters noted the author’s site also loads Cloudflare analytics.

### LLM perspective

- **View:** Payload size alone misdiagnoses the problem; interruption, instability, and unbounded third-party execution better capture user harm.
- **Impact:** Publishers trade reader trust and accessibility for marginal ad and subscription conversions.
- **Watch next:** Per-component byte budgets, Core Web Vitals, low-end-device tests, and conversion results from calmer prompt timing.
