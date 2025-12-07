# How I discovered a hidden microphone on a Chinese NanoKVM

- Score: 352 | [HN](https://news.ycombinator.com/item?id=46173383) | Link: https://telefoncek.si/2025/02/2025-02-10-hidden-microphone-on-nanokvm/

### TL;DR
A security researcher audited Sipeed’s NanoKVM, an ultra-cheap, networked KVM-over-IP device, and found a pile of issues: default SSH password, weak web security (no CSRF, shared hardcoded crypto key), opaque Chinese DNS/update infrastructure, no firmware integrity checks, and preinstalled packet‑capture tools. Most strikingly, the device’s baseboard includes an on-board microphone that isn’t clearly disclosed for the KVM product, yet is fully usable for recording via SSH. The author leans toward negligence over espionage, and notes users can reflash open-source firmware and physically remove the mic. Hacker News debates how serious and unusual these flaws really are versus normal embedded‑Linux sloppiness and hype around “Chinese” hardware.

---

### Comment pulse
- Hidden mic concern → KVM buyers weren’t told, even if base SBC listed it; reuse of boards isn’t an excuse—counterpoint: main risk is full KVM access anyway.  
- Embedded norms vs “flaws” → Chinese DNS, no systemd/apt, tcpdump/aircrack are typical in small Linux devices; core issues are hardcoded secrets, root‑everything, open ports.  
- Broader trust debate → Some see clickbait, xenophobia, and misleading Apple/Google comparisons; others say cheap networked KVMs are inherently dangerous and deserve scrutiny.

---

### LLM perspective
- View: Treat any low-cost, cloud-updating remote-management box as untrusted; segment it, audit firmware, or avoid entirely.  
- Impact: Sysadmins, homelab users, and small businesses relying on budget KVM/IP gear face underestimated surveillance and takeover risk.  
- Watch next: Community firmware hardening, reproducible builds, vendor disclosure of sensors, and third-party teardown audits for remote-access hardware.
