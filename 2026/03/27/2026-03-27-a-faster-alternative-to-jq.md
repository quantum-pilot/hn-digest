# A Faster Alternative to Jq

- Score: 361 | [HN](https://news.ycombinator.com/item?id=47539825) | Link: https://micahkepe.com/blog/jsongrep/

### TL;DR
jsongrep is a Rust CLI that treats JSON as a tree and your query as a regular language over paths (keys/indices). It compiles queries into an epsilon-free NFA, then a DFA, and does a single depth‑first walk of the JSON tree, pruning non-matching branches and using zero‑copy parsing. Benchmarks against jq-like tools on up to 190MB JSON show slower query compilation but much faster search and best end‑to‑end times. HN discussion centers on jq’s syntax, whether speed really matters, and niche big‑data use cases.

---

### Comment pulse
- jq ergonomics are polarizing → some find its operators arcane and prefer CEL, JavaScript, or Clojure/EDN-based tools—counterpoint: others find jq’s dot/pipe style intuitive and powerful.
- Speed skepticism → many say jq/yq already feel fast; they value clearer syntax and examples over microsecond wins for typical CLI use.
- Big-data and ops care → TB-scale ndjson/logs, high-RPS servers, and map-reduce-like shell pipelines do hit jq limits; faster, lower-CPU tools compound into real savings.

---

### LLM perspective
- View: Compiling JSON path queries to DFAs is a clean application of classic automata theory to a very practical niche.
- Impact: Most casual jq users won’t switch; power users in data/infra and Rust projects embedding JSON search might.
- Watch next: More expressive yet still-regular query features, benchmarks on ndjson/streaming, and integration with log/metrics pipelines.
