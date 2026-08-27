# Show HN: Shittp – Volatile Dotfiles over SSH

- Score: 113 | [HN](https://news.ycombinator.com/item?id=46344381) | Link: https://github.com/FOBshippingpoint/shittp

### TL;DR

Shittp brings familiar dotfiles into an SSH session without modifying the remote home directory. A POSIX shell script packs local configuration into a tarball, base64-encodes it inside the SSH remote command, extracts it to a temporary directory, sources initialization, starts a shell, and removes the directory on disconnect. It supports alternate SSH clients, remote commands, and Docker output with only common Unix dependencies. Its main documented limit is command argument size; roughly 100 KB can already fail on Alpine Linux.

### Comment pulse

- Temporary configuration suits colleagues' or foreign machines; personally controlled hosts usually already contain the user's dotfiles.
- Some readers favored one-line copy or HOME overrides, while others wanted complete portable toolchains alongside configuration.
- SSHFS would avoid copying but requires reverse connectivity and may enlarge the attack surface.

### LLM perspective

- View: The value is a friendly disposable workflow, not a novel transport primitive.
- Impact: Operators gain familiar sessions without leaving configuration behind or overwriting another user's environment.
- Watch next: Test quoting, cleanup after interruption, secret exclusion, connection overhead, shell portability, and ARG_MAX behavior.
