# CopyFail was not disclosed to distro developers?

- Score: 332 | [HN](https://news.ycombinator.com/item?id=47965108) | Link: https://www.openwall.com/lists/oss-security/2026/04/30/10

TL;DR  
A severe Linux kernel local privilege escalation (CopyFail, CVE‑2026‑31431) affects kernels since 4.14 via the crypto/AF_ALG subsystem. Mainline/stable got fixes in recent 6.18/6.19/7.0 releases, but long‑term kernels (6.12, 6.6, 6.1, 5.15, 5.10) still lack backports and the upstream fix doesn’t apply cleanly. Gentoo shipped a workaround disabling the affected crypto module. Distributions were not pre‑warned because Linux’s process doesn’t automatically notify distros; the finder disclosed with exploit code, triggering a heated debate over “responsible” disclosure versus broken kernel‑to‑distro coordination.

Comment pulse  
- Who’s responsible for disclosure timing? → Some say releasing a polished exploit before distro patches was reckless; others argue users deserve immediate info and fixes—counterpoint: distros had zero chance to prepare.  
- Process failure, not reporter? → Kernel docs discourage contacting linux-distros before a fix, yet no official downstream notification exists, leaving distros blind despite Linux being a critical shared dependency.  
- Practical security stance → Local kernel LPEs are common; shared-kernel multi‑tenant hosting is inherently risky. Workarounds include eBPF mitigations, but SUID/mount tweaks don’t fix page‑cache poisoning.

LLM perspective  
- View: Linux needs a formal, opt‑in channel from kernel security to vetted distro teams, tied to high‑severity patches and timed disclosure.  
- Impact: Distros, cloud providers, and enterprise users must reassess kernel update cadence and reliance on un-namespaced crypto features.  
- Watch next: Track LTS backports, distro advisories, and any revision to kernel security-bugs policy integrating linux-distros earlier in the workflow.
