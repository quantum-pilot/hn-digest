# Building a Simple Search Engine That Works

- Score: 250 | [HN](https://news.ycombinator.com/item?id=45950720) | Link: https://karboosx.net/post/4eZxhBon/building-a-simple-search-engine-that-actually-works

- TL;DR
  - A developer shows how to build a DB-backed search: two tables (tokens, token→document), three tokenizers (word, prefixes, 3-grams), and a weight scheme combining field/tokenizer/token-length. Indexing batches inserts; querying reuses the same tokenizers and runs a single SQL that sums weights, boosts token diversity and average weight, penalizes long docs, then normalizes. HN likes it for small sites and learning, but flags scaling, underspecified queries, SEO adversaries, org incentives, and feature creep; Lucene/Solr/ES advised for larger deployments.

- Comment pulse
  - Fine for small sites → Search breaks under scale and vague queries; SEO spam makes ranking adversarial — counterpoint: defining relevance is harder than scaling.
  - Corporate search suffers → tuning ranking is iterative, hard to schedule; incentives prioritize other features over search quality.
  - Caution against DIY in production → feature creep (“did you mean?”, taxonomies) and maintenance outstrip teams; better use Lucene/Solr/Elasticsearch.

- LLM perspective
  - View: Solid baseline for in-app search; explicit tokenization and SQL scoring give control, testability, and predictable behavior.
  - Impact: Small teams skip ES/Algolia, keep ops simple, and iterate ranking using domain knowledge instead of external black boxes.
  - Watch next: Benchmarks on corpus size/QPS/latency, index growth; Postgres/SQLite tuning; stemming/stopwords; adversarial spam tests; evaluation datasets and A/B runs.
