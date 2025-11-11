# Vibe Code Warning – A personal casestudy

- Score: 206 | [HN](https://news.ycombinator.com/item?id=45874987) | Link: https://github.com/jackdoe/pico2-swd-riscv

- TL;DR
  - A developer built a Raspberry Pi Pico2 SWD debugger for RP2350 RISC‑V. About 80% of the ~10k LOC library was LLM‑generated (“vibe coded”): it worked, but the author lost the mental model, encountered confident wrongness (e.g., misreading MEM‑AP protocols), and felt no ownership—while AI excelled at digesting specs and tooling. The write‑up also documents a full SWD/DAP/DM stack, defensive dormant‑to‑SWD activation, RP2350 quirks, and SBA. HN debates craft vs throughput, whether vibe coding can be disciplined, and dataset pollution vs “AI as library.”

- Comment pulse
  - Craft gives meaning → understanding and ownership are part of value — counterpoint: most work serves needs; outcome matters.
  - Vibe coding fails without structure → planning, small chunks, tests, and rigorous review determine success; naive prompting produces brittle code.
  - AI‑generated code pollutes datasets → feedback loops risk more nonsense; some expect human curation to filter gems.

- LLM perspective
  - View: Use LLMs for scaffolding, doc parsing, protocol scripts, and tests; author core state machines yourself.
  - Impact: Expect faster prototyping but weaker code taste and explainability; compensate with rigorous tests and provenance.
  - Watch next: Benchmarks of AI‑assisted vs manual debug stacks; tools labeling AI‑generated code; IDEs that track mental models.
