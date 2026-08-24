# Claude Advanced Tool Use

- Score: 275 | [HN](https://news.ycombinator.com/item?id=46038047) | Link: https://www.anthropic.com/engineering/advanced-tool-use

### TL;DR
Anthropic introduced three beta mechanisms for tool heavy agents. Tool Search defers definitions until relevant, reducing context load; Programmatic Tool Calling lets Claude orchestrate, parallelize, and filter calls inside a Python sandbox; Tool Use Examples demonstrate valid parameter patterns. Anthropic reports sizable internal gains in token use and task accuracy, but each feature adds tradeoffs in latency, context visibility, or prompt size. They are complementary, yet teams should adopt only the mechanism matching a measured bottleneck and validate the reported benefits independently.

### Comment pulse
- GraphQL may collapse catalogs into one tool → introspection exposes operations — counterpoint: large schemas can still bloat context.
- Tool retrieval invites ranking games → providers may optimize descriptions for selection — counterpoint: typed SDKs avoid competitive discovery.

### LLM perspective
- View: These features solve real scaling problems, but their benchmark gains remain vendor reported.
- Impact: Well chosen combinations can lower token costs and improve reliable tool selection.
- Watch next: Independent evaluations, retrieval failures, sandbox boundaries, prompt injection resistance, and end to end latency.
