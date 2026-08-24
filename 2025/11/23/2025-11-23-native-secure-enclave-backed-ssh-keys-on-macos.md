# Native Secure Enclave backed SSH keys on macOS

- Score: 278 | [HN](https://news.ycombinator.com/item?id=46025721) | Link: https://gist.github.com/arianvp/5f59f1783e3eaf1a2d4cd8e952bb4acf

### TL;DR

macOS Tahoe can create P-256 SSH credentials inside Apple’s Secure Enclave and expose them through the system ssh-keychain security-key provider. Users can require Touch ID, load resident credentials into ssh-agent, or create reference files containing no private material. Setting one provider environment variable lets standard OpenSSH commands use the native path, potentially replacing helper applications. Non-exportable keys maximize isolation but disappear with the device; a separate exportable mode instead encrypts key material with the enclave and supports password-protected backup and import at reduced security.

### Comment pulse

- Backup concerns dominated → device-bound keys vanish with lost hardware. — counterpoint: multiple credentials or an SSH certificate authority provide recovery.
- Native support attracted Secretive users → fewer applications simplifies setup. — counterpoint: smart-card-style tooling may offer a rougher interface.
- Reference files were clarified → exported OpenSSH private-key stubs identify enclave credentials but contain no secret key material.

### LLM perspective

- View: Native integration meaningfully improves key custody, provided users deliberately separate non-exportable authentication from recovery access.
- Impact: Teams can reduce extractable SSH secrets while retaining familiar OpenSSH workflows and explicit biometric approval.
- Watch next: Tahoe reliability, agent forwarding behavior, enterprise deployment guidance, backup policy, and support beyond P-256 credentials.
