# Ripgrep is faster than grep, ag, git grep, ucg, pt, sift (2016)

- Score: 328 | [HN](https://news.ycombinator.com/item?id=47499245) | Link: https://burntsushi.net/ripgrep/

## TL;DR
Andrew Gallant’s 2016 post introduces ripgrep, a Rust-based code search tool that combines ack/ag-style recursive, ignore-aware defaults with and often surpassing GNU grep’s speed. He dissects grep-like tools end‑to‑end—directory traversal, .gitignore handling, regex engines, literal extraction, SIMD, buffering, and multithreading—then backs design choices with curated benchmarks on the Linux kernel and large text files. Hacker News readers still treat it as a model of technical writing, debate default .gitignore semantics, and compare newer rivals or index‑based approaches.

## Comment pulse
- Shared .ignore standard improved tooling; some dislike grep-like tools reading .gitignore by default as violating POLA — counterpoint: most developers prefer relevance over POSIX semantics.  
- Post praised as exemplary documentation: explains grep internals, regex engines and benchmarks; commenters note author’s other high-quality libraries like Rust regex and jiff.  
- Practitioners reuse its tricks (least-common-byte, SIMD line handling); others explore even faster tools like cgrep or argue indexes beat ripgrep on 100GB monorepos.  

## LLM perspective
- View: The post shows that practical performance comes from whole-pipeline design, not just a faster regex engine.  
- Impact: Inspired a generation of search tools and editors to embed ripgrep or copy its algorithms for everyday navigation.  
- Watch next: Systematic benchmarks on multi-hundred-GB monorepos comparing ripgrep, cgrep, and indexed search with maintenance costs included.
