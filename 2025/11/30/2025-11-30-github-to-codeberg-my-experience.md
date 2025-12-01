# GitHub to Codeberg: my experience

- Score: 109 | [HN](https://news.ycombinator.com/item?id=46097829) | Link: https://eldred.fr/blog/forge-migration/

### TL;DR
A solo dev describes migrating ~45 repositories, CI, and a static website from GitHub to Codeberg in a weekend. Forgejo’s “migrate from GitHub” imported issues/PRs/wikis/releases; link and remote rewrites were scripted; GitHub repos were left as archived stubs pointing to Codeberg, preserving permalinks. Codeberg Actions required only light YAML tweaks, but runners are Linux-only and resource-limited, nudging leaner CI. For hosting, they replaced GitHub Pages with git-pages/Grebedoc, gaining zero-downtime deploys and server-side redirects. HN discussion centers on GitHub’s network effects, alternatives, and CI economics.

---

### Comment pulse
- GitHub’s advantage → social network, integrations, and documentation, not raw forge features—counterpoint: projects like Tangled aim to decouple social discovery from hosting.  
- Alternatives landscape → Forgejo/Codeberg, GitLab, SourceHut (including Mercurial), Gitea/Gogs, Phorge; but GitHub Actions’ free CI remains unmatched “bang for buck.”  
- Migration trend drivers → fatigue with GitHub outages and AI push, internal dysfunction rumors, plus high‑profile exits like Zig highlighting Codeberg as a viable home.

---

### LLM perspective
- View: Migration friction is now mostly social and CI-related, not technical; tooling parity is good enough for many workflows.  
- Impact: Small projects gain autonomy and philosophical alignment; large orgs still depend on GitHub’s ecosystem and CI scale.  
- Watch next: Federated identity for forges, sustainable/free CI funding models, and Codeberg’s eventual full rollout of git-pages.
