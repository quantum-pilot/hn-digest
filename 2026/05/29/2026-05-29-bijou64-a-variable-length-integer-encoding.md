# Bijou64: A variable-length integer encoding

- Score: 198 | [HN](https://news.ycombinator.com/item?id=48323992) | Link: https://www.inkandswitch.com/tangents/bijou64/

### TL;DR

Bijou64 is a new unsigned-64 varint designed for Subduction’s signed CRDT protocol. Values 0–247 occupy one byte; tags 248–255 declare a fixed payload length, while tier offsets prevent shorter values from being re-encoded at longer lengths. Only the nine-byte tier needs an upper-bound check. Published M2 and Zen benchmarks report 2–10× faster decoding than LEB128, with similar sizes on tested workloads, though the authors stress limited validation. Hacker News challenges the canonicality claim, SIMD performance, boundary efficiency, and whether noncanonical encodings can sometimes be intentionally useful.

### Comment pulse

- Omitting the top-tier range check could wrap values and restore ambiguity — counterpoint: the design calls this bounds validation, not duplicate in-range encodings.
- SIMD may favor ULEB128, sentinel, or text parsing; replies argue length prefixes remain vectorizable and striped control/data formats occupy another design space.
- Deliberately overlong LEB128 supports fixed-width linker placeholders, while Bijou64’s two-byte tier holds far fewer small identifiers than LEB128’s.

### LLM perspective

- **View:** Structural canonicality reduces parser obligations but cannot remove all validation; integer bounds remain a security-critical edge.
- **Impact:** Signed and content-addressed protocols gain simpler byte identity; workloads dominated by medium identifiers may pay extra space.
- **Watch next:** Independent implementations, fuzzing, SIMD codecs, more CPUs, realistic distributions, and formal uniqueness proofs including overflow behavior.
