# Bloom filters are good for search that does not scale

- Score: 185 | [HN](https://news.ycombinator.com/item?id=45808998) | Link: https://notpeerreviewed.com/blog/bloom-filters/

### TL;DR

Per-document Bloom filters can make a tiny client-side full-text index for small sites, but searching every filter scales linearly. The author explores sorting, aggregate trees, and a dictionary tree, ultimately recreating something close to an inverted index. Even with logarithmic lookup, space loses: each document re-encodes its words, whereas an inverted index stores shared vocabulary once. Under the article’s simplified assumptions, the crossover arrives around 7,200 documents. Bloom filters remain valuable atop indexes for safely skipping irrelevant data chunks.

### Comment pulse

- Practitioners reported large search gains when Bloom filters skipped blocks, with false positives affecting performance rather than correctness.
- Alternatives included spectral filters, bit-sliced COBS, and combining inverted indexes with per-chunk filters instead of replacing them.

### LLM perspective

- View: Local compression wins until duplicated vocabulary overwhelms the absence of cross-filter sharing.
- Impact: Architecture should place probabilistic filters at pruning boundaries, not automatically at every document.
- Watch next: Corpus-specific crossover benchmarks, update costs, false-positive rates, and hybrid index designs.
