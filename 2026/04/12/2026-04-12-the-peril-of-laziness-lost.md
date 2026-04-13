# The peril of laziness lost

- Score: 271 | [HN](https://news.ycombinator.com/item?id=47743628) | Link: https://bcantrill.dtrace.org/2026/04/12/the-peril-of-laziness-lost/

- TL;DR  
  - Brian Cantrill reinterprets Larry Wall’s “laziness” as the drive to invest hard thinking and abstraction now to keep systems small, simple, and powerful later. Modern hustle culture and LLM‑turbocharged “vibe coding” invert this, glorifying sheer lines of code (e.g., Garry Tan’s 37k LOC/day boast) while bloating systems with junk. Because LLMs have no cost for their own time, humans must supply virtuous laziness—constraints, deletion, and architecture—so AI serves simplicity instead of entropy.

- Comment pulse  
  - LLM‑boosted LOC/test counts are vanity metrics → cheap code and trivial tests hide gaps, maintenance pain, and security risk—counterpoint: only net value, not output matters.  
  - Right level of abstraction is hard → commenters favor WET/Rule‑of‑three to avoid premature platforms, second‑system over‑engineering, and today’s excessive layering.  
  - Laziness as virtue vs vice → some see it as forcing simplicity; others worry it excuses procrastination rather than deliberate design effort.

- LLM perspective  
  - View: LLMs are powerful code generators but terrible architects; they must be constrained by human‑defined abstractions, tests, and deletion discipline.  
  - Impact: Teams that worship velocity metrics risk technical debt; thoughtful teams will redirect LLM speed toward refactoring, migrations, and glue work.  
  - Watch next: Expect emerging practices: code‑size budgets, LLM‑aware review checklists, and org policies that reward deletion, simplification, and smaller trusted binaries.
