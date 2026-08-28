# What If OpenDocument Used SQLite?

- Score: 276 | [HN](https://news.ycombinator.com/item?id=45132498) | Link: https://www.sqlite.org/affcase1.html

### TL;DR

This hypothetical design replaces OpenDocument Presentation’s ZIP container and large shared XML files with SQLite tables. Even a file-as-row schema remains roughly size-competitive while enabling atomic incremental saves. Storing each slide separately could accelerate first display, reduce memory use, update only changed content, and support background crash recovery. Version and manifest tables could retain history, branching, undo, search, and structured access for other tools. The author advocates SQLite for future formats, not changing OpenDocument. Commenters flag untrusted-file hardening, recoverable deleted data, BLOB limits, and network-filesystem locking.

### Comment pulse

- Security discussion recommends defensive configuration when applications open database documents received from untrusted people.
- Readers debate whether presentations generalize well to text documents and spreadsheets, where useful storage granularity is less obvious.

### LLM perspective

- View: SQLite’s strongest advantage is transactional object-level evolution, not merely replacing ZIP with another container.
- Impact: Better incremental persistence can improve startup, autosave, recovery, and tooling while increasing parser and locking responsibilities.
- Watch next: Prototype measurements and schemas for documents and spreadsheets, plus safe sharing over hostile inputs and network storage.
