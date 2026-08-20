# AI-Generated GitHub Copilot “Autofix” Allowed Compromise of Snowflake's Jira

- Score: 424 | [HN](https://news.ycombinator.com/item?id=49331423) | Link: https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug

### TL;DR

Wiz’s autonomous Red Agent found a critical script injection in Snowflake’s public GitHub Actions workflow five days after deployment. Any user could place shell syntax in an issue title, execute commands on the runner, and expose a Jira token with broad read access; an ineffective condition admitted every issue. Snowflake patched the workflow and rotated credentials, with audits finding only Wiz access. Despite the headline, the vulnerable edit is not established as AI-generated: Copilot’s documented change was separate, while Copilot and GitHub Advanced Security failed to flag it.

### Comment pulse

- Dedicated linting would catch direct template expansion → commenters recommended environment variables, zizmor, and shellcheck instead of interpolating untrusted text.
- AI makes low-value refactors cheap → review and maintenance remain costly, so backlog completion can create disproportionate risk.
- AI was blamed for false assurance → counterpoint: supplied evidence does not show Copilot authored the vulnerable edit.

### LLM perspective

- View: The failure was layered governance, not singular authorship: unsafe interpolation, a fail-open guard, review gaps, and missed scanning.
- Impact: Public CI workflows need untrusted-input threat models, short-lived credentials, and mandatory specialized linting before merge.
- Watch next: Confirm provenance of the vulnerable edit and add regression rules for event-context nulls and template injection.
