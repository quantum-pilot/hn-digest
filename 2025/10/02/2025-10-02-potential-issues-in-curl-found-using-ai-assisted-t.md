# Potential issues in curl found using AI assisted tools

- Score: 358 | [HN](https://news.ycombinator.com/item?id=45449348) | Link: https://mastodon.social/@bagder/115241241075258997

- TL;DR
    - curl maintainers accepted a wave of fixes sourced from AI-assisted security/code-analysis tools (SARIF reports), a notable shift from prior “AI slop” floods. HN approves the tooling-first approach: use AI to surface suspicious code and logic bugs, not to auto-write patches. Contributors stress turning AI findings into deterministic scripts/linters in CI, and note some issues were catchable via better compiler flags. Quality varies; specialized agents, better prompts, and integrations like Cursor BugBot yielded useful, reviewable results.
    - Content unavailable; summarizing from title/comments.

- Comment pulse
    - AI as reviewer, not author → Flags suspicious logic paths faster than humans; better when embedded in tools (Cursor BugBot) vs chatbots.
    - Convert probabilistic AI hints into deterministic scripts → Commit linters with file/line and exit codes; CI keeps regressions out — counterpoint: many findings are compiler-flaggable.
    - Evidence of value in curl → ~55 PRs citing SARIF data accepted; notable shift after past “AI slop” flood at HackerOne.

- LLM perspective
    - View: Codify AI discoveries as rules emitting SARIF; prioritize building detectors over accepting model-authored diffs.
    - Impact: Repository hygiene improves via permanent checks; security triage shifts from inbox links to actionable, reproducible findings.
    - Watch next: Benchmark AI+SAST pipelines on real repos: precision/recall, fix time saved, CI cost; track false-positive rates versus compiler warnings.
