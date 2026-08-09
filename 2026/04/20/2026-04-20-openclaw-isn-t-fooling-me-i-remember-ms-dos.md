# OpenClaw isn't fooling me. I remember MS-DOS

- Score: 265 | [HN](https://news.ycombinator.com/item?id=47831437) | Link: https://www.flyingpenguin.com/build-an-openclaw-free-secure-always-on-local-ai-agent/

### TL;DR

The author compares agent gateways that give one LLM process shared credentials and shell execution to MS-DOS’s missing isolation. After following NVIDIA’s NemoClaw tutorial, he argues sandboxing the entire agent forces networking, pairing, and policy compromises. His alternative, Wirken, keeps inference on host loopback, separates channel identities and the vault into processes, and sandboxes each shell call in a networkless, read-only container with hash-chained audits. Hacker News accepted OpenClaw’s credential and prompt-injection risks but challenged the DOS history, recalled its simplicity, and framed insecure popularity as “worse is better” debt.

### Comment pulse

- OpenClaw’s shortcuts fit viral product-model demand — counterpoint: popularity rewards immediate utility while deferring security costs into harder future redesigns.
- Critics noted early DOS hardware lacked rings and virtual memory, though DOS remained dominant after protected hardware and Unix-like alternatives arrived.
- Credential custody remained the practical blocker; suggested remedies included out-of-sandbox vaults, tokenizing proxies, granular approvals, and separating destructive actions.

### LLM perspective

- **View:** Tool-layer isolation limits blast radius beyond wrapping a credential-rich agent, but the comparison does not establish Wirken’s security.
- **Impact:** Agent users must trust chat channels, models, routers, plugins, credentials, and approval logic, multiplying both exfiltration and accidental-action paths.
- **Watch next:** Independent audits, prompt-injection tests, vault escape resistance, capability scoping, recovery from destructive actions, and usability under frequent approvals.
