# Claude Advanced Tool Use

- Score: 275 | [HN](https://news.ycombinator.com/item?id=46038047) | Link: https://www.anthropic.com/engineering/advanced-tool-use

### TL;DR

Anthropic introduced three beta mechanisms for large agent toolsets: on-demand tool search, programmatic tool calls executed through generated code, and examples embedded in tool definitions. The first avoids loading every schema, the second keeps bulky intermediate results outside model context, and the third demonstrates parameter conventions that schemas cannot express. Anthropic reports internal gains in token use and tool accuracy, but these are first-party evaluations. Commenters propose GraphQL, typed SDKs, or direct code as simpler alternatives and question whether search adds avoidable complexity.

### Comment pulse

- Selective discovery reduces context bloat → tool ranking, ambiguous overlap, and added latency become new failure modes.
- Code orchestration makes loops and aggregation explicit → direct SDK or GraphQL access may achieve similar economy with less ceremony.

### LLM perspective

- View: Each feature targets a distinct bottleneck; adopting all three by default would be premature.
- Impact: Large-tool agents can spend context on decisions instead of schemas and raw intermediate records.
- Watch next: Independent benchmarks, beta stability, security boundaries, and comparisons with typed-code and GraphQL designs.
