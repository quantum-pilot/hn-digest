# Since Linux 6.9, LUKS suspend stopped wiping disk-encryption keys from memory

- Score: 384 | [HN](https://news.ycombinator.com/item?id=48763035) | Link: https://mathstodon.xyz/@iblech/116769502749142438

### TL;DR

A Linux 6.9 regression broke the optional cryptsetup-suspend workflow that removes LUKS volume keys from RAM and requires a passphrase after resume. A kernel refactor changed thread-keyring cleanup behavior, so the command silently left keys resident while normal suspend and resume still appeared successful. The author bisected the failure, proposed a one-line kernel fix, added a NixOS integration test, and prompted a cryptsetup warning. HN clarified that stock suspend never promises key removal; exposure concerns Debian’s add-on and ports using this extra hardening, not every LUKS installation.

### Comment pulse

- Silent success made detection unlikely → functionality looked normal while the security property disappeared, illustrating why regression tests must inspect key state.
- Scope matters → users without post-resume passphrase prompts were never using key-wiping suspend — counterpoint: the add-on spread beyond Debian.
- Threat models differ → some need only shutdown or resale protection, while seizure resistance requires protecting keys on powered devices.

### LLM perspective

- **View:** Security invariants deserve direct tests because availability checks cannot detect silent loss of protection.
- **Impact:** Hardened Linux laptop users should verify actual resume behavior, not infer it from configured hooks.
- **Watch next:** Track kernel patch adoption, cryptsetup warnings, and distribution coverage of the new integration test.
