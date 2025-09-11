# Claude now has access to a server-side container environment

- Score: 645 | [HN](https://news.ycombinator.com/item?id=45182381) | Link: https://www.anthropic.com/news/create-files

TL;DR
Anthropic added an “Upgraded file creation and analysis” preview that lets Claude generate Excel, documents, slides, and PDFs by running code in a private server-side environment. Reverse-engineering indicates a sandboxed Linux container with restricted outbound networking via a proxy and domain allowlists. Enabling it replaces the older browser-based Analysis tool; mobile support is inconsistent. HN reports highlight artifact-editing glitches and recent slowdowns/throttling, while some praise remains. Users also note data-exposure risks from internet-enabled processing and confusing, non–Code-Interpreter naming.

Comment pulse
- Code Interpreter-style container → Reverse-engineering found Ubuntu 24.04, Python 3.12, Node 18, gVisor, ~9GB RAM; Envoy proxy allowlists GitHub/PyPI/npm, blocks arbitrary HTTP(S).
- Tool conflicts and naming confusion → Enabling it disables older JS Analysis; iOS support spotty; Version Control targets GitHub only—counterpoint: simpler branding helps non-tech users.
- Reliability and speed issues → Artifacts edits get “stuck”, version history breaks; many report slowdowns/throttling even on paid plans—counterpoint: some users see steady performance.

LLM perspective
- View: This formalizes agentic, code-running workflows for office tasks, trading capability for tight network control and server-side execution.
- Impact: Analysts/PMs offload spreadsheet/report building; security teams revisit approval processes for proxyed execution and storage integrations (e.g., Google Drive).
- Watch next: Compare output quality, speed, and reliability vs ChatGPT Code Interpreter; track allowlist/API expansion, mobile parity, and GitLab/other VCS support.
