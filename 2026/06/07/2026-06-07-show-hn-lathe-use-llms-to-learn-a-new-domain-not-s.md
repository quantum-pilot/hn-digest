# Show HN: Lathe – Use LLMs to learn a new domain, not skip past it

- Score: 223 | [HN](https://news.ycombinator.com/item?id=48433756) | Link: https://github.com/devenjarvis/lathe

## TL;DR
Lathe is a Go-based CLI and local web UI that turns LLMs into on-demand authors of multi-part, hands-on technical tutorials. You invoke skills (e.g., `/lathe`) inside Claude Code/Cursor/Codex; the CLI stores tutorials, serves a focused reader, tracks sources, and optionally verifies code in a scratch directory. The design emphasizes learning by manually typing and debugging code, with “voices” for tone but strict provenance and authorship labeling. HN discussion centers on LLMs as tutors, not code generators, and hybrid CLI–agent workflows for repeatable knowledge work.

---

## Comment pulse
- LLM Socratic / grilling skills → continuous quizzing forces recall and reasoning, improving retention in complex domains like physiology and internals.
- Hybrid pattern praise → deterministic CLI for state and IO, LLM skills for reasoning; some want the inverse (CLI-first with pluggable local agent daemon).
- Typing code as practice → copying working examples builds fluency fast, echoing language Input Hypothesis; — counterpoint: AI makes “average” content easy, but tasteful, deep courses still require human effort.

---

## LLM perspective
- View: Lathe operationalizes “LLM as personalized textbook generator,” with UI and workflows tuned for deliberate practice instead of instant solutions.
- Impact: Best suited for motivated learners in niche/young domains lacking good tutorials, and for teams prototyping agent–tool architectures.
- Watch next: Libraries/daemons exposing standard agent IPC to CLIs, plus empirical studies comparing Lathe-style learning vs curated human tutorials.
