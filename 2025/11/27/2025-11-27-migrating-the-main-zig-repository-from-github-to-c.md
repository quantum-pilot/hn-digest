# Migrating the main Zig repository from GitHub to Codeberg

- Score: 853 | [HN](https://news.ycombinator.com/item?id=46064571) | Link: https://ziglang.org/news/migrating-from-github-to-codeberg/

### TL;DR

Zig moved its canonical repository from GitHub to Codeberg, citing unreliable GitHub Actions, sluggish product quality, AI promotion conflicting with Zig’s no-LLM contribution policy, and ethical concerns. GitHub becomes read-only; existing issues and pull requests remain there until edits are needed, while Codeberg numbering starts at 30000 to avoid collisions. The foundation also asks donors to leave GitHub Sponsors for Every.org despite revenue risk. Commenters welcomed Forgejo support but questioned Codeberg infrastructure reliability, contributor visibility, self-hosting, and whether ethical migration can avoid imperfect dependencies.

### Comment pulse

- Technical motive → CI scheduling failures and limited intervention made GitHub operationally costly for Zig’s master branch.
- Community motive → Codeberg may reduce AI-generated submissions and offers direct help from Forgejo maintainers.
- Platform risk → limited redundancy and hardware concerns make mirrors prudent — counterpoint: no alternative needs moral or operational perfection.

### LLM perspective

- View: The migration converts dissatisfaction into leverage while deliberately limiting issue-history disruption.
- Impact: Zig trades GitHub reach and funding convenience for governance alignment and a smaller infrastructure provider.
- Watch next: Monitor Codeberg uptime, CI throughput, contribution volume, donation migration, issue continuity, and repository mirrors.
