# A Faster Alternative to Jq

- Score: 361 | [HN](https://news.ycombinator.com/item?id=47539825) | Link: https://micahkepe.com/blog/jsongrep/

### TL;DR

jsongrep is a Rust CLI for locating JSON values by matching paths, with fields, indices, ranges, wildcards, alternation, optionals, and recursive descent. It compiles its regular path language through a Glushkov NFA into a DFA, then traverses the parsed tree once, pruning nonmatching branches with constant-time transitions; zero-copy parsing adds speed. The author’s benchmarks show it outperforming four Rust-based alternatives on large documents. Crucially, it is a search tool, not a full jq replacement: it lacks filters, arithmetic, interpolation, and transformations, while its richer compile step costs more.

### Comment pulse

- Most CLI users prioritize syntax and features because jq feels fast enough — counterpoint: terabyte-scale logs and high-request services expose aggregate costs.
- Limited expressiveness partly explains the lead → comparing a search subset with transformation tools requires task-specific interpretation.
- Large-scale operators value habitual efficiency → savings across many servers and repeated jobs can outweigh the learning cost.

### LLM perspective

- **View:** This is best considered ripgrep for JSON paths, not a drop-in jq replacement.
- **Impact:** Operations and embedded Rust users gain faster lookup; transformation-heavy workflows still need jq or another language.
- **Watch next:** Independent benchmarks, memory use, pathological DFA growth, streaming support, and correctness on varied real workloads.
