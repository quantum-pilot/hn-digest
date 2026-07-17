# SQLite should have (Rust-style) editions

- Score: 350 | [HN](https://news.ycombinator.com/item?id=48928135) | Link: https://mort.coffee/home/sqlite-editions/

### TL;DR
The author argues that SQLite’s historical defaults are dangerously lax for modern applications: foreign keys are disabled, type checking is loose, concurrent writers immediately fail with SQLITE_BUSY, and WAL journaling (key for performance and durability) is off. They propose a Rust-style “edition” pragma, e.g. `PRAGMA edition = 2026`, that atomically opts a database into a bundle of safer, faster defaults (foreign keys on, strict tables, WAL, sane timeouts), preserving backward compatibility while giving new projects robust behavior by default.

---

### LLM perspective
- View: An edition-style pragma is a low-friction way to modernize legacy libraries without fragmenting ecosystems or breaking old deployments.  
- Impact: New SQLite users—especially app and embedded developers—would avoid subtle consistency and concurrency bugs without deep DBA knowledge.  
- Watch next: Prototype an edition wrapper library, measure breakage on real schemas, then formalize a SQLite enhancement proposal around concrete pragma bundles.
