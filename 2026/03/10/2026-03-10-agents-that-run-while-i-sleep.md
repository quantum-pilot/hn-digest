# Agents that run while I sleep

- Score: 185 | [HN](https://news.ycombinator.com/item?id=47327559) | Link: https://www.claudecodecamp.com/p/i-m-building-agents-that-run-while-i-sleep

### TL;DR

Autonomous coding makes output cheap but verification scarce. The author argues teams should define plain-English acceptance criteria before prompting, then test observable behavior after the agent finishes: Playwright for frontends and API checks for backends. Their prototype runs a Bash preflight, plans checks, launches one browser agent per criterion, and has a final judge label results as pass, fail, or human review. Commenters support checkpoints and rollback, yet warn model-written tests can reward-hack, pass trivially, and miss incorrect specifications.

### Comment pulse

- Overnight autonomy compounds small errors → checkpoints, rollback triggers, and concise failure summaries are essential.
- Separate agents add perspective → counterpoint: shared model biases and reward-hacked tests can still create test theatre.
- Human leverage shifts upstream → carefully choosing work and specifying behavior matters more than maximizing concurrent agents.

### LLM perspective

- **View:** Acceptance criteria narrow uncertainty but do not prove the specification represents user intent.
- **Impact:** Review moves from every diff toward specifications, failed behaviors, and anomalous execution traces.
- **Watch next:** Mutation tests, independently authored criteria, checkpoint recovery, and comparisons against human code review.
