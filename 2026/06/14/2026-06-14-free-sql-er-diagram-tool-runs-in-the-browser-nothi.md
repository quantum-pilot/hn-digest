# Free SQL→ER diagram tool, runs in the browser, nothing uploaded

- Score: 351 | [HN](https://news.ycombinator.com/item?id=48523992) | Link: https://sqltoerdiagram.com/

### TL;DR

This free, open-source browser app converts `CREATE TABLE` and `ALTER TABLE` DDL for PostgreSQL, MySQL, SQLite, and SQL Server into draggable schema diagrams showing columns, keys, constraints, and relationships. It requires no account or backend, keeps SQL local, exports PNG or SVG, saves projects, and can encode shares in the URL. HN praised exceptional mobile pan, zoom, selection, and editing. Discussion clarified that SQL yields a physical database diagram, not a full conceptual ER model, while raising URL-length, licensing, missing-foreign-key, large-schema, and connector-style concerns.

### Comment pulse

- Mobile interaction sets the tool apart → canvas rendering, cached table bitmaps, and viewport culling kept navigation fluid even with large diagrams.

- Terminology matters → reverse-engineering DDL reconstructs physical tables and declared cardinality, but cannot recover richer conceptual entities, lifecycles, or undocumented relationships.

- Backend-free sharing has limits → encoding the full schema in a URL avoids stored state, but large schemas may exceed interoperable URI lengths.

### LLM perspective

- **View:** It is best framed as an immediate schema explorer, where speed, privacy, and manipulability outweigh formal modeling completeness.

- **Impact:** Developers can inspect databases without schema text leaving the device; educators gain a low-friction way to teach relational structure.

- **Watch next:** Add orthogonal connectors, diagram views, annotations for inferred relationships, explicit license metadata, and safeguards for oversized share URLs.
