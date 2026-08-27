# Show HN: 22 GB of Hacker News in SQLite

- Score: 261 | [HN](https://news.ycombinator.com/item?id=46435308) | Link: https://hackerbook.dosaygo.com

### TL;DR

Hacker Book packages the Hacker News archive as SQLite data usable entirely in the browser. Instead of downloading roughly 22 GB, its WebAssembly client fetches compressed database shards as browsing or queries require; the displayed archive reports 1,698 shards and 48.2 million items. HN readers admired the static-hosting architecture and compared it with HTTP-range SQLite VFS designs. They also found broad queries inefficient because the client may scan shards sequentially, and noted that the project’s source repository quickly became unavailable.

### Comment pulse

- Sharded SQLite enables serverless archives → static files plus browser WASM provide pages and SQL without an application backend.
- Query locality determines performance → selecting one shard is instant, while unconstrained scans traverse many files.
- Baked data suits public read-only datasets → precomputed artifacts simplify hosting but expose the complete underlying corpus.

### LLM perspective

- View: The design trades universal query efficiency for cheap hosting, portability, and incremental transfer.
- Impact: Publishers can ship substantial interactive archives without maintaining database servers or bespoke APIs.
- Watch next: Source restoration, shard pruning, query planning, and comparisons with range-requested SQLite or Parquet.
