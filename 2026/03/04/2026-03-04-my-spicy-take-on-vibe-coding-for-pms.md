# My spicy take on vibe coding for PMs

- Score: 181 | [HN](https://news.ycombinator.com/item?id=47240736) | Link: https://www.ddmckinnon.com/2026/02/11/my-%f0%9f%8c%b6-take-on-vibe-coding-for-pms/

### TL;DR

Product managers should use AI coding to communicate ideas, understand systems, run realistic experiments, and exploit unique domain knowledge—but not bypass prioritization to land production changes at Meta scale. The author argues important work belongs in the engineering queue; PM-written pet features consume review time, accumulate debt, and confuse activity with impact. Every AI PM should instead build evaluations. Commenters supplied examples of query storms and incomplete data handling, while converging on a risk boundary: disposable prototypes and low-stakes internal tools are useful; production code needs engineering ownership and accountability.

### Comment pulse

- Engineers described generated happy-path code causing query storms, orphaned data, and review work disproportionate to its value.
- PMs largely endorsed prototyping ideas, then discarding the prototype while engineers implement the production version.
- Low-blast-radius internal tools can be acceptable; counterpoint: commit counts and launch metrics can incentivize unsafe production shortcuts.

### LLM perspective

- **View:** AI changes who can prototype, not who should own reliability, maintenance, and operational risk.
- **Impact:** PM fluency can improve specifications and evaluations while preserving engineering gates for production systems.
- **Watch next:** Review burden, incident rates, abandoned prototypes, and whether generated work advances priorities rather than personal visibility.
