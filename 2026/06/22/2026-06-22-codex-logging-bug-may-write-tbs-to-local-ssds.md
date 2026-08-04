# Codex logging bug may write TBs to local SSDs

- Score: 460 | [HN](https://news.ycombinator.com/item?id=48626930) | Link: https://github.com/openai/codex/issues/28224

### TL;DR

Codex’s SQLite feedback logger used a global TRACE default, continuously inserting and pruning low-value websocket, telemetry, and dependency events. One report measured 37 TB written in 21 days, extrapolating to 640 TB yearly—enough to threaten a 600-TBW consumer SSD despite a roughly 1.2 GiB retained database. Two merged changes stopped per-event websocket logging and filtered noisy targets, reportedly cutting writes 85%, and release 0.142.0 shipped the fix. HN users reported similar macOS/Windows behavior, criticized the response time, and traded risky database-trigger and VACUUM workarounds.

### Comment pulse

- Product quality drew broader criticism → users cited spinner-driven GPU load and app memory growth — counterpoint: one heavy user praised Codex’s UX and output.
- Temporary remedies carry tradeoffs → blocking inserts stops growth and VACUUM reclaimed 27 GB, but modifying private schemas or vacuuming large databases adds risk.
- Openness depends on the surface → commenters noted the CLI is patchable on GitHub, whereas the desktop Codex app remains proprietary.

### LLM perspective

- **View:** Tiny retained files can conceal severe write amplification; row-ID growth and device-write counters reveal churn better than database size.
- **Impact:** Raw websocket and SSE payload persistence also creates a local privacy exposure, independent of SSD wear.
- **Watch next:** Verify post-0.142.0 write rates across desktop and CLI; add caps, telemetry summaries, and regression tests for idle churn.
