# Potential issues in curl found using AI assisted tools

- Score: 412 | [HN](https://news.ycombinator.com/item?id=45449348) | Link: https://mastodon.social/@bagder/115241241075258997

- TL;DR
  - An engineer used AI-assisted security tooling to scan curl and propose fixes; maintainers accepted many resulting PRs. This contrasts with past floods of low-quality AI reports that curl banned. HN discusses a preferred role for AI: flag suspicious code and logic bugs, not write code. Experiences vary—some models/tools surface real issues, others regurgitate TODOs. Questions remain about the exact toolchain and why it outperformed conventional SAST; a retrospective is promised.
  - Content unavailable; summarizing from title/comments.

- Comment pulse
  - AI should review, not author → devs want hotspots and logic-bug hunts; static analyzers miss semantics — counterpoint: prompting and tools like BugBot can deliver.
  - Evidence-backed PRs earned trust → curl accepted dozens labeled “sarif data,” despite earlier banning AI slop that DDoS’d maintainers.
  - Not all findings are novel → some printf-specifier bugs are compiler-catchable; missing warning flags reduce signal.

- LLM perspective
  - View: Use LLMs to triage SAST output, dedupe, and draft minimal diffs with provenance.
  - Impact: Less maintainer triage, higher-signal PRs, broader adoption of strict compiler flags.
  - Watch next: Publish toolchain and metrics; compare precision/recall vs SAST; integrate SARIF+LLM checks into CI.
