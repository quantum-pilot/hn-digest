# The Theatre of Pull Requests and Code Review

- Score: 208 | [HN](https://news.ycombinator.com/item?id=45371283) | Link: https://meks.quest/blogs/the-theatre-of-pull-requests-and-code-review

- TL;DR
    - Saša Jurić argues reviews fail when PRs are big and incoherent. He recommends returning unreadable PRs, targeting 5–10‑minute reviews (~300 LOC), and crafting narrative commits with clean, compilable history (via fixup/rebase) to speed feedback and enable bisect-friendly debugging. HN split: skeptics call commit narratives and size caps performative or unworkable for large features; supporters say small, stacked PRs plus context and self‑review improve quality and velocity, especially in distributed/open-source teams.

- Comment pulse
    - Small, narrated PRs improve review and debugging → commit-level stories aid blame/bisect; stacks/tools mitigate overhead — counterpoint: feels like theater; nobody reads commits; slows delivery.
    - Prefer feature-sized PRs reviewed for final state → splitting loses coherence; reviewers miss architecture; multiple branches cause conflicts.
    - Make reviews targeted and contextual → require self-review, questions, and code comments; discuss design earlier; PRs optional for trusted changes.

- LLM perspective
    - View: Treat PRs as communication artifacts; size by reviewability, not lines; preserve narrative only when it aids future debugging.
    - Impact: Adopting commit stories and stacks shifts workflows: more self-review, staged merges, and better regression isolation.
    - Watch next: Tooling that supports PR stacks and commit-by-commit review; org policies on optional PRs; empirical studies on review time vs defects.
