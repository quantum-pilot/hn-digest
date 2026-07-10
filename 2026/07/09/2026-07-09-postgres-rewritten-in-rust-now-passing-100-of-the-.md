# Postgres rewritten in Rust, now passing 100% of the Postgres regression tests

- Score: 303 | [HN](https://news.ycombinator.com/item?id=48841676) | Link: https://github.com/malisper/pgrust

## TL;DR
A Rust reimplementation of PostgreSQL, largely generated with LLM help, now passes 100% of the upstream regression suite and claims major speedups: ~1.5× for transactional workloads and ~300× for analytics, approaching ClickHouse on ClickBench. It uses a thread-per-connection model and likely more modern storage/layout techniques. HN discussion is excited but wary: people question benchmark setup and correctness (Jepsen, fsync, MVCC), reviewability of mass‑generated code, the AGPL relicensing, and emphasize real-world shadow-testing and community building.

*Content unavailable; summarizing from title/comments.*

## Comment pulse
- Impressive performance and test results → but real confidence needs Jepsen, heavy fuzzing, and mirrored production traffic comparison—counterpoint: regression suite is still a meaningful baseline.
- LLM-written code is hard to review → shift scrutiny to tests, fuzzing, and invariants; “vibe coding” without deep specs risks subtle, catastrophic bugs.
- AGPL relicensing sparks debate → legally fine with PostgreSQL’s BSD-style license, but culturally contentious amid trends of tighter licenses on rewrites.

## LLM perspective
- View: Using LLMs to “rewrite by tests” is viable only when combined with aggressive differential testing and formalized invariants.
- Impact: Database projects may adopt Rust+LLMs for subsystems first (storage, query engine) before full drop-in replacements.
- Watch next: Independent benchmarks, Jepsen reports, shadow-production trials, and clarity on extension safety under the thread-per-connection model.
