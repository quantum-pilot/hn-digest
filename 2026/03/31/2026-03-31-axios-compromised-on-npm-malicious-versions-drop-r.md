# Axios compromised on NPM – Malicious versions drop remote access trojan

- Score: 1757 | [HN](https://news.ycombinator.com/item?id=47582220) | Link: https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan

### TL;DR

StepSecurity reports that a hijacked axios maintainer account published versions 1.14.1 and 0.30.4, each adding an unused dependency, plain-crypto-js 4.2.1. Its install hook fetched platform-specific remote-access payloads on macOS, Windows, and Linux, then deleted its script and replaced its manifest with a clean-looking older version. The poisoned axios releases were available for roughly two to three hours before removal; users who installed them are told to assume compromise, rebuild, and rotate secrets. HN favored package cooldowns, disabled lifecycle scripts, isolated builds, and fewer dependencies.

### Comment pulse

- Batteries-included platforms reduce third-party attack surface — counterpoint: standard libraries age and cannot cover every format, API, or specialized use case.
- Minimum release ages and disabled install scripts would block this incident, giving researchers time to quarantine fresh malicious packages.
- Trusted publishing removes long-lived tokens, but full registry-account takeover can change configuration; downstream sandboxes and egress controls remain necessary.

### LLM perspective

- **View:** Source review alone is insufficient when release provenance and install-time execution form separate trust boundaries.
- **Impact:** Developer machines and CI runners placed accessible credentials at risk before application code ever imported axios.
- **Watch next:** Downstream credential pivots, confirmed install counts, npm account controls, maintainer findings, and stronger lifecycle-script defaults.
