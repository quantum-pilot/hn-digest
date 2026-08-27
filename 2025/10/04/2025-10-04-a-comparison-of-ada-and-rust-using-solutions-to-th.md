# A comparison of Ada and Rust, using solutions to the Advent of Code

- Score: 182 | [HN](https://news.ycombinator.com/item?id=45473861) | Link: https://github.com/johnperry-math/AoC2023/blob/master/More_Detailed_Comparison.md

### TL;DR

Using Advent of Code solutions, the author compares Ada 2022 and Rust 2021 across safety, types, performance, error handling, generics, enumerations, and iteration. Both target reliable systems work, but Ada emphasizes problem-domain types, ranges, contracts, readability, a detailed standard, and built-in tasking; Rust emphasizes memory safety, result-based errors, pattern matching, macros, functional iterators, and strong release performance. The author cautions that neither implementation nor benchmark is necessarily idiomatic. Commenters add that ecosystem, Unicode semantics, compiler speed, and Rust’s built-in threads complicate several comparisons.

### Comment pulse

- Readers particularly admired Ada’s range types, dimensional checking, SPARK verification, and readability.
- Others argued Rust’s tooling, libraries, community, and current formal-specification efforts matter more for many practical projects.

### LLM perspective

- View: The comparison reveals different safety philosophies more clearly than it identifies a universal winner.
- Impact: Ada encodes domain constraints directly; Rust offers stronger ecosystem momentum and ownership-centered memory safety.
- Watch next: Project-specific trials should include dependencies, interoperability, compiler behavior, certification, staffing, and long-term maintenance.
