# A Social Filesystem

- Score: 229 | [HN](https://news.ycombinator.com/item?id=46665839) | Link: https://overreacted.io/a-social-filesystem/

- TL;DR  
    - Dan Abramov describes the AT Protocol as a “social filesystem”: each person has a repository of JSON records, grouped into schema-governed collections and globally addressed with DIDs and at:// URIs. Apps become interchangeable views and writers over this shared, verifiable data layer instead of silos owning your posts and graph. Examples like Bluesky, custom feeds, Sidetrail, and Teal.fm scrobbles show new apps can appear or die while your data persists. HN readers like the vision but flag complexity, permanence, and adoption risks.

- Comment pulse  
    - Data should outlast code → open, documented formats let many apps interoperate; the real leverage is incentivizing big platforms to embrace, not subvert, shared standards.  
    - Social/commerce as marketplaces → if users and sellers host their own data/APIs, platforms become discovery layers, reducing fees, lock‑in, and gatekeeping.  
    - Self-describing lexicons won’t auto-generate good UIs or fix spam; PDS replication makes posts quasi-permanent — counterpoint: private data planned, and solving lock‑in still valuable.

- LLM perspective  
    - View: AT makes “social data” a shared, typed log like Git+RSS, with apps as competing read/write views.  
    - Impact: Most impact lands on power users, indie devs, and niche networks first; incumbents won’t adopt until user pull is undeniable.  
    - Watch next: Watch for robust private/DM semantics, migration tooling from Twitter/Reddit, and standardized moderation/abuse schemas shared across AT apps.
