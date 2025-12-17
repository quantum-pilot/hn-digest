# Pricing Changes for GitHub Actions

- Score: 439 | [HN](https://news.ycombinator.com/item?id=46291156) | Link: https://resources.github.com/actions/2026-pricing-changes-for-github-actions/

### TL;DR
GitHub is restructuring Actions pricing: from Jan 1, 2026, GitHub‑hosted runners get up to ~39% cheaper per‑minute rates, but from Mar 1, 2026 a new $0.002/min “cloud platform” fee applies to all Actions workflows, including self‑hosted runners on private repos. Public repos and GitHub Enterprise Server remain free for Actions minutes. GitHub claims 96% of customers see no bill change and most affected pay only slightly more, while funding scaling work and new self‑hosted features—but HN sees lock‑in and rent‑seeking and is eyeing alternatives.

---

### Comment pulse
- Charging for self‑hosted → feels like “paying to use my own hardware” atop an unstable, awkward product (fragile workflows, weak Kubernetes story, broken multi‑label, bad logging) — counterpoint: some report runner software itself is solid; platform/workflow design is the real problem.  

- Strategy concern → $0.002/min equals smallest hosted runner, nudging users to GitHub‑hosted/Azure and blocking cheap third‑party runners; compared to Netflix‑style “we’ve saturated the market, now squeeze”.

- Exit mindset → several teams say new fees are their trigger to migrate CI to Jenkins, Forgejo+Woodpecker, or GitLab, accepting some DIY jank over per‑minute platform charges.

---

### LLM perspective
- View: This is a classic SaaS maturation move: rebalance costs from “free” heavy users to paid usage, at the cost of goodwill and trust.

- Impact: Heavy private, self‑hosted Actions users and third‑party runner providers are most exposed; hobbyists and public OSS projects remain mostly insulated.

- Watch next: Whether GitHub pairs this with real SLAs, major Actions UX fixes, or further price shifts—and if migration to lighter self‑hosted CI accelerates.
