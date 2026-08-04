# Protobuf-py: Protobuf for Python, without compromises

- Score: 129 | [HN](https://news.ycombinator.com/item?id=48827058) | Link: https://buf.build/blog/protobuf-py

### TL;DR

Buf’s protobuf-py is a from-scratch Protocol Buffers runtime for Python 3.10+ that passes the full binary and JSON conformance suite across proto2, proto3, and editions. Messages remain ordinary slotted Python objects, generated files are readable and typed, imports are relative, and registries are explicit; an optional Rust accelerator handles parsing and serialization. Against Google’s upb, its isolated parse and serialize throughput was 0.22× and 0.60×, but a text-heavy end-to-end workload reached 1.06× by avoiding repeated C-to-Python field conversion. HN welcomed the design while questioning vendor trust, longevity, and benchmark generality.

### Comment pulse

- Google’s awkwardness reflects compatibility commitments → one engineer cited three interchangeable backends, Java 8 support, decade-old generated code, and critical internal use.
- Alternative-runtime risk is organizational → gogoproto veterans feared another painful migration — counterpoint: Buf’s conformance discipline and multi-language footprint provide reassurance.
- Pricing history damaged trust → users praised Buf’s free CLI and registry but described paid code-generation changes as rent-seeking and costly to unwind.

### LLM perspective

- **View:** The architectural bet is eager Python materialization: slower boundaries can win when applications inspect and mutate enough fields afterward.
- **Impact:** Teams gain navigable generated code and static typing, but replacing an entrenched runtime expands dependency and migration responsibility.
- **Watch next:** Benchmark binary-heavy, sparse-read, large-message, free-threaded, and pure-Python workloads; verify schema compatibility and upgrade stability over multiple releases.
