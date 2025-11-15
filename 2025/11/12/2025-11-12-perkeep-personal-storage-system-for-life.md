# Perkeep – Personal storage system for life

- Score: 313 | [HN](https://news.ycombinator.com/item?id=45896130) | Link: https://perkeep.org/

- TL;DR
  - Perkeep (formerly Camlistore) is an open‑source, privacy‑first, content‑addressed personal datastore aiming for decades‑long durability with multi‑backend replication and access via phone, browser, and FUSE. A 0.12 “Toronto” release arrives after ~5 years idle. HN praises the architecture but cites near‑abandonment, hard‑coded indexers, weak integrations, and slow community momentum; adoption hinges on effortless ingest/search across devices and clouds. Skeptics say a filesystem plus backup suffices; others note simpler peers like Timelinize and separate tools for webpage archiving.

- Comment pulse
  - Compelling design, but near-abandonware → years-long pause, sparse community, hard-coded indexers, slow PRs; missing mobile/cloud ingest and polished search. — counterpoint: 0.12 just restarted activity.
  - Question the premise → filesystem plus replication/versioning covers most needs; better to separate organization and backup than adopt a monolith; overview docs exist but unconvincing.
  - Compare/alternatives → Timelinize favors files+sqlite for approachability; for bookmark/page archiving people use ArchiveBox, SingleFile, WebScrapBook, Zotero, LinkDing.

- LLM perspective
  - View: A personal, content-addressed data lake is valuable, but wins only with seamless ingestion, rich indexing, and durable portability guarantees.
  - Impact: If revived, early adopters: self-hosters, researchers, journalists; could pressure cloud providers via import/export connectors and multi-backend replication.
  - Watch next: Roadmap clarity, plugin/indexer SDK, mobile clients, photo/notes importers, FUSE stability, PR velocity, and migration guides from Dropbox/Google Photos.
