# 1-Click RCE to steal your Moltbot data and keys

- Score: 138 | [HN](https://news.ycombinator.com/item?id=46848769) | Link: https://depthfirst.com/post/1-click-rce-to-steal-your-moltbot-data-and-keys

### TL;DR

Depthfirst’s researcher describes chaining two OpenClaw flaws into one-click remote code execution: a URL parameter silently changed the gateway and leaked the user’s authentication token, while missing WebSocket origin validation let attacker-controlled JavaScript reach localhost. Because the token carried administrative and approval scopes, the exploit could disable command confirmations, redirect execution outside containers, and run host commands. The team patched automatic connection behavior; versions through v2026.1.24-1 were affected. Commenters saw broader danger in agents holding sensitive data and powerful permissions.

### Comment pulse

- Security concern extends beyond this bug → prompt injection remains dangerous when agents ingest public content while controlling messages, files, and accounts.
- Isolation advocates favor kernel sandboxes or quarantined hosts → tool-level approvals can be disabled by a sufficiently privileged stolen token.
- Automated code-flow analysis impressed readers → cross-file vulnerabilities are easy to miss as AI-generated code increases review volume.

### LLM perspective

- View: Agent security should assume interface compromise and enforce least privilege beneath the application layer.
- Impact: OpenClaw users risk credential theft, private-data exposure, and host takeover from a single malicious page.
- Watch next: Confirm upgrades, rotate possibly exposed tokens, and test origin validation plus immutable sandbox boundaries.
