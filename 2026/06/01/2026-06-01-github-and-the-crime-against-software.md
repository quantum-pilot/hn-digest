# GitHub and the crime against software

- Score: 186 | [HN](https://news.ycombinator.com/item?id=48361064) | Link: https://eblog.fly.dev/githubbad.html

## TL;DR

The article argues GitHub has become a case study in infrastructural decay: frequent incidents, misleading uptime claims, and prioritizing Copilot/“agentic” AI features over reliability and performance. The author measures GitHub, GitLab, and Codeberg with throttled-network tests, HAR analysis, heap snapshots, and PageSpeed. GitHub ships ~15–22 MiB, hundreds of assets, and ~70–150 MiB RAM usage for simple pages—graded F versus GitLab (D+), Codeberg (C+), and the author’s own lean site (A–). Conclusion: big-tech forges are wasteful and user-hostile; diversify or self-host.

---

## Comment pulse

- Mirror repos across GitHub, GitLab, Codeberg → trivial via multiple push URLs; real lock‑in is issues, PRs, CI, and accumulated workflow metadata.  
- Self‑hosted forges (Gitea, Forgejo, Tailnet‑exposed Mac mini) → users report feeling “free,” using GitHub only when employers demand it.  
- GitHub stars create platform lock‑in → stars influence adoption and can be bought, giving GitHub social capital control—counterpoint: some moves (e.g., nginx) were mainly about Git vs Mercurial.

---

## LLM perspective

- View: There’s room for lightweight, opinionated forges that treat AI as optional, not the navigation center of the UI.  
- Impact: Teams with strict latency/bandwidth constraints, regulated environments, or long-lived projects benefit most from migrating or self-hosting.  
- Watch next: Tools that export/import issues, PRs, and stars between forges could meaningfully erode GitHub’s practical lock‑in.
