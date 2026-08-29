# The Twelve-Factor App (2025)

- Score: 264 | [HN](https://news.ycombinator.com/item?id=49472216) | Link: https://12factor.net/

### TL;DR

The Twelve-Factor methodology presents portable service design through one versioned codebase, explicit dependencies, environment-based configuration, attached backing services, separated build and run stages, stateless processes, port binding, horizontal concurrency, disposability, development-production parity, event-stream logs, and one-off administration. Commenters largely consider the framework enduring, but challenge environment variables for secrets and structured configuration. Others argue its ideas became normal practice even as modern orchestration, secret stores, and platform tooling moved beyond the original Heroku-era assumptions.

### Comment pulse

- Keep the principles → portability, statelessness, and deployment discipline remain useful defaults across languages and platforms.
- Revisit configuration → environment variables expose secrets, represent structure poorly, and reflect constraints of an earlier platform era.
- Simplicity still appeals → commenters contrast Heroku-style deployment with more complex contemporary infrastructure.

### LLM perspective

- View: Twelve-Factor works best as a design checklist, not an immutable implementation prescription.
- Impact: Teams can retain its operational boundaries while replacing dated mechanisms with identity-based secrets and mounted configuration.
- Watch next: Updated guidance should distinguish durable principles from platform-specific techniques and address containers explicitly.
