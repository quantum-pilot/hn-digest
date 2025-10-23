# I see a future in jj

- Score: 191 | [HN](https://news.ycombinator.com/item?id=45672280) | Link: https://steveklabnik.com/writing/i-see-a-future-in-jj/

- TL;DR
  - Steve Klabnik argues jj (Jujutsu) has Rust-like momentum: Git-compatible for incremental adoption, traction from individuals to Google-scale monorepos, and an experienced, welcoming team. He’s leaving Oxide to join ERSC to build collaboration tooling atop jj. Commenters focus on what a “jjhub” must deliver (stacked-diff review, offline-first workflows), whether Google’s uptake signals durable viability amid internal churn, and industry needs beyond Git’s comfort zone (e.g., large binaries/Perforce). jj recently formalized governance and has a passionate early community; Klabnik’s popular tutorial reflects that momentum.

- Comment pulse
  - ERSC “jjhub” needed → stacked-diff review and integration beyond GitHub; Gerrit aligns via change IDs; offline-first workflows requested.
  - Google uptake shows scale viability → jj atop Piper; Perforce fork may be deprecated — counterpoint: Google frequently churns internal VCS tools.
  - GitHub today limits jj benefits → change IDs don't help PRs; jj-spr helps; GitHub SVP exploring stacked diffs.

- LLM perspective
  - View: Edge: stacked-change model with Git interoperability; success hinges on integrated review/CI UX.
  - Impact: Could normalize stack-based workflows outside Meta/Google; pressures GitHub/GitLab to support change IDs and non-linear review.
  - Watch next: ERSC alpha, Gerrit change-ID rollout, GitHub stacked-diff experiments, large-binary strategy beyond LFS.
