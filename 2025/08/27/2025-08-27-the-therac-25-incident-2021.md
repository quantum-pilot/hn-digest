# The Therac-25 Incident (2021)

- Score: 449 | [HN](https://news.ycombinator.com/item?id=45036294) | Link: https://thedailywtf.com/articles/the-therac-25-incident

### TL;DR

The Therac-25 radiotherapy machine caused six severe overdoses between 1985 and 1987, injuring and killing patients. One race condition let a fast operator’s corrected beam selection appear onscreen without recalculating the treatment sequence; another shared byte counter incorrectly became zero every 256 increments. With hardware interlocks removed, cryptic errors normalized, incident reports fragmented, and software testing largely dismissed, those defects could deliver massive radiation doses. The article argues that organizational process—not one programmer alone—created the catastrophe.

### Comment pulse

- Commenters emphasized independent hardware safeguards, dose detectors, and designs where no single software failure can cause an accident.
- Medical and engineering anecdotes reinforced that reporting culture, redundancy, and institutional assumptions matter alongside code quality.

### LLM perspective

- View: Therac-25 is fundamentally a systems-safety failure in which software defects escaped every organizational layer meant to contain them.
- Impact: Compiler checks and tests help, but safety-critical systems also need independent interlocks, incident escalation, and skeptical regulation.
- Watch next: Audit whether modern automated systems fail safely when software behaves arbitrarily, operators move quickly, or communications break.
