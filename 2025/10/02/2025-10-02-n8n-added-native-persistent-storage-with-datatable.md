# N8n added native persistent storage with DataTables

- Score: 127 | [HN](https://news.ycombinator.com/item?id=45450044) | Link: https://community.n8n.io/t/data-tables-are-here/192256

- TL;DR
    - n8n added DataTables, a native persistent store, closing a long‑standing gap that forced users to hack state via blobs or external DBs. Commenters welcome the feature but note Node‑RED has had multi‑scope state for years. The thread is dominated by licensing anxiety: fear of VC‑driven feature gating and price hikes, citing MinIO/Taipy, with some users already migrating to Node‑RED and other OSS tools. Others argue visual workflow builders breed spaghetti and custom connectors, suggesting code‑first/agent systems—yet n8n’s turnkey OAuth remains a draw.
    - Content unavailable; summarizing from title/comments.

- Comment pulse
    - Licensing skepticism → VC-backed OSS drifts to feature gating, steep pricing; MinIO/Taipy cited; expect n8n’s shoe to drop — counterpoint: reasonable pricing might retain users.
    - State finally built-in → DataTables addresses long-missing persistence; users hacked JSON blobs before; Node‑RED already offers global/flow/node scopes; n8n’s popularity rising.
    - Visual workflows vs code → Teams report spaghetti flows and custom connectors; others prefer agents or raw code; LangChain/LangGraph criticized for boilerplate; n8n’s OAuth praised.

- LLM perspective
    - View: Native tables fix a core gap but don’t resolve platform risk; portability and exportability matter as licensing clouds grow.
    - Impact: SMBs and hobbyists gain simpler state; enterprises may delay adoption pending licensing clarity; open, code-first alternatives get renewed interest.
    - Watch next: Watch for data size/cap limits, transactional guarantees, export/migration tools, and transparent pricing; benchmark against Node‑RED’s state performance and reliability.
