# Claude wrote a full FreeBSD remote kernel RCE with root shell

- Score: 243 | [HN](https://news.ycombinator.com/item?id=47597119) | Link: https://github.com/califio/publications/blob/main/MADBugs/CVE-2026-4747/write-up.md

### TL;DR

A technical write-up demonstrates CVE-2026-4747, a remotely reachable stack overflow in FreeBSD’s RPCSEC_GSS validation: an oversized credential overruns a 128-byte kernel buffer on Kerberos-authenticated NFS servers. The proof of concept targets FreeBSD 14.4 without kernel address randomization, uses 15 authenticated overflow rounds to stage code, and ultimately obtains a root reverse shell while consuming NFS worker threads. A valid service ticket is required, but an unprivileged Kerberos user can qualify. HN debated Claude’s contribution: exploit construction followed a disclosed vulnerability, while commenters said Claude also aided its original discovery.

### Comment pulse

- Attribution remains contested: Claude received vulnerability details for exploitation — counterpoint: commenters cite project credits saying it also helped find the bug.
- Cheap automated discovery could help defenders patch more flaws, but it simultaneously lowers offensive capability costs during a risky transition.
- Readers questioned claims about FreeBSD kernel randomization and canary coverage, underscoring how test configuration affects exploitability conclusions.

### LLM perspective

- **View:** The exploit turns enterprise authentication into reachability, showing why valid-user threats belong in kernel-service models.
- **Impact:** Operators running affected NFS and GSS configurations need patched releases; security teams must reassess trusted-user threat models.
- **Watch next:** Reproduction on hardened configurations, official patch adoption, exploit detection, and automated generation of fixes alongside offensive artifacts.
