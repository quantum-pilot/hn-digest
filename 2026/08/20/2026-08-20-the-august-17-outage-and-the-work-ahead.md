# The August 17 outage, and the work ahead

- Score: 261 | [HN](https://news.ycombinator.com/item?id=49378957) | Link: https://github.blog/news-insights/company-news/the-august-17-outage-and-the-work-ahead/

### TL;DR

GitHub says its August 17 outage lasted 7 hours 47 minutes, disrupting the site, authentication, Actions, APIs, collaboration features, and Copilot. Peak traffic overwhelmed a critical Central US component; a latent VS Code retry loop then amplified Copilot token traffic roughly tenfold and delayed recovery. GitHub says this and its August 6 incident were capacity failures, not triggered by code or configuration changes, as monthly commits rose from 1.4 billion to 2.9 billion since April. Planned work covers retry budgets, isolation, scalable reads, alerts, and further Azure migration.

### Comment pulse

- Retry opinions split between fast resilience and immediate errors; circuit breakers or server-directed backoff emerged as conditional middle ground.
- Testing criticism met pushback that retry behavior needs integration coverage and perfect unhappy-path coverage is unrealistic.
- The commit surge prompted AI-automation and “productivity panic” theories, plus questions about why commits—not pushes—measure load.

### LLM perspective

- View: A capacity miss became a feedback-loop outage because client recovery behavior multiplied load.
- Impact: GitHub’s central role turns regional infrastructure weaknesses into worldwide development disruption.
- Watch next: Retry-budget rollout, Azure load share, read-scaling deployment, isolation progress, and repeat incident frequency.
