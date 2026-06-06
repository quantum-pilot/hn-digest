# We stopped AI bot spam in our GitHub repo using Git's –author flag

- Score: 386 | [HN](https://news.ycombinator.com/item?id=48181125) | Link: https://archestra.ai/blog/only-responsible-ai

- TL;DR
    - Archestra’s open-source repo was flooded by AI-generated comments and untested PRs, especially on bounty issues, burying real contributors and consuming maintainer time. After failed reputation bots and AI detectors, they used GitHub’s “limit to prior contributors” plus a workaround: an external onboarding form that, via GitHub Actions and git --author, adds vetted users as commit authors on main, whitelisting them. The post argues platforms over-count AI “activity” while offloading spam, morale, and security costs onto maintainers.

- Comment pulse
    - Whitelisting via “prior contributor” and fabricated --author commits may expand trust surface; some see real security risk, others call it existing GitHub weakness.
    - Many blame GitHub/Microsoft for enabling AI PR spam, wanting platform-level throttling, approvals-for-all-externals, and PR archiving or deletion instead of project-specific hacks.
    - Proposed reputation or Elo-style scoring to rank contributors and throttle low-quality activity—counterpoint: any gameable metric will be exploited by bots and determined trolls.

- LLM perspective
    - View: Treat AI-generated contributions as untrusted by default; require human friction (onboarding, CAPTCHAs, review) before granting repo interaction rights.
    - Impact: Maintainers gain signal amidst noise but pay overhead maintaining whitelists and automations; casual drive-by contributions become rarer.
    - Watch next: Native GitHub controls for AI spam, contributor-rate limits, and ecosystem-wide reputation systems that are transparent, auditable, and abuse-resistant.
