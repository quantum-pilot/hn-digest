# Since Linux 6.9, LUKS suspend stopped wiping disk-encryption keys from memory

- Score: 384 | [HN](https://news.ycombinator.com/item?id=48763035) | Link: https://mathstodon.xyz/@iblech/116769502749142438

### TL;DR
Linux 6.9 introduced a regression where `cryptsetup luksSuspend` no longer reliably removed LUKS volume keys from RAM, undermining setups that rely on “secure suspend” (wipe key, ask again on resume). This mainly affects systems using the Debian-origin `cryptsetup-suspend` approach, now adopted by several distros, not default Linux suspend. The bug stemmed from a change breaking the documented lifetime of thread keyrings, so keys survived longer than expected. NixOS integration tests helped detect and bisect the issue.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Scope is narrower than the title suggests → only configurations using `cryptsetup luksSuspend`/`cryptsetup-suspend` were affected, not stock suspend flows — counterpoint: the broken thread-keyring behavior is clearly a kernel regression.

- Security angle → regular suspend keeps keys in RAM; Debian’s addon was meant to clear them to resist physical/cold-boot attacks; CPU RAM-encryption features further reduce such risks.

- Threat models differ → some only care about data-at-rest when selling laptops; suggestions include wiping the LUKS header, though with strong keys that’s largely redundant.

---

### LLM perspective
- View: This illustrates how subtle kernel API contract changes (keyring semantics) can silently break higher-level security guarantees.

- Impact: Cryptsetup, distro maintainers, and security-conscious users must treat “secure suspend” as an explicitly tested feature, not an assumed property.

- Watch next: Track kernel fixes, add upstream regression tests for luksSuspend-like workflows, and clarify distro defaults around suspend vs hibernate security.
