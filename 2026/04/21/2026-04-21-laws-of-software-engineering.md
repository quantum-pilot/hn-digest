# Laws of Software Engineering

- Score: 794 | [HN](https://news.ycombinator.com/item?id=47847179) | Link: https://lawsofsoftwareengineering.com

## TL;DR

A polished reference site catalogs 56 “laws of software engineering” (Conway, CAP, YAGNI, DRY, etc.), grouped by topic and seniority, and sold alongside a book/poster. HN treats it less as authoritative doctrine and more as a grab‑bag of heuristics: useful for naming trade‑offs, dangerous when turned into slogans. The strongest thread is around Knuth’s “premature optimization,” where commenters argue for performance‑aware architecture and measurement from day one, while rejecting nitpicky micro‑optimizations and cargo‑cult readings of old quotes.

---

## Comment pulse

- Premature optimization needs reinterpreting → think about architecture, data access, and concurrency early; measure hotspots later, but don’t assume “we’ll fix perf someday.”  

- Laws conflict and get weaponized → Postel vs Hyrum, DRY vs KISS/YAGNI; real skill is knowing which “law” to break, when, and why.  

- Skepticism about the site/book → vibe-coded, card-heavy design and author’s “cheat sheet” history make some doubt the depth behind the collection.

---

## LLM perspective

- View: Treat these as a vocabulary for design discussions, not commandments; always pair each “law” with explicit context and counterexamples.  

- Impact: Most valuable for juniors and non-specialists to name recurring issues; seniors must actively de‑mythologize and localize them.  

- Watch next: Curated case studies showing laws failing; tools that flag conflicting heuristics in reviews; more emphasis on measurement over aphorisms.
