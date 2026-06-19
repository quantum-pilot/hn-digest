# Clojure Hosted on Go

- Score: 194 | [HN](https://news.ycombinator.com/item?id=48578326) | Link: https://github.com/glojurelang/glojure

## TL;DR

Glojure is an early-stage, hosted Clojure interpreter running on Go. It offers a Clojure-style REPL, scripting, and the ability to embed Clojure as a scripting language inside Go applications. Because it’s “hosted,” Go values and Glojure values interoperate directly, with built-in access to many Go standard-library packages and a generator to expose additional ones. It differs slightly from JVM Clojure in numeric types and implementation details, and is currently a tree-walk interpreter prioritizing interop and extensibility over raw performance.  

## Comment pulse

- Go as FP host → People like Go as a target for functional languages, citing Lisette and the strong Go runtime/tooling ecosystem.  
- Project maturity/maintenance → Users note forks and maintenance locations, and wonder how far Glojure and other Clojure dialects have progressed toward parity—counterpoint: still clearly early-stage.  
- REPL / dialect interest → Curiosity about whether the REPL compiles to Go or runs on a VM, and enthusiasm for fast-evolving Clojure dialects on non-JVM hosts.  

## LLM perspective

- View: Hosted Clojure on Go neatly combines Go’s deployment story with Clojure’s expressiveness and macro system.  
- Impact: Most useful for Go shops wanting dynamic configuration, plugins, or REPL-driven development without leaving their ecosystem.  
- Watch next: Benchmarks, improved interop generation, and stability guarantees (v1), plus comparisons with Lisette and Joker in real-world tooling use.
