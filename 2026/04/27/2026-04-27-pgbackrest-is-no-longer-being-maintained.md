# Pgbackrest is no longer being maintained

- Score: 391 | [HN](https://news.ycombinator.com/item?id=47919997) | Link: https://github.com/pgbackrest/pgbackrest

- TL;DR  
  pgBackRest, a widely-used backup/restore tool for PostgreSQL, has been declared obsolete by its creator after 13 years. Following Crunchy Data’s sale, he couldn’t find a job or sponsorship that funded ongoing maintenance at a sustainable level, and chose a hard stop rather than sporadic support. The code remains under open-source license and may be forked, but users now face uncertainty over long‑term maintenance. HN discussion centers on open‑source sustainability, funding responsibilities, and hidden corporate risk in critical tooling.

- Comment pulse  
  - Sustainability requires money → users should donate, buy support, or fork instead of expressing sadness—counterpoint: monetizing licensing is legally and socially complex for multi-contributor projects.  
  - Many users are grateful yet worried → see this as emblematic of OSS burnout, AI-driven deadline pressure, and vital infrastructure relying on unpaid nights/weekends.  
  - Crunchy Data acquisition stands out → one sponsor’s M&A shift can imperil core tooling, pushing some engineers toward simpler stacks like SQLite plus file-based backups.

- LLM perspective  
  - View: This illustrates how single-maintainer projects underpin serious production systems; treat them as vendors, not free background magic.  
  - Impact: Teams using pgBackRest should evaluate alternatives, or coordinate a maintained fork with clear governance, funding, and support expectations.  
  - Watch next: Whether hyperscalers or Postgres vendors adopt, fork, or replace pgBackRest will signal how industry values low-level infrastructure projects.
