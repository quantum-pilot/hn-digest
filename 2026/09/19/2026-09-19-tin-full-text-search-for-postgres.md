# Tin: full-text search for Postgres

- Score: 218 | [HN](https://news.ycombinator.com/item?id=49766611) | Link: https://planetscale.com/blog/introducing-tin

### TL;DR

PlanetScale introduced TIN, a Postgres extension supporting Boolean, phrase, fuzzy, wildcard, regex, counting, and BM25-ranked searches with transactional visibility and concurrent updates. Its design uses native physical tuple identifiers, two-level page/offset bitmaps, vectorized set operations, visibility-map intersections, and mergeable segments without document renumbering. In PlanetScale's 150-million-document benchmark, TIN delivered at least 8× competitors' throughput across reported scenarios and built fastest within 32 GB. HN praised the database engineering but noted equivalent local performance is not currently distributed and rejected unsupported assumptions that AI wrote it.

### Comment pulse

- Native ctids remove translation overhead → TIN returns Postgres-ready identifiers and reuses page structure for compression, visibility checks, heap-order reads, and segment merging.
- Vendor benchmarks need independent reproduction → reported gains are large, but the production implementation is hosted while the local project tests syntax without matching performance.
- BM25 is not the difficult part → commenters emphasized storage layout, MVCC, updates, fault tolerance, and merging over the ranking formula itself.

### LLM perspective

- View: TIN's advantage comes from designing around Postgres internals rather than embedding a search engine behind an identifier mapping layer.
- Impact: Hosted Postgres users gain richer search without a separate service, while self-hosters cannot yet evaluate the same implementation locally.
- Watch next: Independent workloads, crash recovery, replication, update-heavy longevity, index bloat, licensing, and availability outside PlanetScale's managed platform.
