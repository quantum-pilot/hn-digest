# Apple: SSH and FileVault

- Score: 358 | [HN](https://news.ycombinator.com/item?id=45294440) | Link: https://keith.github.io/xcode-man-pages/apple_ssh_and_filevault.7.html

- TL;DR
  - macOS 26 “Tahoe” adds remote FileVault unlock via SSH. At boot, the data volume is locked and OpenSSH configs live there, so keys/shells aren’t usable. If Remote Login is enabled, you can still password-auth to unlock; macOS then briefly drops SSH, mounts the volume, starts services, and full SSH returns. HN sees this enabling headless Mac minis and corporate fleets; previous authrestart tricks had security tradeoffs and didn’t work with FileVault; race worries exist, but Apple triggers a userspace reboot and retries mitigate.

- Comment pulse
  - Headless/server use unlocked → Remote password over SSH unlocks FileVault post-boot; reconnect yields full access; ideal for Mac minis and enterprise fleets.
  - Past approach: authrestart → One-time auto-login bypassed prompts; convenient but risky; didn’t mesh with FileVault-secure workflows — counterpoint: worked before, just not alongside FileVault.
  - Race concerns → Pre-mount services can fail (e.g., Nix shells); Apple does a userspace reboot post-unlock; implement retries for transient SSH drop.

- LLM perspective
  - View: Practical bridge between secure pre-boot and manageability; limits exposure to password-only unlock, then restores full SSH.
  - Impact: Simplifies remote recovery and patching; reduces truck rolls for labs, media, and SMBs running headless Macs.
  - Watch next: MDM commands for unlock/retry orchestration, audit logs for unlock events, and guidance on hardening password auth pre-boot.
