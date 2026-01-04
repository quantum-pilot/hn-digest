# Tally – A tool to help agents classify your bank transactions

- Score: 86 | [HN](https://news.ycombinator.com/item?id=46475218) | Link: https://tallyai.money/

## TL;DR
CLI tool Tally uses AI coding assistants (Copilot, Claude Code, etc.) to turn messy bank transaction strings into detailed, user-defined categories stored as local rules. You export CSVs, Tally orchestrates the AI to infer merchants and write categorization logic, then it generates a spending report—all without cloud storage or a database. Hacker News debates whether this should remain a deterministic regex script, notes how irregular real-world descriptors are, questions the manual CSV workflow, and discusses AI cost and experimentation.

## Comment pulse
- AI is needless complexity for a deterministic task → substring/regex rules are transparent, cheap, and won’t hallucinate budgets—counterpoint: messy, irregular descriptors make handcrafted rules unmaintainable.  
- Workflow feels unfriendly → users expect direct bank integrations like Puzzle, not manual CSV exports and AI-in-the-loop CLIs, especially for non-technical budgeting.  
- Cost and access matter → some want to avoid paid models; others note Tally works without AI and mention free tiers from Gemini and OpenRouter.  

## LLM perspective
- View: This pattern—LLMs drafting human-reviewable rule files—blends probabilistic understanding with deterministic execution, mitigating hallucination risk while handling long-tail merchants.  
- Impact: If polished, similar tools could become add-ons to finance software, empowering power-users without requiring banks to expose APIs.  
- Watch next: Benchmarks comparing Tally-plus-LLM vs regex-only pipelines on accuracy, reproducibility, and cost would clarify when AI is truly justified.
