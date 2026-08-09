# Baochip-1x: What it is, why I'm doing it now and how it came about

- Score: 262 | [HN](https://news.ycombinator.com/item?id=47339219) | Link: https://www.crowdsupply.com/baochip/dabao/updates/what-it-is-why-im-doing-it-now-and-how-it-came-about

### TL;DR

Baochip-1x combines open VexRiscv cores and an MMU with a 22 nm embedded SoC, targeting secure loadable applications and the small-footprint Rust Xous OS. Most data-processing RTL is inspectable; closed blocks are mainly AXI, USB PHY, analog, and I/O components. Rather than fund a separate mask set, bunnie “hitchhiked” in unused space on Crossbar silicon, sharing peripherals with a switchable proprietary CPU. Hundreds of hand-screened samples exist, with thousands planned after automated qualification; commenters praise the arrangement while emphasizing the trust and schedule risk Crossbar accepted.

### Comment pulse

- The MMU breaks embedded flat-memory convention while remaining composable with PMP and CHERI-style protections.
- Shipping partially open silicon now can mature software before fully open fabrication becomes economical.
- Crowd Supply’s reported VPN blocking frustrated privacy-conscious readers — counterpoint: another commenter cited export-control risk.

### LLM perspective

- **View:** Reusing spare die area turns interpersonal trust and disciplined scope into substitutes for venture capital.
- **Impact:** Developers gain inspectable compute logic and a path away from proprietary embedded memory protection.
- **Watch next:** Production qualification, driver and documentation progress, additional languages and operating systems, and late-2026 inventory.
