# Show HN: Duck-UI – Browser-Based SQL IDE for DuckDB

- Score: 173 | [HN](https://news.ycombinator.com/item?id=45633453) | Link: https://demo.duckui.com

- TL;DR
  - Duck-UI is a browser-based, self-hostable SQL IDE for DuckDB that runs locally (WASM), supports custom charts, and keeps data on-device. HN compares it with DuckDB’s official web UI: the default is simpler and auto-profiles columns, but isn’t self-hosted/offline and lacks flexible charting. Users report strong production experience with DuckDB on terabytes and praise WASM for sub-200ms local queries. Feedback requests grid virtualization and UX fixes, integration via FlightSQL/Arrow IPC, and possibly adopting Perspective for charting; vector types remain experimental.

- Comment pulse
  - Auto‑profiling panel → built-in UI’s per‑column histograms often replace simple queries; Duck-UI emphasizes custom charts but lacks that one-click profiling.
  - Client‑side performance → WASM keeps compute local, reducing latency; teams process terabytes; vector types experimental — counterpoint: local compute doesn’t help when data lives remote.
  - UX and integrations → request infinite grid, selected-cell panel, better dropdown/menu behavior, dark-mode tooltips; add FlightSQL/Arrow IPC ingestion; consider Perspective for charting.

- LLM perspective
  - View: Local browser SQL IDEs are viable for serious analytics; reduce server dependencies and improve data privacy.
  - Impact: Beneficiaries: analysts handling CSV/Parquet, startups needing quick BI, enterprises with strict data-egress policies.
  - Watch next: Measure WASM vs native throughput, add FlightSQL/Arrow, stabilize vector types, and benchmark Perspective-based charts on large datasets.
