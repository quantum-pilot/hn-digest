# Billing can be bypassed using a combo of subagents with an agent definition

- Score: 180 | [HN](https://news.ycombinator.com/item?id=46936105) | Link: https://github.com/microsoft/vscode/issues/292452

### TL;DR

A VS Code issue alleges Copilot bills only the initial model while nested calls add no premium requests. The reporter says a free-model orchestrator invoked an Opus-configured agent; one three-hour loop launched hundreds of Opus subagents for three credits. Microsoft’s security center deemed billing bypasses out of scope and directed public filing; automation closed the report against a meta-issue before a maintainer reopened and assigned it. The issue remains open. Commenters mocked the handling, challenged invocation pricing, and made conflicting, often sarcastic claims that the flaw was fixed.

### Comment pulse

- Client-side billing controls invite abuse → commenters said agent products place business logic and guardrails locally.
- Invocation pricing mismatches agent sessions → one request can fan into long, expensive workloads — counterpoint: token pricing creates different quality incentives.
- Disclosure routing failed conspicuously → security triage required public instructions, then automation misclassified and closed the distinct report.

### LLM perspective

- View: The alleged defect is an accounting-boundary mismatch: nested execution inherits neither premium-model cost nor enforceable server validation.
- Impact: Unmetered fan-out could impose provider costs, encourage abuse, and force pricing or agent-limit changes for legitimate users.
- Watch next: Maintainer confirmation, server-side metering, subagent caps, client-message validation, patched versions, retroactive billing, and public disclosure policy.
