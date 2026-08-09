# Wander – A tiny, decentralised tool to explore the small web

- Score: 181 | [HN](https://news.ycombinator.com/item?id=47422759) | Link: https://susam.net/wander/

### TL;DR

Wander is a two-file, decentralized discovery tool for the small web: an HTML console and a JavaScript list curated by each site owner. A console recommends pages and neighboring consoles; following those links recursively reveals a human-maintained graph without a server, database, account, or installation. Unlike a static blogroll, discovery can continue across communities and include any personal site type. HN readers welcomed a StumbleUpon-like return to serendipity, while noting that an empty or malicious neighbor could trap exploration unless the client retains previously discovered consoles.

### Comment pulse

- Maintenance stays local: owners curate their own lists and prune dead links instead of governing a central index.
- Retaining every encountered console would make the graph resilient to dead ends and let users switch recommendation neighborhoods.
- Readers compared it with blogrolls, webrings, and search engines; recursive transitive discovery is the differentiating behavior.

### LLM perspective

- **View:** Wander trades ranking scale for legible provenance: every recommendation comes from an identifiable curator.
- **Impact:** Small sites gain discovery through relationships rather than engagement optimization or centralized indexing.
- **Watch next:** Cycle handling, cache behavior, abuse resistance, link decay, and tools for merging discovered neighborhoods.
