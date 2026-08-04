# The Eternal Sloptember

- Score: 435 | [HN](https://news.ycombinator.com/item?id=48263238) | Link: https://geohot.github.io//blog/jekyll/update/2026/05/24/the-eternal-sloptember.html

### TL;DR

After six months using coding agents on tinygrad and hardware reverse engineering, the author concludes they front-load progress but stall at polish, producing plausible defects that become harder to notice as models improve. He still values LLMs for search and disposable prototypes, but predicts large organizations will accumulate low-quality code because weak feedback loops reward volume while skilled users keep reviewing every line. HN largely favored a narrower tool role, yet challenged the essay’s lack of concrete failures; commenters focused on deferred maintainability, wrong-problem architectures, and the costly final 5–20%.

### Comment pulse

- Enhanced search remains valuable → LLMs retrieve and adapt prior art effectively but should not own full applications or opaque legacy refactors.
- Generation can erase architectural friction → agents defer costs from solving the wrong problem, allowing complexity to compound before teams feel consequences.
- Evidence standards are contested → critics wanted concrete failure examples — counterpoint: others said subtle taste and architecture defects resist isolated demonstrations.

### LLM perspective

- **View:** The relevant unit is the human-agent system; capability without review discipline can raise throughput while reducing net engineering value.
- **Impact:** Organizations with slow feedback, weak ownership, and output-based incentives bear more technical-debt risk than small expert teams.
- **Watch next:** Measure defect escape, maintenance time, rollback frequency, code comprehension, and architectural complexity months after agent-authored changes ship.
