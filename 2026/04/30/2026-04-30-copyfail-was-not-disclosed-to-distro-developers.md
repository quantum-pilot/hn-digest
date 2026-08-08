# CopyFail was not disclosed to distro developers?

- Score: 332 | [HN](https://news.ycombinator.com/item?id=47965108) | Link: https://www.openwall.com/lists/oss-security/2026/04/30/10

### TL;DR

CopyFail, CVE-2026-31431, is a Linux local privilege-escalation flaw introduced in kernel 4.14. Fixes reached 6.18.22, 6.19.12, and 7.0, but older long-term branches initially lacked backports because API changes made adaptation difficult. Gentoo planned to disable the affected `authencesn` module as an immediate workaround. Sam James explained that kernel reporters must separately choose to notify the private `linux-distros` list; that did not happen here. The disclosure exposed a coordination gap while widely deployed kernels remained without straightforward fixes.

### Comment pulse

- Many blamed kernel security coordination, arguing reporters should not individually identify and contact every downstream distributor.
- Others faulted the researchers for publishing an easy exploit first — counterpoint: immediate-disclosure advocates prioritize administrators’ right to mitigate known risk.
- Suggested SUID restrictions address one demonstration path, but commenters warned arbitrary page-cache poisoning offers many escalation routes.

### LLM perspective

- Accepted high-severity fixes should automatically trigger confidential downstream advisories with disclosure deadlines.
- Backport readiness belongs in embargo planning, especially for supported long-term kernels.
- Shared-hosting operators should isolate mutually untrusted tenants beyond a common kernel boundary.
