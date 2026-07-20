# Claude Code uses Bun written in Rust now

- Score: 370 | [HN](https://news.ycombinator.com/item?id=48966569) | Link: https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/

## TL;DR
Simon Willison verifies that Claude Code now embeds the Rust rewrite of Bun, using simple `strings` checks and a Bun preload trick to reveal an unreleased v1.4.0 canary build. Bun-in-Rust is already running in production across millions of Claude Code installations, with about 10% faster startup on Linux and no visible breakage. Hacker News focuses less on the verification and more on whether a terminal UI built with React/JavaScript and a JS runtime is justified, plus the implications of Anthropic’s Bun acquisition and Rust rewrite.

## Comment pulse
- JS/React TUI is overkill → burns CPU/battery for terminal apps; 40 years of ncurses-style tooling exist — counterpoint: JS gives huge ecosystem and rapid, LLM-assisted iteration.  
- Rust over Zig/C → ownership model and compiler errors eliminate many manual lifetime bugs, a better fit for LLM-written systems code, despite sizable `unsafe` regions.  
- Anthropic’s Bun strategy → keeping a JS runtime preserves Bun’s value, ecosystem, and cloud angles; some worry Bun’s governance is now effectively “Anthropic decides.”

## LLM perspective
- View: Strong type systems plus deterministic compilers (Rust) pair well with stochastic LLM coding, enabling safer large-scale rewrites.  
- Impact: Developer tools may keep JS UIs despite inefficiency, trading runtime performance for speed of iteration and AI-assisted development.  
- Watch next: How Bun’s Rust port stabilizes, governance clarity post-acquisition, and real-world benchmarks in apps like Claude Code.
