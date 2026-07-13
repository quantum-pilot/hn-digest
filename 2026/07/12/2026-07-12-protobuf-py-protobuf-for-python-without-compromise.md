# Protobuf-py: Protobuf for Python, without compromises

- Score: 129 | [HN](https://news.ycombinator.com/item?id=48827058) | Link: https://buf.build/blog/protobuf-py

- TL;DR  
  Buf’s protobuf-py introduces a new Python Protobuf runtime/generator focused on speed, type hints, and introspectable, idiomatic classes instead of Google’s opaque, C++-style bindings. Discussion praises improved ergonomics and performance but debates Buf’s tooling model and potential lock‑in. A Google Protobuf engineer explains the official library’s constraints—huge internal usage, three runtimes, strict backward compatibility—and welcomes alternatives. Others worry about relying on non‑standard implementations and question micro‑optimizing in Python, with defenders citing system‑wide serialization costs.

  *Content unavailable; summarizing from title/comments.*

- Comment pulse  
  - Buf tooling is rent‑seeking and hard to remove → critics describe painful lock‑in; others say CLI/registry are usable free and greatly simplify protoc.  
  - Google engineer: official Python Protobuf must support massive internal surface and three runtimes → explains odd APIs, stresses long‑term stability, endorses ecosystem tools like Buf.  
  - Alternative implementations worry some after gogoproto’s demise → fear long‑term breakage in non‑standard Protobufs—counterpoint: Protobuf lacks a formal standard; diversity explores better ergonomics and parsers.

- LLM perspective  
  - View: Multiple high‑quality runtimes per language are healthy if they pass conformance tests and are easy to swap at boundaries.  
  - Impact: Python shops heavy on gRPC, ML, or microservices may gain faster, clearer schemas without rewriting surrounding infrastructure.  
  - Watch next: Watch adoption in major frameworks, Buf’s pricing/governance signals, and whether Google simplifies or deprecates its current Python binding strategy.
