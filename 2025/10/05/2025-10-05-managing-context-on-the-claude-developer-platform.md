# Managing context on the Claude Developer Platform

- Score: 177 | [HN](https://news.ycombinator.com/item?id=45479006) | Link: https://www.anthropic.com/news/context-management

### TL;DR

Anthropic introduced two beta mechanisms for long-running agents. Context editing removes stale tool calls and results as token limits approach, while a client-side memory tool lets Claude create and consult files stored in developer-controlled infrastructure across conversations. Anthropic reports that combining them improved its internal agentic-search evaluation by 39% over baseline; context editing alone improved it 29% and cut tokens 84% in a 100-turn search test. These are vendor-reported results, and commenters note both techniques formalize patterns developers could already implement themselves.

### Comment pulse

- Developers wanted manually editable transcripts that can remove obsolete code or repair a bad model response’s lingering influence.
- Others warned deleting tool results can break assumptions, reduce cache reuse, and trigger unsupported reconstruction of missing context.

### LLM perspective

- View: Context management is selective forgetting plus durable notes; correctness depends on preserving dependencies, not merely shrinking tokens.
- Impact: Platform primitives reduce implementation work but may deepen coupling to provider-specific conversation and memory semantics.
- Watch next: Independent evaluations should measure factual drift, cache costs, recovery after deletion, and portability across models.
