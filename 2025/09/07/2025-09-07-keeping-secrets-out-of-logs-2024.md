# Keeping secrets out of logs (2024)

- Score: 249 | [HN](https://news.ycombinator.com/item?id=45160774) | Link: https://allan.reyes.sh/posts/keeping-secrets-out-of-logs/

TL;DR
Secrets-in-logs isn’t solvable by one control. The article catalogs six common causes (direct logging, “kitchen-sink” objects, config flips, embedded-in-URLs, telemetry, user input) and ten “lead bullets”: centralized pipelines, minimization/redaction/tokenization, domain primitives and read-once wrappers, taint checking, log formatters, unit tests, scanners, and preprocessors, plus people/process. Strategy: map data flows, protect chokepoints, layer prevention and detection, and plan cleanup/rotation. HN discussion highlights runtime tagging vs. type/taint approaches, node-level rsyslog redaction, limitations of GuardedString, and the need for training and better architectures.

Comment pulse
- Runtime in‑band tagging → mark secrets with magic tokens and strip at sinks; simple to deploy — counterpoint: late masking, no single‑use, easy to bypass.
- Node‑level rsyslog redaction → regex redact known patterns, spool locally, encrypt upstream; throttle to WARN+ and alert on risky INFO/DEBUG to limit retention exposure.
- Train developers and prefer signatures/IDs over transmitting secrets → fewer kitchen‑sink leaks; third‑party APIs may still force bearer tokens in headers.

LLM perspective
- View: Model logs as data flows; pair domain primitives, read-once wrappers, and taint analysis; scanners are backstops, not shields.
- Impact: Catches leaks in compile-time/tests, lowers prod overhead, and limits blast radius when config flips or telemetry bypasses logging.
- Watch next: Define leak-rate SLOs, measure formatter and preprocessor latency, pilot Semgrep/CodeQL rules, and test sampling plus TruffleHog/LLM verification pipelines.
