# Jeffgeerling.com has been migrated to Hugo

- Score: 205 | [HN](https://news.ycombinator.com/item?id=46487498) | Link: https://www.jeffgeerling.com/blog/2026/migrated-to-hugo/

### TL;DR

After running Drupal since 2009 through versions 6–10, Jeff Geerling migrated more than 3,500 posts to Hugo. Drupal’s enterprise-oriented stack, repeated upgrade churn, module maintenance, image uploads, cache purges, and duplicated Markdown publishing steps had overwhelmed a personal blog. Hugo aligns publishing with his existing Markdown workflow and reduces the runtime surface, though redirects, broken media, search, and self-hosted comments remain unfinished. Commenters supported simpler static publishing but warned that customized themes and generator upgrades can recreate maintenance unless versions and build environments are pinned.

### Comment pulse

- Custom generators offer complete understanding and tailored features—counterpoint: tinkering can consume the time supposedly recovered for writing.
- Hugo users recommended pinning or archiving a known-good binary because template changes can break neglected themes years later.
- Static pages minimize read-path cost and attack surface, while comments and search can remain small, separately operated services.

### LLM perspective

- View: The migration succeeds because content was already Markdown; Hugo removes translation steps rather than introducing a new authoring model.
- Impact: Publishing becomes cheaper and more reproducible, but the owner assumes responsibility for redirects, builds, search, and community features.
- Watch next: Audit legacy URLs and images, freeze tool versions, restore search, and evaluate the self-hosted comment system.
