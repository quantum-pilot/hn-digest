# I added a Bluesky comment section to my blog

- Score: 188 | [HN](https://news.ycombinator.com/item?id=46747366) | Link: https://micahcantor.com/blog/bluesky-comment-section.html

### TL;DR

Micah Cantor added comments to a statically generated, CDN-hosted blog by rendering replies to a corresponding Bluesky post. Bluesky supplies identity, storage, spam handling, and moderation, while its public API lets the site retain a native presentation. Cantor wrote roughly 200 lines instead of adopting an existing React component, mainly for styling and future control. An OAuth prototype could post replies directly, but completing it meant building a custom client; the simpler release stores a post identifier in article metadata and fetches replies on page load.

### Comment pulse

- Static ownership remains possible → manually reviewing submissions and committing them as content limits spam and platform lock-in.
- Federation broadens the pattern → commenters reproduced it with Mastodon and reusable non-React components.
- Post discovery can be automated → matching the author’s first Bluesky post containing the article URL removes metadata upkeep.

### LLM perspective

- View: Outsourcing identity and moderation preserves static hosting while keeping discussion visually integrated.
- Impact: One public API adds comments without operating a database, account system, or continuously maintained backend.
- Watch next: Deleted posts, API limits, nested-thread rendering, post discovery, and long-term comment archiving.
