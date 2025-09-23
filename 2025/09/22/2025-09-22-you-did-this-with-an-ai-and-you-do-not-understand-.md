# You did this with an AI and you do not understand what you're doing here

- Score: 982 | [HN](https://news.ycombinator.com/item?id=45330378) | Link: https://hackerone.com/reports/3340109

- TL;DR
  - A HackerOne report claimed a critical libcurl cookie-parser RCE with ASan logs and a “PoC,” but the code never called curl. Maintainer Daniel Stenberg flagged it; the reporter retracted, the report was closed as Not Applicable, the account banned, and the thread disclosed for transparency. HN sees it as AI-generated slop creeping into security reports/PRs, wasting maintainers’ time. Commenters emphasize human-in-the-loop responsibility, but warn that reflexively labeling content “AI” can become a lazy dismissal, prompting frustration and gallows humor.

- Comment pulse
  - AI slop is flooding OSS triage → obvious template-y language, fake PoCs, and copy‑pasted jargon consume scarce maintainer time.
  - Use AI, but own the output → human-in-the-loop must validate, run PoCs against real code, and take responsibility before filing.
  - Spotting AI is getting easier → formulaic tone and errors give it away — counterpoint: overusing “that’s AI” can dismiss legitimate reports.

- LLM perspective
  - View: Require reproducible, code-path PoCs and exact file/line references; auto-close reports lacking minimal evidence.
  - Impact: Maintainers regain time; frivolous AI submissions drop; serious reporters adapt workflows to provide verifiable artifacts.
  - Watch next: HackerOne/GitHub add AI-detection and templates; curated queues; penalties for spam; benchmarks for “AI-assisted but validated” submissions.
