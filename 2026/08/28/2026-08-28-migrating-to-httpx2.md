# Migrating to HTTPX2

- Score: 193 | [HN](https://news.ycombinator.com/item?id=49477212) | Link: https://github.com/openai/openai-python/blob/main/httpx2.md

### TL;DR

The OpenAI Python SDK now installs HTTPX2 instead of legacy HTTPX. Default API calls remain unchanged, but custom clients, transports, hooks, mocks, raw responses, and annotations must use HTTPX2 objects. TLS verification now uses the operating-system trust store rather than certifi, potentially breaking minimal containers or corporate proxies unless CA settings are updated. A temporary injected legacy client remains possible with type-checking workarounds. Commenters framed HTTPX2 as a stability fork amid HTTPX governance and breaking-change concerns, while questioning alternatives and migration benefits.

### Comment pulse

- HTTPX2 preserves the familiar API while HTTPX approaches disruptive changes → SDK maintainers gain a steadier dependency target.
- System trust stores simplify internal CA support → counterpoint: missing container certificates can become a deployment break.
- Alternative clients may benchmark faster → commenters questioned governance and monkey-patching behavior in one proposed option.

### LLM perspective

- View: Compatibility at the SDK surface hides meaningful transport, trust-store, typing, and test-infrastructure changes.
- Impact: Teams with custom networking or corporate certificates need deliberate migration; default-client users mostly do not.
- Watch next: Audit CA bundles, transitive imports, mocks, instrumentation, transports, and the legacy escape hatch's removal timeline.
