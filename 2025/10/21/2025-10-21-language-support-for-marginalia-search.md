# Language Support for Marginalia Search

- Score: 161 | [HN](https://news.ycombinator.com/item?id=45653143) | Link: https://www.marginalia.nu/log/a_126_multilingual/

- TL;DR
  - Marginalia Search shipped experimental German/French/Swedish support by parameterizing its NLP pipeline (language definitions, POS-pattern rules, stemming only for TF‑IDF) and adding tooling. To curb lexicon growth, hash collisions, and cross‑language homographs, it maintains per‑language indexes pointing to shared document lists. Non‑English corpora are still tiny—millions vs 100M+ English—due to English‑centric crawling; a new domain‑verification process aims to rebalance. HN readers praised the technical transparency, asked for site‑search/white‑label integration, and probed POS‑tagger performance.

- Comment pulse
  - Educational release note → readers valued the deep dive into pipeline design; author says writing clarifies thinking and aids future maintenance.
  - Site-specific/white‑label search wanted → ad‑hoc domain filters and a public API are planned to enable fast “site search.”
  - Implementation curiosity: POS‑tagger and speed → uses optimized RDRPOSTagger; language detection and sentence splitting are other bottlenecks.

- LLM perspective
  - View: Per-language indices are a smart tradeoff for recall/precision and performance on a small-team, budget-constrained crawler.
  - Impact: Quality depends on growing non‑English corpora; without TF‑IDF stats, BM25 carries ranking, limiting keyword extraction benefits.
  - Watch next: Train per-language TF‑IDF models; add lemmatization/segmentation for morphologically rich/CJK languages; benchmark collision rates and multi-index latency.
