# A new experimental Go API for JSON

- Score: 263 | [HN](https://news.ycombinator.com/item?id=45182770) | Link: https://go.dev/blog/jsonv2-exp

TL;DR (70–90 words)
Go 1.25 ships an experiment: encoding/json/v2 and a lower-level jsontext. v2 adds options to Marshal/Unmarshal, streaming interfaces (MarshalJSONTo/UnmarshalJSONFrom), and stricter defaults: valid UTF‑8, no duplicate keys, nil slices/maps as []/{}. It reimplements v1 for gradual migration and reports large Unmarshal speedups. HN discussion: early adopters see mostly drop‑in behavior, debate omitempty vs new omitzero semantics, and compare against Sonic/goccy’s unsafe/JIT speed. Maintainers ask folks to run workloads to catch perf/allocation regressions.

Comment pulse
- Real-world tests mostly pass under GOEXPERIMENT=jsonv2 → some saw big perf wins, one found allocation regression; jsontext enables streaming and custom parsers.
- omitempty vs omitzero → omit after JSON encoding vs omit by Go zero-ness; omitzero customizable via IsZero; omitempty useful for foreign types.
- High-performance libs like Sonic/goccy → speed from JIT/unsafe; auditability and portability suffer; arm64 slower; benchmarks often ignore v2 — counterpoint: measure on your workload.

LLM perspective
- View: Clear separation of syntax vs semantics plus streaming interfaces modernizes Go's JSON without breaking v1 users.
- Impact: Strict defaults (UTF-8, duplicate keys, case-sensitive) reduce footguns; nil map/slice normalization eases interop.
- Watch next: Track Unmarshal speedups across architectures, memory regressions, and adoption of MarshalerTo/UnmarshalerFrom in major libraries.
