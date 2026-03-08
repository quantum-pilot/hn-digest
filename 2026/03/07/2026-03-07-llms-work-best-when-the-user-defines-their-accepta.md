# LLMs work best when the user defines their acceptance criteria first

- Score: 418 | [HN](https://news.ycombinator.com/item?id=47283337) | Link: https://blog.katanaquant.com/p/your-llm-doesnt-write-correct-code

## TL;DR
An engineer benchmarks an LLM-generated Rust reimplementation of SQLite and finds basic primary-key queries up to 20,000× slower than real SQLite despite passing tests. Root causes are planner and I/O design bugs plus many individually “safe” choices that collectively wreck performance. A second 82k‑line Rust disk-space manager similarly overbuilds a problem solvable by a one-line cron job. Combined with evidence of sycophancy and degraded code quality, the essay argues LLMs are only effective when users predefine strict, measurable acceptance criteria.

## Comment pulse
- LLMs compound complexity → naive prompts cause ever-growing abstractions, tests, and workarounds; reviewing and untangling this costs far more time than generation.  
- Legal commenters report similarly: models draft convincing yet unsound arguments that overwhelm courts and opponents because refuting weak reasoning takes vastly more effort.  
- Practitioners increasingly restrict LLMs to small autocomplete-like snippets while keeping humans responsible for system design, performance tuning, and final code ownership.  

## LLM perspective
- View: Use LLMs as fast drafters only after you’ve specified invariants, performance targets, and explicit failure conditions they must satisfy.  
- Impact: Organizations that treat generated code as authoritative, especially without strong reviewers, will accumulate massive technical, legal, and operational debt.  
- Watch next: Toolchains that embed profilers, property-based tests, and static analyzers to reject plausible-but-wrong LLM output before humans review it.
