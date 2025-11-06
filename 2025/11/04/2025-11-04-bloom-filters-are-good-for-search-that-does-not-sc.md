# Bloom filters are good for search that does not scale

- Score: 185 | [HN](https://news.ycombinator.com/item?id=45808998) | Link: https://notpeerreviewed.com/blog/bloom-filters/

- TL;DR
    - The post revisits per‑document Bloom filters for full‑text search: tiny and simple for small sites, but scaling fails. Sorting and OR‑trees don’t prune due to high‑dimensional overlap; a “dictionary tree + document filters” collapses into an inverted index. Space math: filters re‑encode every word per document, so beyond a few thousand docs an inverted index is smaller; Bloom filters shine as skip‑indexes, not replacements. HN adds field reports of big block‑skipping speedups, spectral/bit‑sliced variants, and a new online string‑search family.

- Comment pulse
    - Bloom filters as block skip indexes → 30× query speedups, ~1% false positives, ~1.25 KB per 1k‑record block; used in RSA systems and Splunk.
    - Per‑doc Bloom filters duplicate shared vocab → prefer inverted index + per‑chunk filters for skipping — counterpoint: BF‑based online string search shows promising throughput.
    - Alternatives: Spectral Bloom Filters enable counts/ranking; COBS bit‑sliced signatures map n‑grams to document bitmaps, suiting static or genomic corpora.

- LLM perspective
    - View: Use Bloom filters as accelerators atop inverted indexes; avoid per‑document filters when vocabularies overlap heavily.
    - Impact: Client‑side search, OLAP/TSDB, and log analytics benefit most; web‑scale text remains inverted‑index‑centric.
    - Watch next: Benchmark COBS/Xor filters vs postings at 1k–1M docs; measure update costs and FPR; track ClickHouse FTS changes.
