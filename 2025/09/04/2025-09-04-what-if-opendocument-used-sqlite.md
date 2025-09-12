# What If OpenDocument Used SQLite?

- Score: 276 | [HN](https://news.ycombinator.com/item?id=45132498) | Link: https://www.sqlite.org/affcase1.html

- TL;DR
  - SQLite as a container for OpenDocument (example: presentations) could replace the ZIP pile‑of‑files with a small relational store: per‑slide records enable incremental saves, faster first‑paint, lower memory, and built‑in versioning/crash recovery; file sizes are comparable to ZIP. The essay frames this as a future‑format thought experiment, not an ODF change request. HN discussion highlights security hardening for untrusted files, network‑filesystem locking pitfalls, 2 GiB BLOB limits, and how the approach might generalize to text/spreadsheets; some note Hipp’s advocacy style.

- Comment pulse
  - Use SQLite safely requires secure_delete and untrusted-file settings; otherwise data remnants and attachment RCE risk — counterpoint: SQLite fuzzes heavily and documents mitigations.
  - Beware environment limits: network filesystems without robust locks risk corruption; large assets hit 2GiB BLOB cap; workarounds split blobs or save-temp-then-copy.
  - Beyond slides, value hinges on granularity choices: per-sheet or per-cell for spreadsheets; chapters/blocks for text; better demos requested.

- LLM perspective
  - View: Use SQLite containers for local, single-user documents; design chunked schemas; bake in security pragmas and safe extension policies.
  - Impact: Simplifies autosave/recovery logic; enables per-object diffs/version browsing; unlocks scripting/FTS across documents without custom parsers.
  - Watch next: Standardize schema, publish benchmarks vs ZIP, define blob-splitting and locking guidance, prototype Writer/Calc converters.
