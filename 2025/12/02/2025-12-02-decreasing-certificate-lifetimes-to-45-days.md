# Decreasing Certificate Lifetimes to 45 Days

- Score: 148 | [HN](https://news.ycombinator.com/item?id=46117126) | Link: https://letsencrypt.org/2025/12/02/from-90-to-45.html

### TL;DR

Let’s Encrypt will reduce certificate validity from 90 to 45 days by 2028 under industry requirements, while shrinking domain-authorization reuse from 30 days to seven hours. An opt-in 45-day profile arrives May 2026; the default moves to 64 days in February 2027 and 45 days in February 2028. Automated users should verify renewal schedules, adopt ACME Renewal Information, and monitor failures. Commenters largely favored automation, while highlighting legacy systems, certificate pinning, and operational fragility; DNS-PERSIST-01 drew particular interest.

### Comment pulse

- Automation supporters → shorter lifetimes limit compromise and make manual certificate handling untenable.
- Operations skeptics → brittle enterprise integrations can renew incorrectly or require restarts, turning frequency into outage risk.
- DNS-PERSIST-01 enthusiasm → one persistent DNS record could automate validation without distributing zone-edit credentials.

### LLM perspective

- View: Short lifetimes convert certificate renewal from maintenance practice into required infrastructure.
- Impact: Reliable ACME clients and monitoring become mandatory, especially for legacy fleets and pinned applications.
- Watch next: Test ARI support, renewal alarms, DNS-PERSIST-01 standardization, and behavior before each staged cutoff.
