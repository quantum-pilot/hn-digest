# SQLite as a Document Database (2020)

- Score: 197 | [HN](https://news.ycombinator.com/item?id=49426995) | Link: https://dgl.cx/2020/06/sqlite-json-support

### TL;DR

SQLite 3.31’s generated columns let applications store complete JSON documents as text while extracting selected fields into virtual or stored columns for constraints, indexes, and efficient queries. Invalid JSON can fail at insertion, required keys can use NOT NULL, and new virtual projections can be added later—useful for webhooks whose important fields emerge over time. Commenters distinguish document modeling from merely storing JSON, note newer JSONB support, and emphasize that the example preserves the original body rather than discarding it.

### Comment pulse

- Documents emphasize self-contained records → JSON is merely one representation, while relational models distribute related facts across tables.
- Retrospective indexing is the feature → applications can preserve raw payloads, then expose and index only fields that become operationally useful.
- SQLite remains pragmatic → commenters report document-style deployments with blobs, change tracking, backups, and newer JSONB functions.

### LLM perspective

- View: Generated columns bridge flexible ingestion and relational enforcement without requiring an early, exhaustive schema.
- Impact: Small applications can postpone specialized document infrastructure while retaining indexes, constraints, and a single-file deployment.
- Watch next: Measure write validation, index growth, and migration behavior against representative payloads before adopting this pattern broadly.
