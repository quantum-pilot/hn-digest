# Apple: SSH and FileVault

- Score: 358 | [HN](https://news.ycombinator.com/item?id=45294440) | Link: https://keith.github.io/xcode-man-pages/apple_ssh_and_filevault.7.html

### TL;DR

macOS 26 Tahoe can unlock a FileVault-encrypted data volume through password authentication over SSH when Remote Login is enabled. Before unlock, ordinary OpenSSH configuration and shell access remain unavailable because they live on the encrypted volume. The initial SSH connection performs only authentication and unlocking, then disconnects while macOS mounts data and starts dependent services; users reconnect afterward. HN readers welcome this for remotely administered Mac minis, especially systems that reboot after outages or major updates without physical keyboard access.

### Comment pulse

- Remote Mac servers become more practical → FileVault no longer forces physical intervention after an unattended reboot.
- Existing `authrestart` offers a one-reboot workaround → commenters note it carries security tradeoffs and is not persistent.
- Mount timing prompted concern → a reply says macOS uses a userspace reboot after unlock to avoid partially available services.

### LLM perspective

- View: Apple separated preboot disk authentication from the full SSH environment without weakening normal post-unlock configuration.
- Impact: Corporate automation can retain disk encryption while recovering headless Macs after power or update restarts.
- Watch next: Authentication hardening, fleet-management support, retry behavior, and edge cases involving secondary encrypted volumes.
