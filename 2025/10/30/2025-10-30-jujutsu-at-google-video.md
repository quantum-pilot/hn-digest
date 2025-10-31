# Jujutsu at Google [video]

- Score: 117 | [HN](https://news.ycombinator.com/item?id=45759572) | Link: https://www.youtube.com/watch?v=v9Ob5yPpC0A

- TL;DR
    - A Google talk showcases Jujutsu (JJ), a Git‑compatible VCS emphasizing a simpler model and conflict handling. Commenters praise first‑class conflicts, auto‑snapshotted changes, no staging area, clean commit splitting, and easier “commit surgery” for stacked changes/rebases. Fans report gains with trunk‑based workflows and occasional serverless sharing; skeptics say Git + IDEs are already sufficient. Some meta‑debate on presentation style. The video seems unlisted in the JJ Con playlist, prompting questions about distribution.
    - Content unavailable; summarizing from title/comments.

- Comment pulse
    - Conflicts-as-state and auto-snapshots simplify work-in-progress → switch branches without stashing; split edits cleanly; commit chains stay logical during rebases.
    - Fits trunk-based development with stacked reviews → remove staging area and stash; bounce between top-of-stack work and reviewer edits without WIP commits.
    - Git is already simple with GUIs/IDEs → most devs need few commands — counterpoint: Git rebase conflict handling is awkward; JJ’s model reduces context switching.

- LLM perspective
    - View: JJ optimizes developer flow, not storage; strongest value in conflict management and stacked-change editing over time.
    - Impact: Adoption easiest where Git compatibility suffices locally; organizational shift depends on CI/CD, code review, and training aligning with JJ.
    - Watch next: Official GitHub/GitLab integrations, JetBrains/VS Code plugins, metrics comparing rebase-conflict resolution time and error rates on large repos.
