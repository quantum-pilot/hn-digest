# Ruff v0.16.0 – Significant new updates – 413 default rules up from 59

- Score: 332 | [HN](https://news.ycombinator.com/item?id=49056112) | Link: https://astral.sh/blog/ruff-v0.16.0

### TL;DR

Ruff 0.16 expands its zero-configuration lint set from 59 to 413 of 968 rules, adding checks for severe syntax and runtime failures plus Bugbear, pyupgrade, and Ruff categories; the former defaults remain selectable. It also formats Python fences in Markdown and Quarto, adds line and file `ruff: ignore` suppressions with reasons and automatic insertion, and displays fix diffs in normal check output. One 3,000-line migration was reported manageable and useful, while commenters debated warning floods and whether automated style enforcement saves or wastes team attention.

### Comment pulse

- Broader defaults improve discovery → users found issues older versions missed — counterpoint: established repositories may face hundreds of newly surfaced warnings.
- Automation can end style arguments → consistent formatting frees reviews for semantics — counterpoint: arbitrary rewrites may erase deliberate presentation choices.
- The cited formatting failure was not Ruff’s behavior → it preserved commented dictionary entries, adding spacing and a trailing comma rather than collapsing them.

### LLM perspective

- **View:** Default policy is product design: selecting rules determines whether newcomers experience immediate value or an intimidating remediation queue.
- **Impact:** Greenfield projects gain stronger safety automatically; mature codebases need staged adoption, explicit selections, or selective suppressions.
- **Watch next:** Measure false-positive rates, migration effort, CI noise, suppression growth, and adoption of Markdown formatting across documentation-heavy projects.
