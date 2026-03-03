# If AI writes code, should the session be part of the commit?

- Score: 460 | [HN](https://news.ycombinator.com/item?id=47212355) | Link: https://github.com/mandel-macaque/memento

### TL;DR
Memento is a Git tool and GitHub Action that records AI-assisted coding sessions alongside commits using git notes. It can store a concise, LLM-generated summary in the main notes stream and keep full transcripts in a separate audit ref, with CI gates and merge propagation. HN discussion centers on what should actually be preserved: raw sessions, distilled specs/plans, or just polished docs. Trade-offs include readability, repository noise, reproducibility, future AI analysis, and how AI-coded projects should be presented publicly.

---

### Comment pulse
- Spec/plan/debug markdown workflows → Many engineers co-create detailed design/plan files with AI and sometimes commit them as a living architecture lexicon for future humans/LLMs.  
- What to save → Some favor only specs and summaries; others want full sessions for audit, debugging, and scientific-style reproducibility — counterpoint: transcripts are noisy and hard to trust.  
- Community impact → AI-generated repos are flooding Show HN; proposals include stricter Show HN gating and requiring process commentary, not just vibe-coded code drops.

---

### LLM perspective
- View: Separate artifacts: concise, curated intent/plan docs in-tree; full AI sessions stored as optional, queryable history or external archive.  
- Impact: Helps teams audit AI changes, debug intent, and bootstrap future agents without overwhelming everyday readers or bloating main branches.  
- Watch next: Standard formats for agent traces, git-note conventions, and IDE/Git integrations that auto-summarize and attach sessions with privacy controls.
