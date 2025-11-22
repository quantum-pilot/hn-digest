# FAWK: LLMs can write a language interpreter

- Score: 198 | [HN](https://news.ycombinator.com/item?id=46003144) | Link: https://martin.janiczek.cz/2025/11/21/fawk-llms-can-write-a-language-interpreter.html

- TL;DR
    - An FP-loving developer imagines a “modern AWK” with first-class arrays/functions, lexical scope, explicit globals, and pipeline syntax, then uses Claude via Cursor to actually implement it. The LLM produces a working FAWK interpreter and tests in a day, with only tricky numeric details needing help from libraries. The author reassesses LLM capabilities but worries about owning unfamiliar, machine-written code. HN commenters share similar language/interpreter projects, celebrating huge productivity gains while debating quality, verbosity, and whether these systems really reason.

- Comment pulse
    - LLMs can now co-create full languages (FAWK, Aether, Perchance) quickly via “vibe coding” sessions with tests and PRs—counterpoint: output often hides architectural or performance flaws.
    - Solo devs report building substantial DSLs and tooling (webpipe, LSPs, blogs) in spare hours; others prefer established, less-verbose DSLs like JetBrains .http or Perl.
    - Experiments show LLMs inferring semantics of novel stack languages and generating correct programs; detailed transcripts persuade some observers that genuine reasoning is occurring.

- LLM perspective
    - View: LLMs excel at scaffolding interpreters from examples, but spec accuracy and long-term maintainability still demand human oversight.
    - Impact: Enables far more hobby languages and DSLs; shifts developers from writing every line to curating tests and architecture.
    - Watch next: Standard benchmarks and competitions for LLM-designed interpreters, plus studies of defect rates versus traditionally authored compilers.
