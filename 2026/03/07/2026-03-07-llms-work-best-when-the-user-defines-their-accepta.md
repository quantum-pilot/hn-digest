# LLMs work best when the user defines their acceptance criteria first

- Score: 418 | [HN](https://news.ycombinator.com/item?id=47283337) | Link: https://blog.katanaquant.com/p/your-llm-doesnt-write-correct-code

### TL;DR

An audit of an LLM-generated Rust SQLite reimplementation found code that compiled and passed tests yet made primary-key lookups roughly 20,000 times slower than SQLite. Its planner missed named INTEGER PRIMARY KEY fast paths, while per-statement synchronization, schema reloads, cloning, and allocations compounded overhead across 576,000 lines. A second 82,000-line daemon overbuilt cleanup that existing tools could handle. The author argues agents optimize for plausible fulfillment, so users must define measurable acceptance criteria before generation and independently benchmark outcomes. HN emphasized review asymmetry: fast generation creates slow, costly verification.

### Comment pulse

- Agents patch flawed foundations with fast paths, adapters, and tests, making initial mistakes expand fractally instead of correcting architecture.
- Small autocomplete chunks keep review manageable — counterpoint: thousand-line generated pull requests shift hours of comprehension and refutation onto reviewers.
- Legal drafting shows the same asymmetry: plausible unsupported output is cheap to create but expensive for judges or opponents to disprove.

### LLM perspective

- **View:** Acceptance criteria turn vague intent into falsifiable constraints that surface failures hidden by plausible structure.
- **Impact:** Teams may generate faster yet deliver slower unless review effort, performance, simplicity, and maintenance are measured.
- **Watch next:** Independent evaluators, benchmark-first workflows, review-cost accounting, smaller diffs, and models rewarded for rejecting bad premises.
