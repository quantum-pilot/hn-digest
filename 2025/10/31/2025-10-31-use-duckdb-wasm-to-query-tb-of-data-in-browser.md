# Use DuckDB-WASM to query TB of data in browser

- Score: 122 | [HN](https://news.ycombinator.com/item?id=45774571) | Link: https://lil.law.harvard.edu/blog/2025/10/24/rethinking-data-discovery-for-libraries-and-digital-humanities/

- TL;DR
    - Harvard’s Library Innovation Lab built Data.gov Archive Search as a static site running DuckDB‑WASM in the browser to query remote Parquet metadata via HTTP range reads. The model delivers search/browse on multi‑TB archives without servers, cutting ops cost and risk for long‑lived library projects, but needs careful data layout and pays a big WASM download. HN welcomes the simplicity and embedding patterns, compares DuckLake/SQLite alternatives, and debates whether heavy data work belongs in browsers or in traditional backends.

- Comment pulse
    - Embedding DuckDB alongside existing stacks → Hybrid patterns (S3‑hosted .duckdb/Parquet, periodic sync) add analytics without replacing Postgres.
    - Frozen catalogs often unnecessary → Plain Parquet + views update easier; SQLite/httpvfs cover simpler cases; add Postgres only if cataloging needs grow.
    - Browser‑first is pragmatic cross‑platform → WASM enables write‑once compute; critics cite RAM/egress/latency limits — counterpoint: cost and maintainability often trump perfect fit.

- LLM perspective
    - View: Best for read-heavy, append-rare datasets; interactive exploration, catalogs, logs, maps—less for OLTP or multi-user transactions.
    - Impact: Shifts cost from servers to clients and egress; favors institutions with limited ops budgets but distributed users.
    - Watch next: Quantify cold‑start size, range‑read efficiency, and egress; benchmark DuckDB‑WASM vs hyparquet/Arquero; test R2/S3/Cloudflare cache strategies.
