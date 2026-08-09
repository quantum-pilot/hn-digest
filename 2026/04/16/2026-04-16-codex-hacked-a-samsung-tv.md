# Codex Hacked a Samsung TV

- Score: 201 | [HN](https://news.ycombinator.com/item?id=47791212) | Link: https://blog.calif.io/p/codex-hacked-a-samsung-tv

### TL;DR

Researchers gave Codex a browser shell on a Samsung Tizen TV, matching firmware source, an ARM build host, and an in-memory execution helper, then asked it to reach root. Codex identified world-writable Novatek driver nodes, found /dev/ntksys mapped arbitrary physical memory, validated it with an ntkhdma address leak, scanned RAM for the browser process’s credentials, zeroed its identity fields, and launched a root shell. Humans repeatedly redirected execution. Hacker News found it impressive but stressed that source access and the initial compromise were advantages, leaving binary-only and black-box performance unanswered.

### Comment pulse

- The crucial bug was architectural: an unprivileged, world-writable driver accepted unchecked physical ranges and remapped their page frames directly.
- The agent built, deployed, tested, and revised live exploits — counterpoint: humans supplied infrastructure, corrected mistakes, and had already gained browser execution.
- Owners reported assistants rapidly reverse-engineering locked-down routers and peripherals, turning undocumented protocols into usable APIs and metrics.

### LLM perspective

- **View:** The result demonstrates post-exploitation engineering, not autonomous end-to-end compromise; the harness converted hardware research into an operable feedback loop.
- **Impact:** Vendor source releases can accelerate defensive auditing and exploitation alike, especially when unsafe kernel interfaces survive into shipped devices.
- **Watch next:** Binary-only reproduction, blind discovery, exploit stability, firmware scope, vendor remediation, disclosure timing, and safeguards for autonomous device testing.
