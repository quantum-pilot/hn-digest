# I tested every IP KVM in my Homelab

- Score: 222 | [HN](https://news.ycombinator.com/item?id=48413072) | Link: https://www.jeffgeerling.com/blog/2026/i-tested-every-ip-kvm/

### TL;DR

IP KVMs provide keyboard, video, mouse, and BIOS access even when a target OS is frozen or off; many add power control, but all create privileged network attack surfaces. Jeff Geerling compares PiKVM, JetKVM, GL.iNet, NanoKVM, TinyPilot, forks, and direct-USB options from $25 to $499. He favors JetKVM for everyday use and PiKVM for an open, flexible stack despite its price, advising buyers to prioritize ports, PoE, passthrough, power control, support, and trust. HN added production evidence that low-level USB correctness, network isolation, and platform compatibility can outweigh headline features.

### Comment pulse

- Reliability → A refurbisher replaced about 10 GL.iNet units after one ThinkPad rejected malformed USB input; PiKVM passed analyzer testing and offered easier customization.
- Exposure → One user blocks KVM Internet access and reaches it through Tailscale, aligning with the article’s advice to isolate and update devices.
- Alternatives → Intel vPro offers preboot management without an add-on, but needs compatible CPU, chipset, BIOS enablement, and equally strict network controls.

### LLM perspective

- **View:** A remote console is infrastructure, not a gadget; deterministic HID behavior and maintainable firmware matter more than UI polish.
- **Impact:** Homelabs gain recovery independence from host software; businesses can automate BIOS workflows, but compromise reaches below the operating system.
- **Watch next:** Vendor CVE response, signed updates, local-only operation, USB compliance, model identifiers, multi-device management, and long-term upstream support.
