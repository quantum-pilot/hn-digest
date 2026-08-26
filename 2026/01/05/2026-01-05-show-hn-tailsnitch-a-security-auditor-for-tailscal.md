# Show HN: Tailsnitch – A security auditor for Tailscale

- Score: 235 | [HN](https://news.ycombinator.com/item?id=46501137) | Link: https://github.com/Adversis/tailsnitch

### TL;DR

Tailsnitch is an MIT-licensed Go auditor for Tailscale configurations, running 52 checks across access controls, authentication, devices, network exposure, SSH, logging, and DNS. It supports scoped OAuth or API keys, severity and category filtering, JSON output, accepted-risk ignores, SOC 2 evidence, CI use, and interactive or dry-run remediation for selected findings. HN users welcomed help with sprawling ACLs, while asking for Headscale compatibility, native Tailscale scanning, and live structured SSH-session events—capabilities beyond this point-in-time configuration linter.

### Comment pulse

- Growing teams value CI scanning → long HuJSON policies become difficult to review confidently as environments and memberships multiply.
- Security practitioners want operational telemetry too → connection, idle-session, and disconnect events serve detection needs that configuration audits cannot.
- Native continuous compliance appeals to enterprises → Tailscale APIs could feed GRC tools and preserve point-in-time reports.

### LLM perspective

- View: Configuration linting finds risky states, but cannot prove intended access behavior or detect live misuse.
- Impact: Administrators gain repeatable evidence and remediation; mature teams still need event telemetry and independent policy tests.
- Watch next: Verify check accuracy, OAuth least privilege, fix-mode auditability, Headscale support, and remote Tailnet Lock handling.
