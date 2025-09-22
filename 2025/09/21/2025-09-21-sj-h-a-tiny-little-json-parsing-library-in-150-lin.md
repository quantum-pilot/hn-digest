# Sj.h: A tiny little JSON parsing library in ~150 lines of C99

- Score: 272 | [HN](https://news.ycombinator.com/item?id=45324349) | Link: https://github.com/rxi/sj.h

- TL;DR
  - sj.h is a ~150‑line, single‑header C99 JSON parser that returns string slices with zero allocations and leaves number/string decoding to the user. It reports errors with line:column and targets minimal state and embedding. HN notes it’s intentionally lenient—more a data extractor for known‑good JSON than a validator—and can accept malformed constructs. Discussion flags unchecked integer math that could cause undefined behavior on extreme inputs. Fans praise rxi’s small, permissively licensed libraries; others suggest established, fully compliant parsers for untrusted data.

- Comment pulse
  - Minimalist extractor for known-good JSON → tiny footprint, zero alloc, easy embedding; good when you control producer.
  - Lenient/under-validating parser → accepts malformed constructs (mismatched braces, extra whitespace); not RFC-complete; treat as slicer, not security boundary.
  - Overflow/UB risks → unchecked integer depth/line counters can overflow; constrain input sizes or switch to 64-bit — counterpoint: checks add complexity, defeat minimalism.

- LLM perspective
  - View: This is a slice-based tokenizer, not a full JSON validator; best for controlled pipelines.
  - Impact: Enables tiny, dependency-free parsing in games, tools, and embedded; risky for network-facing services.
  - Watch next: Publish conformance results, document limits and UB cases, offer optional bounds/depth checks without allocations.
