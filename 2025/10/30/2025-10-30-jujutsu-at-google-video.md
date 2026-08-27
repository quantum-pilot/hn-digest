# Jujutsu at Google [video]

- Score: 117 | [HN](https://news.ycombinator.com/item?id=45759572) | Link: https://www.youtube.com/watch?v=v9Ob5yPpC0A

### TL;DR

The supplied video description presents Jujutsu, or JJ, as an open-source, Git-compatible version-control system and says its architecture and future plans were discussed at Google's JJ Con 2025. Without a transcript, the technical substance comes mainly from commenters: they value automatic working-copy snapshots, no separate staging index, editable commit stacks, `jj split`, and conflicts represented as persistent first-class state. Others find ordinary Git workflows adequate and question whether JJ's advantages justify another tool for teams with simpler histories.

### Comment pulse

- JJ users reported smoother trunk-based work, stacked changes, review revisions, and fewer stash-or-WIP-commit interruptions.
- Git users said a small command set plus IDE history and conflict tools already handles large-team work effectively.

### LLM perspective

- View: JJ's value appears strongest for change-stack surgery and interrupted work, not for every Git user.
- Impact: Teams matching that workflow may reduce context switching while accepting migration and interoperability learning costs.
- Watch next: Evaluate repository scale, collaboration behavior, Git compatibility, conflict workflows, and onboarding in real teams.
