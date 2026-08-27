# Sj.h: A tiny little JSON parsing library in ~150 lines of C99

- Score: 272 | [HN](https://news.ycombinator.com/item?id=45324349) | Link: https://github.com/rxi/sj.h

### TL;DR

sj.h is a public-domain, roughly 150-line C99 JSON reader that allocates nothing, returns slices, tracks line and column errors, and deliberately leaves number, string, and Unicode handling to callers. That narrow interface appeals to developers wanting auditable single-header code. However, commenters found it permissive enough to accept malformed JSON and noted possible signed-overflow undefined behavior only at extreme sizes. The central dispute is scope: a compact extractor for trusted input may be useful, but it should not be mistaken for a validating, standards-conformant parser.

### Comment pulse

- Minimalism won praise, while critics demonstrated malformed inputs the reader may accept and questioned its safety at untrusted boundaries.

### LLM perspective

- View: The library is compelling only when its deliberately narrow contract and trusted-input assumption are explicit.
- Impact: Mislabeling a permissive extractor as a parser could move validation failures into callers and create inconsistent security boundaries.
- Watch next: Look for conformance-test results, malformed-input documentation, depth limits, and guidance for Unicode and number handling.
