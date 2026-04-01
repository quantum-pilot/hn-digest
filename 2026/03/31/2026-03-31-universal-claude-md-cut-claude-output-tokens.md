# Universal Claude.md – cut Claude output tokens

- Score: 446 | [HN](https://news.ycombinator.com/item?id=47581701) | Link: https://github.com/drona23/claude-token-efficient

## TL;DR
A small GitHub project ships a single `CLAUDE.md` file that standardizes Claude Code’s behavior: no sycophantic greetings, no restating prompts, ASCII-only output, minimal explanations, and simplest-working code. Benchmarks on explanatory prompts claim ~63% fewer output words, with clear caveats that savings only matter for high-output workflows because `CLAUDE.md` itself consumes input tokens. HN discussion questions its safety and generality: possible quality loss in complex agentic coding, fragile rules (e.g., always trusting user “corrections”), and weak benchmarking around accuracy.

---

## Comment pulse
- Conciseness can degrade agentic coding → explanation tokens often reveal mistakes and maintain long-horizon coherence—counterpoint: some summarize history into markdown (/handoff) instead of keeping everything in context.  
- Several rules look unsafe → “answer on line 1,” “accept user corrections as ground truth” risk confirmation bias, lost pushback, and silent runaway errors.  
- Skeptics expect Anthropic to optimize defaults → if such a prompt truly improved cost/quality, it would likely be integrated; constant “fix Claude” layers churn workflows.

---

## LLM perspective
- View: Treat this as an optional house-style prompt, not a universal performance upgrade or safety layer.  
- Impact: Best for pipelines where Claude emits lots of boilerplate prose; less so for exploratory or high-stakes coding.  
- Watch next: Independent accuracy benchmarks on real coding tasks and variants that relax risky rules while still trimming obvious verbosity.
