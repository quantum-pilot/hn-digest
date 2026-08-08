# An update on GitHub availability

- Score: 302 | [HN](https://news.ycombinator.com/item?id=47932422) | Link: https://github.blog/news-insights/company-news/an-update-on-github-availability/

### TL;DR

GitHub says agentic development pushed repository creation, pull requests, APIs, automation, and monorepos beyond its 10× capacity plan, requiring infrastructure designed for 30× current scale. It is expanding Azure compute, isolating Git and Actions, reducing database load, moving hot paths from Ruby to Go, and exploring multicloud resilience. The April 23 merge-queue regression affected 658 repositories and 2,092 pull requests; an April 27 Elasticsearch overload disrupted search-backed UI. Commenters welcomed scale data but remained skeptical that stated reliability priorities match persistent outages and incomplete status reporting.

### Comment pulse

- Critics saw continued feature churn despite reliability promises — counterpoint: large teams can improve capacity while unrelated teams ship interface work.
- Users reported incomplete pull-request lists while CLI results were correct and the status page claimed all systems operational.
- Multicloud plans raised doubts about Azure, though others called provider diversity sensible for a platform this large.

### LLM perspective

- Publish labeled workload graphs and service targets so customers can distinguish growth pressure from execution failures.
- Automated rollback gates should cover multi-PR squash groups before merge-queue changes reach production.
- Watch the Elasticsearch analysis and whether availability metrics become granular enough for enterprise risk decisions.
