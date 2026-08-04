# Claude Code is steganographically marking requests

- Score: 1327 | [HN](https://news.ycombinator.com/item?id=48734373) | Link: https://thereallo.dev/blog/claude-code-prompt-steganography

### TL;DR

Inspection of Claude Code 2.1.196 found a hidden classifier in its system prompt: when `ANTHROPIC_BASE_URL` targets a custom gateway, hostname categories alter the Unicode apostrophe in “Today’s,” while Shanghai or Urumqi time zones change date hyphens to slashes. Official or unset endpoints bypass it. The author infers Anthropic uses these markers to identify resellers or model-distillation traffic, but calls the undisclosed, obfuscated mechanism a trust violation and technically trivial to evade. HN split between that transparency concern and the view that covert, strip-resistant abuse detection is justified.

### Comment pulse

- Undisclosed fingerprinting breaks developer trust → a privileged coding client classified local configuration without documentation, prompting fears about unobserved data collection.
- Steganography strengthens abuse detection → gateways can remove explicit telemetry — counterpoint: visible Unicode markers are easily patched by serious adversaries.
- Legitimate proxies face collateral risk → internal routers, secret filters, account switching, and request inspection may be misclassified alongside resellers.

### LLM perspective

- **View:** The failure is governance, not marker potency: security controls in privileged clients need disclosed purpose, scope, and appeal paths.
- **Impact:** Custom-gateway users may receive differentiated treatment; Anthropic gains weak attribution signals while accepting reputational and false-positive costs.
- **Watch next:** Demand release-note disclosure, reproducible client builds, traffic audits, controlled response comparisons, and documented handling of marker-derived classifications.
