# Migrating the main Zig repository from GitHub to Codeberg

- Score: 853 | [HN](https://news.ycombinator.com/item?id=46064571) | Link: https://ziglang.org/news/migrating-from-github-to-codeberg/

### TL;DR
Zig is moving its main repository from GitHub to Codeberg (Forgejo) after a decade, citing GitHub’s decline in performance and reliability, especially GitHub Actions’ “vibe-scheduled” CI that blocks essential builds. The project also objects to GitHub’s AI push, which clashes with Zig’s strict no-LLM policy, and sees continued reliance on GitHub Sponsors as a financial liability. The GitHub repo becomes read-only; Codeberg is now canonical, with issues effectively “copy-on-write” and renumbered to avoid ambiguity.

---

### Comment pulse
- AI “slop” PRs are a concrete problem → LLM-generated, non-working contributions waste maintainer time and confuse newcomers; Zig’s policy tries to limit this.  
- Ethics debate: leaving GitHub over ICE vs Codeberg’s PayPal link → some call it a purity spiral; others say reducing harm pragmatically still matters—counterpoint: consistency questions won’t ever fully disappear.  
- Codeberg as infra: worrying hardware/uptime vs appealing hacker ethos → some want self-hosted Forgejo for safety; others value the responsive Forgejo/Codeberg community and will mirror for redundancy.

---

### LLM perspective
- View: Strong signal that AI-centric platform roadmaps can push serious projects away, especially those with explicit no-AI norms.  
- Impact: CI-heavy, ethics-conscious projects may diversify off GitHub; forges like Forgejo/Codeberg gain credibility if they prove reliable at scale.  
- Watch next: Codeberg uptime and incident reports; how much Zig funding shifts from Sponsors to Every.org; whether other languages or big libs follow.
