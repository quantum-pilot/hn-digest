# Tracking down the 16-year-old WAL-reset SQLite bug

- Score: 1045 | [HN](https://news.ycombinator.com/item?id=49272832) | Link: https://tailscale.com/blog/sqlite-wal-reset-bug

### TL;DR

Tailscale traced 19 SQLite corruptions over six months to a 16-year-old race between a write transaction and an aggressively managed WAL checkpoint. Under rare timing, the checkpoint could believe pages had reached the main database when they had not, permanently losing data and corrupting references. Transaction replay exposed vanished committed writes; a SQLite support contract and a newly built VFS tracing shim isolated the cause. The fix shipped in 3.51.3 after 3.52.0 was withdrawn for a separate stale-expression-index false alarm.

### Comment pulse

- Recovery improvements cut shard outages from more than an hour to under an hour while investigation continued.
- Existing peer connections survived outages, but new devices, network changes, the admin console, and API access were impaired.
- Four incident-free months followed a production alert proving the fixed race’s trigger still occurred.

### LLM perspective

- View: Documented configurations still carry tail risk when operational cadence differs sharply from common deployments.
- Impact: Tailscale strengthened recovery and funded reusable diagnostics; SQLite users gained a fix for an exceptionally rare race.
- Watch next: Watch aggressive checkpoint users, multi-connection WAL deployments, and adoption of the VFS shim for similarly intermittent corruption.
