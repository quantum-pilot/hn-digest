# A DuckDB-based metabase alternative

- Score: 160 | [HN](https://news.ycombinator.com/item?id=47057879) | Link: https://github.com/taleshape-com/shaper

- TL;DR  
  Shaper is an open-source, self-hosted BI tool that uses DuckDB and pure SQL to define dashboards, charts, and embedded analytics. Instead of a GUI builder, every visual element is configured in queries, enabling git-based workflows and easy PDF/PNG/CSV/Excel export and scheduling. HN discussion focuses on reviving the idea of giving customers direct read access and push-based reports, how this compares to Metabase’s richer non-technical UX, and related tools like SQLPage or Metabase with a DuckDB driver.

- Comment pulse  
  - Expose read replicas and push reports, not complex dashboards → customers build analytics; tools like Shaper help — counterpoint: transactional DBs shouldn’t serve analytics.  
  - Shaper positions as SQL-as-code dashboards → great for engineers, git workflows, PDFs; Metabase remains better for rich, non-technical self-serve exploration.  
  - HN notes neighboring tools → SQLPage for general UIs; Metabase+DuckDB driver for BI; Definite building similar DuckDB-based “embedded lakehouse” offering.

- LLM perspective  
  - View: SQL-defined dashboards align with infra-as-code trends, improving reproducibility, reviews, and multi-environment promotion.  
  - Impact: Best fit for teams with SQL literacy and existing DuckDB stacks; less ideal where business users demand point-and-click authoring.  
  - Watch next: Worth tracking scheduled-report automation, embedded SDK ergonomics, and benchmarks against Metabase/Superset on real-world datasets and concurrency.
