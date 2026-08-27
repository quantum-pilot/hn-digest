# Who needs Graphviz when you can build it yourself?

- Score: 495 | [HN](https://news.ycombinator.com/item?id=45742907) | Link: https://spidermonkey.dev/blog/2025/10/28/iongraph-web.html

### TL;DR

SpiderMonkey replaced its Graphviz-based Ion compiler visualization with an interactive, application-specific layout engine. Because JavaScript and WebAssembly control-flow graphs have labeled loop backedges and reducible loops, iongraph can simplify Sugiyama-style layout: preserve branch order, place loop exits predictably, route edges through dummy nodes and use fixed straightening passes. The author reports stable layouts and a large example dropping from roughly ten minutes to 20 milliseconds. The tool is integrated with certain SpiderMonkey shell builds, open sourced and still rough, with no browser exposure planned.

### Comment pulse

- Readers note the comparison is specifically with Graphviz’s dot engine, not every Graphviz layout.
- Critics question whether huge graphs are useful and identify compactness versus readability as a genuine tradeoff.

### LLM perspective

- View: Exploiting domain invariants can outperform general optimization when human comprehension, not abstract graph scores, is the objective.
- Impact: Stable layouts make compiler-pass differences easier to inspect and dramatically reduce rendering latency.
- Watch next: Search, subgraph navigation and evidence from everyday debugging will show whether large visualizations remain tractable.
