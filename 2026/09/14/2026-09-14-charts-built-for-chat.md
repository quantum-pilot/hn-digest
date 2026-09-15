# Charts built for Chat

- Score: 220 | [HN](https://news.ycombinator.com/item?id=49704246) | Link: https://dbtcharts.com/blog/charts-built-for-chat/

### TL;DR

dbt Labs open-sourced dbt Charts, an Apache-licensed YAML language that combines SQL, prose, variables, and chart configuration into auditable dashboard files. Its CLI validates and renders boards as SVG, HTML, PNG, PDF, terminal output, or local sites; dbt integration keeps models and charts together in Git and CI. A hosted beta adds conversational analytics, editing, access control, and sharing. HN welcomed BI unbundling and agent-friendly declarative artifacts, while noting similar open projects and questioning whether simple agents can directly generate adequate SVG.

### Comment pulse

- Declarative dashboards constrain agent sprawl → one YAML artifact is easier to audit and revise than generated React, CSS, and chart-library stacks.
- Open chart layers reduce BI lock-in → local rendering and Git portability separate visualization code from optional hosting and permissions.
- The design space already has alternatives → Malloy, DaC, and direct SVG generation may cover overlapping needs with different deployment tradeoffs.

### LLM perspective

- View: Agent-generated analytics needs governed intermediate representations more than another conversational interface.
- Impact: Data teams can review visualization changes like code while nontechnical users retain chat and visual editing.
- Watch next: Grammar stability, semantic-layer support, SQL safety, accessibility, complex-dashboard performance, and interoperability with competing specifications.
