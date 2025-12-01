# Migrating Dillo from GitHub

- Score: 249 | [HN](https://news.ycombinator.com/item?id=46096800) | Link: https://dillo-browser.org/news/migration-from-github/

### TL;DR
The Dillo browser maintainer is moving the project off GitHub to a lean, self-hosted setup that Dillo can actually browse and that avoids centralized control. Complaints include GitHub’s JS-heavy UI, dependence on always-on connectivity, weak moderation for non-technical users, push-style notification culture, and its role in AI-driven web bloat. Instead, Dillo now runs on a tiny VPS using cgit, a custom git-backed static bug tracker, OpenPGP-signed releases, and mirrors on other forges to reduce lock‑in and data-loss risk.

### Comment pulse
- Forgejo/Gitea preferred over GitLab for self-hosting → single-binary Go services, low RAM, trivial upgrades; good CI integration—counterpoint: some solo devs prefer plain git+SSH only.  
- Push-model notifications seen as distracting → email-based workflows let maintainers pull patches on their schedule and work offline—counterpoint: GitHub filters already make notifications mostly pull-based.  
- Many expect a GitHub diaspora → competition among forges may yield federated, decentralized collaboration instead of a dominant replacement, trading convenience for autonomy and resilience.  

### LLM perspective
- View: This migration exemplifies small projects optimizing tooling for their own constraints rather than bending to mainstream platforms’ assumptions.  
- Impact: Encourages more git-backed, text-first workflows and could normalize static bug trackers, PGP-signing, and mirrors as basic project hygiene.  
- Watch next: Whether forge federation standards, issue-sync tools, and lightweight CI runners emerge to make multi-home hosting practical for maintainers.
