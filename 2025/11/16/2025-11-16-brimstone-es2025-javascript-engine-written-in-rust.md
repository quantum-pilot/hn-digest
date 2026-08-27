# Brimstone: ES2025 JavaScript engine written in Rust

- Score: 180 | [HN](https://news.ycombinator.com/item?id=45944337) | Link: https://github.com/Hans-Halverson/brimstone

### TL;DR

Brimstone is a from-scratch Rust JavaScript engine targeting full ECMAScript support. The repository reports more than 97% language coverage in test262, with a bytecode VM, compacting garbage collector, custom parser and regular-expression engine, and most built-ins implemented. It remains explicitly unready for production and lacks SharedArrayBuffer and Atomics. Commenters admired the three-year solo effort, compact binary, and reported benchmark performance, while noting that bundled Unicode data complicates size comparisons with Boa and that Brimstone uses substantial unsafe Rust.

### Comment pulse

- Compliance impressed readers → a largely solo engine reportedly passes over 97% of the official language suite.
- Binary-size comparisons need normalization → Boa embeds Unicode tables while Brimstone relies on ICU4X differently.
- Rust branding prompted debate → memory-safety expectations are tempered by the garbage collector's acknowledged unsafe code.

### LLM perspective

- View: Brimstone's achievement is specification breadth from a small effort, not yet production readiness.
- Impact: Engine implementers gain another readable Rust design and comparison point for parsers, runtimes, and garbage collectors.
- Watch next: Measure test262 gaps, performance, unsafe-code auditing, Unicode packaging, and eventual SharedArrayBuffer support.
