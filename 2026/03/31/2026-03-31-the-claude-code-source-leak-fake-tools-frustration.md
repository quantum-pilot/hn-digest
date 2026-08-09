# The Claude Code Source Leak: fake tools, frustration regexes, undercover mode

- Score: 652 | [HN](https://news.ycombinator.com/item?id=47586778) | Link: https://alex000kim.com/posts/2026-03-31-claude-code-source-leak/

### TL;DR

An accidentally published Claude Code source map exposed the CLI’s readable source before Anthropic pulled the package. The author identifies feature-gated fake-tool injection and signed summaries meant to hinder distillation, native request attestation, regex-based frustration detection, and an unreleased always-on agent mode called KAIROS. Most controversially, an internal “undercover” prompt suppresses Claude attribution in public-repository commits and PRs. HN debated whether that protects internal details or obscures AI involvement, while broader concern centered on repeated leaks and trust in a tool with codebase access.

### Comment pulse

- One fork reportedly received a DMCA notice despite not containing leaked code, reinforcing claims Anthropic cannot contain the disclosure.
- Some reject automated co-author lines because humans retain accountability — counterpoint: explicit suppression may evade warranted scrutiny of AI-generated contributions.
- Operational comments make decisions legible to coding agents, readers argued, but also expose internal incidents and scale if source escapes.

### LLM perspective

- **View:** Roadmap secrecy matters less than provenance policy and secure artifact-release controls.
- **Impact:** Enterprise adopters must reassess supply-chain review, disclosure expectations, and confidence in vendor handling of proprietary repositories.
- **Watch next:** Root-cause report, package-pipeline fixes, attribution policy, DMCA scope, KAIROS release status, and server-side enforcement changes.
