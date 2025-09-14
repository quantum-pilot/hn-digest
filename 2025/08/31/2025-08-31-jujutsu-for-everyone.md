# Jujutsu for everyone

- Score: 442 | [HN](https://news.ycombinator.com/item?id=45083952) | Link: https://jj-for-everyone.github.io/

- TL;DR
  - This tutorial introduces Jujutsu (jj), a Git‑compatible VCS aimed at beginners: simpler commands, powerful history editing, and a path to grow without Git’s UI quirks. It acknowledges some downsides (immature CLI, occasional gaps vs Git) but argues benefits outweigh them. HN asks for concrete “power” examples; users cite effortless editing of earlier commits with automatic rebases, Mercurial‑style revsets, and first‑class conflicts. Praise centers on consistent primitives and jjui; concerns note Git LFS and light‑clone gaps, bookmark/branch friction, and a few safety/stability gotchas.

- Comment pulse
  - jj simplifies complex history editing → edit earlier commits; descendants auto-rebase; revsets DSL; first-class conflicts aid workflows — counterpoint: readers want concrete, side-by-side examples.
  - Git compatibility with rough edges → no LFS; tags/submodules uneven; light-clone co-location missing; bookmarks vs branches complicate shared-branch 'tug' workflow.
  - Safety/reliability concerns → stale workspaces sometimes drop changes; time-traveling before .gitignore caused secret to be tracked and pushed.

- LLM perspective
  - View: jj is viable for daily Git-backed workflows, but guardrails and missing integrations limit frictionless team adoption today.
  - Impact: Best fit: individual contributors, small teams, or Git power-users wanting safer, faster history surgery without Git’s UI overhead.
  - Watch next: Track LFS support, bookmark/branch UX, light-clone co-location, workspace-stability fixes, and jjui maturation; compare rebasing/conflict-resolution time vs Git in user studies.
