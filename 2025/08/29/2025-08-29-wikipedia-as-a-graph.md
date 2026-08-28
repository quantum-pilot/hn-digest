# Wikipedia as a Graph

- Score: 253 | [HN](https://news.ycombinator.com/item?id=45066060) | Link: https://wikigrapher.com/paths

### TL;DR

Wikigrapher is an alpha, JavaScript-dependent tool for finding paths between Wikipedia articles. Its September 2025 English dump models roughly 7.05 million pages, 11.58 million redirects, 2.55 million categories, and hundreds of millions of page links, alongside redirect and category relations. The interface exposes solver, direction, and layout options plus an API. Commenters found it entertaining but warned that unweighted shortest paths often produce weak semantic connections through lists, awards, or categories, and suggested weighting link placement or using richer Wikidata relationships.

### Comment pulse

- A reported missing path between two prominent subjects was suspected to be a bug.
- Readers proposed excluding categories or assigning lower value to incidental navigational links.

### LLM perspective

- View: Graph reachability is easy to compute, but meaningful relationship quality depends on edge semantics.
- Impact: Raw shortest paths can look authoritative while encoding editorial layout more than conceptual closeness.
- Watch next: Compare weighted Wikipedia links against Wikidata relations and test suspected no-path failures.
