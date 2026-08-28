# A new experimental Go API for JSON

- Score: 263 | [HN](https://news.ycombinator.com/item?id=45182770) | Link: https://go.dev/blog/jsonv2-exp

### TL;DR

Go 1.25 adds experimental `encoding/json/v2` and `encoding/json/jsontext` packages to address compatibility-locked flaws in the original API. The new design separates syntax from Go-value semantics, supports true token and value streaming, passes options through calls, and enables caller-defined conversions. Safer defaults reject invalid UTF-8 and duplicate names, use case-sensitive field matching, and encode nil maps or slices as empty objects or arrays. The team reports roughly comparable marshaling and substantially faster unmarshaling, but seeks broader testing before possible Go 1.26 adoption.

### Comment pulse

- One user’s large suite passed except for an error-message change; another found major speedups alongside a memory-allocation regression.
- Commenters welcomed `jsontext` while debating tag semantics, API complexity, unsafe optimizations, and third-party benchmark quality.

### LLM perspective

- View: A parallel API is justified when compatibility guarantees preserve defaults that now carry correctness and security costs.
- Impact: Shared internals and configurable semantics offer migration without permanently maintaining two independent implementations.
- Watch next: Production regressions, allocation behavior, streaming adoption, final tag semantics, and the Go 1.26 stability decision.
