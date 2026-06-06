# I tested every IP KVM in my Homelab

- Score: 222 | [HN](https://news.ycombinator.com/item?id=48413072) | Link: https://www.jeffgeerling.com/blog/2026/i-tested-every-ip-kvm/

### TL;DR
Geerling surveys the booming ecosystem of IP KVMs—from $25 DIY-ish USB dongles to $400 Pi-based, enterprise-ready units—and explains when you need them over SSH/RDP: BIOS access, crashed OSes, and machines you must reach “no matter what.” He compares PiKVM, JetKVM, GL.iNet, Sipeed, TinyPilot and others on price, resolution, PoE, passthrough, USB vs LAN, and openness. Security risks are emphasized: these devices are remote backdoors, some with serious past vulnerabilities. His daily driver: JetKVM; gold standard: PiKVM.

---

### Comment pulse
- PiKVM is “gold standard” → rock-solid USB behavior, very hackable, supports original authors; GL.iNet forks are cheaper but had protocol bugs and are less customizable.
- JetKVM appreciated → polished hardware and software; confusion over new PoE/full-HDMI revision since naming and SKUs don’t clearly distinguish versions.
- Intel vPro/AMT raised as alternative → powerful firmware-level KVM, but rarely present/enabled on consumer gear and risky if not tightly controlled.

---

### LLM perspective
- View: Feature checklists matter, but trust (vendor, firmware, update cadence) is the real deciding factor for out-of-band access tools.
- Impact: These devices let homelabs and small orgs get near-iDRAC/iLO-class control without buying server hardware, shifting how they design remote infrastructure.
- Watch next: Independent security reviews, clearer open-source compliance, and unified management dashboards for fleets of heterogeneous IP KVMs.
