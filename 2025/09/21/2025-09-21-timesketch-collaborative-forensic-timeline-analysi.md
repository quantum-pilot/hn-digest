# Timesketch: Collaborative forensic timeline analysis

- Score: 96 | [HN](https://news.ycombinator.com/item?id=45324343) | Link: https://github.com/google/timesketch

- TL;DR
  Timesketch is an Apache-licensed, open-source app for collaborative forensic timeline analysis. It ingests events from multiple sources, lets teams tag, comment, and search, and builds a combined, queryable timeline to trace intrusions or outages. Notebook and API clients support deeper workflows. HN discussion centers on whether it’s more than a “log viewer,” practical uses like incident postmortems, and questions about the UI; screenshots/site indicate a dedicated timeline view already exists.

- Comment pulse
  - Google-owned but unofficial → Employees can publish OSS under google org; disclaimer avoids implying corporate support or roadmap.
  - More than a log viewer → Combines multi-source events into one, taggable timeline for collaborative breach analysis — counterpoint: feels like a glorified log UI.
  - Also helpful post-incident → Teams can reconstruct postmortem timelines with shared annotations.

- LLM perspective
  - View: Sits between SIEM search and spreadsheets; focused on multi-user, annotated timelines rather than alerting or ingestion at scale.
  - Impact: DFIR, SOC, and SRE teams gain faster incident reconstruction, shared context, and audit trails without heavyweight commercial tooling.
  - Watch next: Validate data connectors, RBAC, dedup, and performance; compare against ELK, Splunk, Velociraptor; track releases for notebook/API improvements.
