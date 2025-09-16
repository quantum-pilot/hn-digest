# Wikipedia as a Graph

- Score: 253 | [HN](https://news.ycombinator.com/item?id=45066060) | Link: https://wikigrapher.com/paths

TL;DR
Wikigrapher turns English Wikipedia into a navigable graph (≈7M pages, 692M links) to compute and visualize shortest paths, with an API and dashboards. HN praises the speed/UI but notes paths often route through categories, list pages, and award-recipient lists—suggesting link weighting and filters. Others point to Wikidata/DBpedia for typed relations and share dump-parsing tools. There’s prior art on BFS over dumps. A reported missing Love→Kissinger path hints at a bug.

Comment pulse
- Better paths via link weighting/filters → downweight categories, 'lists', 'See also'; emphasize infobox/bio links; avoids award-list shortcuts and anchor-text surprises — counterpoint: categories can be valid.
- Leverage Wikidata/DBpedia → typed relations (named after, etc.) enrich edges; prior art includes BFS on dumps; open-source dump parsers shared.
- Impressive build speed (~2h per dump) and slick frontend; reports of a missing Love→Kissinger path suggest a bug vs Six Degrees.

LLM perspective
- View: Shortest-path on dense Wikipedia favors hubs; modeling link semantics and position will yield more meaningful connections.
- Impact: Fast public graph + API enables research, teaching, and games; better ranking aids explainability over six-degree puzzles.
- Watch next: Expose edge weights and filters; path constraints; per-topic subgraphs; human-judged benchmarks; compare latency/coverage with Six Degrees.
