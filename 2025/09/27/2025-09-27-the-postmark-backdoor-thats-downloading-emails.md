# The Postmark backdoor that’s downloading emails

- Score: 214 | [HN](https://news.ycombinator.com/item?id=45395957) | Link: https://www.koi.security/blog/postmark-mcp-npm-malicious-backdoor-email-theft

- TL;DR
  Security firm Koi reports a malicious update to the npm package postmark-mcp: version 1.0.16 added a hidden BCC to phan@giftshop.club, silently exfiltrating every sent email. The package impersonated Postmark’s official repo and was later deleted, but installed instances continue leaking. Koi frames this as the first malicious MCP server and a warning that AI agent “tools” have god-mode privileges with no sandboxing. HN debates whether this risk is unique to MCPs, questions download-based impact estimates, and calls for default sandboxing and stricter supply-chain controls.

- Comment pulse
  - Not MCP-specific → Any software/extension can exfiltrate data; you trust authors/distributors by design — counterpoint: MCP agents execute autonomously, multiplying unnoticed misuse.
  - Impact skepticism → npm download counts are noisy; CI pipelines inflate numbers; repo engagement is tiny, so likely few real users.
  - Obvious yet recurrent → Convenience beats security; users keep granting god-mode; missing default sandboxing makes repeating this mistake easy.

- LLM perspective
  - View: Treat MCP servers as privileged extensions; require provenance, code review, and behavior monitoring before enabling sensitive scopes.
  - Impact: Security teams should inventory MCP tools, gate installs, enforce least-privilege tokens; AI platforms need built-in allowlists and audit logs.
  - Watch next: Independent verification: revocation lists for MCPs, signature/publisher verification, runtime policy (no external BCC), and telemetry showing package-to-resource access.
