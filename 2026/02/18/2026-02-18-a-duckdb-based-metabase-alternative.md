# A DuckDB-based metabase alternative

- Score: 160 | [HN](https://news.ycombinator.com/item?id=47057879) | Link: https://github.com/taleshape-com/shaper

### TL;DR

Shaper is an MPL-licensed, self-hosted analytics tool that turns SQL queries into DuckDB-powered dashboards. It treats dashboards as code and supports cross-source queries, Git workflows, white-label embedding without iframes, JWT row security, shareable links, scheduled alerts, and PDF, image, CSV, or Excel output. A Docker command provides the quick start; paid hosting and support are optional. Its developer describes it as a deliberately minimal alternative to Metabase, not a feature match: technical users define everything in SQL rather than using a broad self-service interface.

### Comment pulse

- People especially valued scheduled reports and direct customer data access over another product-specific dashboard.
- Read replicas empower sophisticated customers — counterpoint: transactional databases should not become warehouses, and multi-tenant authorization is difficult.
- Heavy Metabase users found the comparison overstated; Shaper’s author emphasized SQL-as-code productivity over nontechnical exploration.
