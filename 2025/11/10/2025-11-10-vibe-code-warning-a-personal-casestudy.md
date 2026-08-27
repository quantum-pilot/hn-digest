# Vibe Code Warning – A personal casestudy

- Score: 206 | [HN](https://news.ycombinator.com/item?id=45874987) | Link: https://github.com/jackdoe/pico2-swd-riscv

### TL;DR

An embedded developer describes using Claude Code to expand a roughly 1,000-line, personally understood RP2350 RISC-V debugging prototype into a tested library approaching 10,000 lines. Although the result works in the author’s projects and has a substantial test suite, they lost their mental model around 3,000–4,000 lines and no longer felt ownership, trust, or accomplishment. AI was more satisfying when used to digest documentation and generate focused support tools. The central warning is that plausible-looking generated code can overwhelm human judgment faster than tests restore it.

### Comment pulse

- Readers split between valuing the creative process and prioritizing a useful result, with some treating AI as another abstraction layer.
- Critics argued that the outcome depends heavily on planning, decomposition, review, testing, and how quickly generated code is accepted.

### LLM perspective

- View: Test coverage proves observed behavior, not that a maintainer still understands the system’s design.
- Impact: Generation speed can create an ownership deficit whose maintenance cost appears only after the initial success.
- Watch next: Workflows that cap change size and require human reconstruction of invariants before accepting generated code.
