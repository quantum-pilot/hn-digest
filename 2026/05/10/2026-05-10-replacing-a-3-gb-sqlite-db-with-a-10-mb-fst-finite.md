# Replacing a 3 GB SQLite db with a 10 MB FST (finite state transducer) binary

- Score: 160 | [HN](https://news.ycombinator.com/item?id=48082676) | Link: https://til.andrew-quinn.me/posts/replacing-a-3-gb-sqlite-database-with-a-7-mb-fst-finite-state-trandsucer-binary/

### TL;DR

A Finnish-English dictionary outgrew its 60 MB trie when inflected forms expanded from about 400,000 entries to 40–60 million, so the author temporarily shipped a 3 GB SQLite FTS database. Rebuilding the static lookup with Rust’s `fst` crate produced a 10 MB binary—a roughly 300× reduction—because a finite-state transducer shares repeated suffixes as well as prefixes. HN celebrated first shipping the obvious working solution, while warning that temporary architecture can entrench itself and noting the technique’s older DAFSA/DAWG lineage.

### Comment pulse

- Starting with SQLite bought correctness and an oracle for optimization → counterpoint: provisional designs can become prohibitively entrenched.
- Readers traced FSTs through DAWGs, DAFSAs, and Scrabble structures → specialized representations often rediscover mature ideas.
- Some questioned the headline comparison → ordinary compression could shrink SQLite, though not necessarily preserve equivalent searchable access.

### LLM perspective

- **View:** Optimize after real data exposes the dominant redundancy.
- **Impact:** Static corpora benefit most; frequently updated indexes may surrender the advantage.
- **Watch next:** Compare cold latency, build memory, and compressed-database distribution—not just raw file sizes.
