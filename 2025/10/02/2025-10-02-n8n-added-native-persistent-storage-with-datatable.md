# N8n added native persistent storage with DataTables

- Score: 151 | [HN](https://news.ycombinator.com/item?id=45450044) | Link: https://community.n8n.io/t/data-tables-are-here/192256

### TL;DR

n8n v1.113 introduces beta Data Tables on every plan, adding native state that persists across workflow executions. Suggested uses include deduplication, status tracking, prompt reuse, AI evaluation datasets, lookups, and merges. Storage defaults to 50MB, with a configurable limit for self-hosters. Commenters welcomed an alternative to JSON blobs and external databases, but discussion quickly broadened to licensing distrust, competing automation platforms, and whether visual workflows remain manageable when production integrations require many custom code and HTTP nodes.

### Comment pulse

- Missing primitive arrives → users previously improvised persistent state with remote blobs or files, making native tables a practical simplification.
- Licensing anxiety → commenters expect community restrictions and named Node-RED, Windmill, and AutoKitteh as alternatives.
- Visual-versus-code tradeoff → n8n improves accessibility and connector coverage, but complex flows can become spaghetti built from custom nodes.

### LLM perspective

- View: Native state removes a common workaround but does not resolve platform governance or workflow complexity.
- Impact: Small automations can consolidate storage inside n8n; production teams must still assess portability and concurrency needs.
- Watch next: Beta durability, migrations, backup behavior, concurrency semantics, size-limit ergonomics, and licensing changes.
