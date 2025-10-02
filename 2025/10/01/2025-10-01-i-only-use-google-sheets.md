# I only use Google Sheets

- Score: 303 | [HN](https://news.ycombinator.com/item?id=45435463) | Link: https://mayberay.bearblog.dev/why-i-only-use-google-sheets/

- TL;DR
    - A junior operator argues for defaulting to Google Sheets in fast-changing small businesses: it ships fastest, reveals real requirements, and avoids overbuilt, unused tools. He replaced months-long admin, quoting, and CRM efforts with simple sheets, then recommends iterating once scope stabilizes. HN broadly agrees on spreadsheets as rapid workbenches, while warning about scale-induced pain: versioning, fragmentation, one-to-many limits, and vendor lock-in. Alternatives like Grist surface, yet anecdotes show spreadsheets persisting even through enterprise system rollouts.

- Comment pulse
    - Low barrier and extensible → offline mobile data entry; developers use Apps Script via clasp/TypeScript; resonates with HyperCard/Visual Basic tinkering culture.
    - Operational risks → multi-file sprawl across SharePoint/network drives causes conflicting sources; versioning/testing weak; Excel track-changes exists but is rarely adopted.
    - Inertia is real → spreadsheets survive corporate system rollouts; migrate when SSO/SAML, row-level permissions, or complex one-to-many models become mandatory.

- LLM perspective
    - View: Start in Sheets to learn requirements; formalize into a schemaed system once relationships, permissions, and audit needs stabilize.
    - Impact: Saves cycles for small teams; reduces premature architecture; demands a clear migration plan to avoid long-term data debt.
    - Watch next: Tools bridging spreadsheets and databases: row-level security, versioning, lineage, offline-first, and Apps Script alternatives with better testing.
