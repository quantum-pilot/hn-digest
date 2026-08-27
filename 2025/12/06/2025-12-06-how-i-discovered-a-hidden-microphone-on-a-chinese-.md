# How I discovered a hidden microphone on a Chinese NanoKVM

- Score: 352 | [HN](https://news.ycombinator.com/item?id=46173383) | Link: https://telefoncek.si/2025/02/2025-02-10-hidden-microphone-on-nanokvm/

### TL;DR

A NanoKVM owner reports that the remote-control device shipped with a microphone and recording tools despite the microphone not being clearly advertised for the KVM product. Their audit also alleges an initial default SSH password, shared hardcoded encryption material, weak session controls, unverifiable updates, and communications with vendor servers. The author attributes this to rushed negligence rather than proven espionage and suggests alternative firmware. Commenters accept the serious credential and firmware issues but dispute treating embedded Linux minimalism, diagnostic tools, Chinese DNS, or hardware reuse as evidence of malice.

### Comment pulse

- The underlying LicheeRV Nano specification reportedly lists a microphone—counterpoint: NanoKVM buyers were not clearly told it remained active.
- Critics prioritize shared secrets and root-level design over missing systemd, apt, CSRF protection, or bundled network utilities.
- A compromised KVM already exposes screen and input; server-room audio may add less risk than keylogging.

### LLM perspective

- View: The strongest case is insecure privileged firmware, not the device’s nationality or tool inventory.
- Impact: KVM compromise can bypass host controls because it impersonates trusted display and input hardware.
- Watch next: Signed updates, unique credentials, microphone disclosure, network isolation guidance, and independent firmware audits.
