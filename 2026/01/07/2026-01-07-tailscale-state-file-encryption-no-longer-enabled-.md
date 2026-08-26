# Tailscale state file encryption no longer enabled by default

- Score: 164 | [HN](https://news.ycombinator.com/item?id=46531925) | Link: https://tailscale.com/changelog

### TL;DR

Tailscale 1.92.5 changed Linux and Windows defaults so state-file encryption and hardware-attestation keys are no longer automatically enabled. It also stopped hardware-key loading failures from preventing client startup after a TPM reset or replacement. This frozen input contains only the January 6 client entry; context in the discussion came from the engineer who made the change. They said heterogeneous TPM behavior created excessive support failures, so controlled, security-conscious fleets can still opt in while broad consumer installations favor recoverability and reliable startup.

### Comment pulse

- The responsible engineer said benign TPM resets, BIOS changes, VMs, and heterogeneous hardware made default enforcement too support-intensive.
- Some readers endorsed opt-in security; others argued TPM failure should block access precisely because replacement may indicate tampering.
- Recovery-key proposals exposed a core tension: escape hatches improve reliability but can weaken hardware-bound protection.

### LLM perspective

- View: Secure defaults lose legitimacy when ordinary platform maintenance is indistinguishable from hostile key loss.
- Impact: Administrators must now explicitly trade stronger node-state protection against fleet heterogeneity and recovery costs.
- Watch next: Better diagnostics, backup policy, and scoped defaults could recover security without recreating startup failures.
