# How we rebuilt Next.js with AI in one week

- Score: 301 | [HN](https://news.ycombinator.com/item?id=47142156) | Link: https://blog.cloudflare.com/vinext/

### TL;DR

Cloudflare’s experimental vinext reimplements 94% of the Next.js 16 API on Vite, targeting Workers first. One engineer directed AI through more than 800 sessions over one week for about $1,100, backed by 1,700 Vitest and 380 Playwright tests. On one 33-route fixture, Vite 8/Rolldown built 4.4 times faster and produced a 57% smaller client bundle than Next.js; serving performance was not tested. Static build-time prerendering remains absent. HN found the result impressive but questioned untested edge cases and whether cloning well-documented APIs and public tests weakens open-source incentives.

### Comment pulse

- AI excelled because the target was unusually legible → extensive documentation, public tests, and Vite’s RSC foundation supplied specification and scaffolding.
- Passing imported tests may miss behavioral equivalence → commenters found implementations far smaller and sometimes structurally unlike Next.js.
- Open specifications enable competition → counterpoint: maintainers may hide tests if documentation makes mature projects cheap to clone.

### LLM perspective

- **View:** This demonstrates accelerated compatibility engineering, not a general one-week recipe for mature frameworks.
- **Impact:** Hosting providers gain leverage while framework authors face faster API-level competition.
- **Watch next:** Production traffic, API coverage, static prerendering, non-Cloudflare targets, maintenance cost, and independent benchmarks.
