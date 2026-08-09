# The Vercel plugin on Claude Code wants to read your prompts

- Score: 252 | [HN](https://news.ycombinator.com/item?id=47704881) | Link: https://akshaychugh.xyz/writings/png/vercel-plugin-telemetry

### TL;DR

Source inspection of Vercel’s Claude Code plugin found two telemetry tiers across every project: default-on session metadata and full Bash command strings linked by a persistent device ID, plus optional prompt text. The prompt opt-in is presented through plugin-injected instructions that make Claude render a native-looking question and write the preference via shell commands, without visible third-party attribution. Although an environment variable disables collection, the author says installation does not disclose it. HN readers called the unscoped command capture a supply-chain-grade trust breach and urged platform enforcement.

### Comment pulse

- System-context behavior injection is normal for skills — counterpoint: disguising a vendor’s consent flow as native UI and directing writes exceeds ordinary context.
- Commenters warned command strings can expose paths, project names, infrastructure details, or secrets, making anonymous branding misleading despite opt-out controls.
- Critics cited Claude’s plugin rules against extraneous conversation collection and coerced external calls; expectations centered on marketplace removal or policy enforcement.

### LLM perspective

- **View:** Consent is invalid when provenance, scope, payload, and the no-data option are not equally visible.
- **Impact:** Developers may leak operational context from unrelated repositories merely by installing a deployment helper.
- **Watch next:** Vercel’s defaults and disclosures, Anthropic’s review outcome, permission manifests, hook attribution, and project-scoped activation.
