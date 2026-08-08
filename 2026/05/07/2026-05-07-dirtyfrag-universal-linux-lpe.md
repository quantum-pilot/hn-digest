# Dirtyfrag: Universal Linux LPE

- Score: 346 | [HN](https://news.ycombinator.com/item?id=48053623) | Link: https://www.openwall.com/lists/oss-security/2026/05/07/8

### TL;DR

Security researcher Hyunwoo Kim disclosed Dirty Frag, a Linux local privilege-escalation technique claimed to work across major distributions by chaining two kernel vulnerabilities involving ESP/XFRM and RxRPC paths with page-cache corruption. The post included working exploit code that turns an unprivileged local account into root. Disclosure followed a broken embargo, so the announcement said no distribution patches or CVEs were yet available. Its interim mitigation disables and unloads the `esp4`, `esp6`, and `rxrpc` modules; applicability depends on whether they are loadable rather than built into a distribution kernel.

### Comment pulse

- Readers said Copy Fail targeted the wrong interface while leaving authencesn reachable — counterpoint: they stressed the RxRPC issue is separate.
- Debate split between minimizing optional kernel attack surface and preserving broad module compatibility for uncommon workloads.
- Several corrected unsafe recovery advice: privileged redirection matters, and confirmed compromise warrants rebuilding rather than merely clearing caches.

### LLM perspective

- Emergency guidance should distinguish prevention, removal of poisoned page-cache state, and recovery after successful exploitation.
- Autoloadable modules expand reachable attack surface even when no service is listening or manually enabled.
- Broken embargoes create an operational race between public exploitability and downstream patch delivery.
