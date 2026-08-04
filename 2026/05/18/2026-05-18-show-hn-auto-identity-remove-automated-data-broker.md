# Show HN: Auto-identity-remove – Automated data broker opt-out runner for macOS

- Score: 314 | [HN](https://news.ycombinator.com/item?id=48178184) | Link: https://github.com/stephenlthorn/auto-identity-remove

### TL;DR

Auto Identity Remove is an MIT-licensed Node/Playwright runner that schedules monthly opt-out attempts across 500-plus data brokers, stores personal details locally, tracks successful submissions for 90 days, solves optional CAPTCHAs, and opens manual cases in a browser. Its coverage is uneven: roughly 31 brokers have explicit mappings, while about 490 use generic heuristics that may fail silently, and submission does not prove deletion. HN’s Canadian test found 404s, Apple-specific email assumptions, signup prompts, and extensive manual work, reinforcing the author’s request for verification and cross-platform help.

### Comment pulse

- International support remains brittle → a Canadian user encountered nonnumeric postal-code problems, dead URLs, Apple Mail assumptions, account creation, and many manual steps.

- Automation quality is hard to assess → commenters suspected heavy AI generation — counterpoint: contributors can validate flows and add explicit broker mappings.

- Individual automation treats symptoms → commenters preferred laws restricting mass collection and resale, while noting GDPR supplies stronger legal leverage.

### LLM perspective

- **View:** Privacy automation is adversarial maintenance, not a one-time script; broker forms, selectors, verification steps, and datasets continuously decay.

- **Impact:** Users trade subscription fees for operational burden, false-success risk, and exposure from repeatedly submitting identity data.

- **Watch next:** Track live success rates by broker, independent deletion checks, non-US tests, email-confirmation handling, and selector-maintenance cadence.
