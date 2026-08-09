# Git commands I run before reading any code

- Score: 1738 | [HN](https://news.ycombinator.com/item?id=47687273) | Link: https://piechowski.io/post/git-commands-before-reading-code/

### TL;DR

Five shell pipelines mine Git history before code review: rank frequently changed files, measure contributor concentration, find files touched by bug-fix commits, chart monthly commit volume, and search for reverts or emergency fixes. Cross-referencing churn with bug keywords can suggest risk, while authorship and cadence can expose knowledge loss or firefighting. The author treats these as fast diagnostic clues, not proof. HN’s strongest objection was that merge strategy, generated files, automation, commit habits, project maturity, and simple stability can make the same metrics tell a very different story.

### Comment pulse

- Commit-message quality determines several queries → disciplined PR descriptions help, while vague or generated messages erase useful evidence.
- Raw churn and commit counts mislead → active feature files, generated artifacts, bots, and prolific low-value contributors can dominate.
- Readers favored context or richer combinations → churn plus complexity is more actionable than either metric alone.

### LLM perspective

- **View:** These commands are hypothesis generators for interviews and code reading, not a health score.
- **Impact:** Auditors can prioritize investigation quickly, but teams risk unfair personnel or architecture conclusions from repository artifacts.
- **Watch next:** Aliases, exclusion filters, merge-policy awareness, complexity overlays, and validation against tickets, incidents, and team history.
