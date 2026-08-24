# Ex-GitHub CEO launches a new developer platform for AI agents

- Score: 272 | [HN](https://news.ycombinator.com/item?id=46961345) | Link: https://entire.io/blog/hello-entire-world/

### TL;DR

Thomas Dohmke’s company Entire raised a $60 million seed round to build infrastructure for human-agent software development. Its plan combines a Git-compatible database, semantic context graph, and redesigned lifecycle; its first open-source product is a Git-aware CLI. On agent-generated commits, Checkpoints stores transcripts, prompts, touched files, token use, and tool calls on a separate branch, initially supporting Claude Code and Gemini CLI. Commenters valued traceability, review, and handoffs but questioned whether context dumping creates noise, whether a familiar workflow needs venture-scale funding, and whether improving models will erase the opportunity.

### Comment pulse

- Agent provenance aids audits → preserved intent and constraints can explain why code changed and help later reviewers judge whether assumptions still hold.
- More context is not always better → raw transcripts may overload repositories and agents; curated design records can be more useful.
- Market size divides readers → technical utility looks clear — counterpoint: a $60 million seed implies an enterprise platform, not merely metadata storage.

### LLM perspective

- View: Checkpoints solves a real traceability gap; Entire’s larger bet depends on context becoming infrastructure rather than disposable exhaust.
- Impact: Teams gain reproducible agent histories, but must govern secrets, retention, repository growth, and which reasoning deserves preservation.
- Watch next: Codex and Cursor support, checkpoint size, privacy controls, review-time savings, agent reuse quality, enterprise mandates, and open-format adoption.
