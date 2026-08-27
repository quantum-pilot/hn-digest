# Native Secure Enclave backed SSH keys on macOS

- Score: 278 | [HN](https://news.ycombinator.com/item?id=46025721) | Link: https://gist.github.com/arianvp/5f59f1783e3eaf1a2d4cd8e952bb4acf

### TL;DR

macOS Tahoe can create biometric-protected P-256 SSH credentials in the Secure Enclave using `sc_auth`, then expose them through Apple’s `ssh-keychain.dylib` as OpenSSH security keys. `ssh-keygen` can save a public key plus a nonsecret credential reference, while `ssh-agent` can load resident identities directly; an environment variable makes the provider default. Nonexportable keys resist extraction but disappear with the device. A separate exportable variant encrypts private material using the enclave for backup. Commenters weighed native convenience against recovery planning, control limitations, and Secretive’s friendlier interface.

### Comment pulse

- Nonexportability benefit → one key per device limits theft, while multiple credentials or an SSH certificate authority preserve recovery.
- Backup compromise → exportable identities improve portability but weaken the guarantee that private material never leaves hardware.
- Native adoption → removing a third-party app is attractive if Apple’s smart-card workflow proves reliable and understandable.

### LLM perspective

- View: Hardware binding improves credential containment but converts device loss into an explicit access-management problem.
- Impact: Mac users gain built-in biometric SSH signing without carrying a separate token or running Secretive.
- Watch next: Verify Tahoe compatibility, biometric-change behavior, agent forwarding prompts, recovery procedures, and Apple documentation.
