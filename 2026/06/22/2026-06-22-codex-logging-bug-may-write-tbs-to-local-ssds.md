# Codex logging bug may write TBs to local SSDs

- Score: 460 | [HN](https://news.ycombinator.com/item?id=48626930) | Link: https://github.com/openai/codex/issues/28224

## TL;DR
Codex’s CLI/Desktop shipped with a SQLite “feedback” logger set to global TRACE, continuously dumping high‑volume WebSocket, OpenTelemetry, and dependency logs into `~/.codex/logs_2.sqlite` and its WAL. Users measured ~37 TB written in 21 days (~640 TB/year), enough to exhaust many consumer SSDs and even trigger Codex agents to delete local files when disks filled. The community reverse‑engineered the schema, provided bash/sqlite mitigations, and criticized OpenAI’s responsiveness and code quality. OpenAI has since merged patches to stop logging each WebSocket event and filter noisy targets, reportedly cutting writes by ~85% in upcoming releases.

## Comment pulse
- AI dev tools are seen as sloppy and resource‑hungry → Codex and Claude Code burn GPU/CPU/RAM, are partly closed‑source, and feel unworthy of “near‑AGI” marketing.  
- DIY fixes emerge → SQLite triggers, VACUUM, or cron‑driven WAL truncation mitigate churn—counterpoint: safest option is avoiding Codex or using a RAM disk.  
- Vendor trust questioned → OpenAI appears slow to fix long‑standing issues; some note the logging bug is now patched in the repo and should ship soon.

## LLM perspective
- View: Logging for AI tools must default to minimal, sampled, redactable telemetry with explicit write budgets, not blanket TRACE to local databases.  
- Impact: Heavy disk churn and data‑loss risk undermine developer trust in AI assistants and raise real hardware costs for serious users.  
- Watch next: Whether Codex’s release actually eliminates sustained writes, and if other AI vendors audit their logging for SSD endurance and privacy.
