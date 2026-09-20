# You can run Git on object storage if you re-make packfiles

- Score: 144 | [HN](https://news.ycombinator.com/item?id=49730069) | Link: https://www.tigrisdata.com/blog/objgit-packfiles/

### TL;DR

Objgit replaces Git's filesystem-oriented packfiles with an object-storage-native `.bin` data file plus fixed-width `.cue` records containing hashes, types, compression, offsets, and compressed lengths. That metadata enables precise HTTP Range requests while full packfiles download concurrently, avoiding thousands of high-latency bucket operations without changing clients. In Wi-Fi benchmarks across three repositories, the author reports 4–14.6× faster pushes and 1.8–4.5× faster clones. The project remains experimental: authentication, authorization, rate limits, compaction, and large-file handling are unfinished. HN highlighted existing static and proxy alternatives.

### Comment pulse

- Storage layout must match network physics → local mmap-friendly packs lack enough compressed-length metadata for efficient arbitrary object retrieval over HTTP ranges.
- Parallel range reads hide full-download latency → requested objects arrive immediately while a bounded pack container streams into temporary local storage.
- Existing approaches deserve comparison → commenters cited server-info, GitSocial, proxy migration, and object-backed filesystems, but requested equivalent large-repository benchmarks.

### LLM perspective

- View: Reformatting immutable, reconstructible repository data is reasonable when the original format's assumptions create thousands of network round trips.
- Impact: Object-storage Git services could reduce request costs and push latency without requiring custom client behavior.
- Watch next: Add security controls, garbage collection, compaction, Git LFS, failure recovery, and reproducible comparisons against existing implementations.
