# Minions: Stripe’s one-shot, end-to-end coding agents

- Score: 92 | [HN](https://news.ycombinator.com/item?id=47110495) | Link: https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents

### TL;DR

Stripe says its unattended Minions now produce more than 1,000 merged pull requests weekly, with humans reviewing but writing none of the submitted code. Engineers launch them from Slack or internal tools; a prewarmed, isolated devbox, a customized Goose agent, conditional rules, and curated MCP tools carry each task through branch creation, tests, CI, and a review-ready pull request. Stripe limits CI to two rounds. Commenters questioned whether PR volume measures value, warning that review burden and reduced hands-on coding could offset parallelism and erode reviewers’ skills.

### Comment pulse

- Supporters see unattended agents as a way to resolve many small tasks concurrently, especially during on-call work.
- Critics called the headline volume a vanity metric — counterpoint: Stripe describes merged, human-reviewed changes integrated with demanding internal checks.
- Developers feared becoming permanent validators and losing implementation judgment; others framed current experimentation as a necessary path toward better tools.

### LLM perspective

- **View:** Minions demonstrate that agent throughput depends more on prepared environments, constrained tools, and fast feedback than model autonomy.
- **Impact:** Work shifts toward task specification, platform design, and review, risking bottlenecks and skill decay if review demand grows.
- **Watch next:** Change complexity, escaped defects, review time, revert rates, human coding share, and productivity normalized per merged outcome.
