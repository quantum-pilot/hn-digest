# Woxi: Wolfram Mathematica Reimplementation in Rust

- Score: 225 | [HN](https://news.ycombinator.com/item?id=47155526) | Link: https://github.com/ad-si/Woxi

### TL;DR

Woxi is an AGPL-licensed Rust interpreter implementing a growing subset of the Wolfram Language for command-line scripts, Jupyter and browser-hosted JupyterLite. Its tests compare supported commands against WolframScript, and its native startup avoids kernel and license overhead; the developer targets most Mathematica 1.0 features plus popular newer functions. Hacker News welcomed an open alternative but stressed the immense compatibility, symbolic-correctness, performance and polish challenge. A central design dispute is whether mathematical behavior belongs in Rust or in a small term-rewriting core extended using the language itself.

### Comment pulse

- A tiny rewrite core could scale contributions → symbolic rules in the interpreted language avoid proliferating special-case Rust logic.
- Native implementations promise speed — counterpoint: hard-coded growth may become difficult to maintain, verify and extend consistently.
- Compatibility is a cliff → Mathematica's value reflects decades of breadth, applications, exact symbolic behavior and interface polish.

### LLM perspective

- **View:** Define a conformance target before function count becomes the main progress metric.
- **Impact:** Success could unlock legacy notebooks and scripts for users lacking proprietary licenses.
- **Watch next:** Mathics and Rubi comparisons, randomized symbolic tests, performance profiles, clean-room review and agent-authored code share.
