# Making a Linux home server sleep on idle and wake on demand (2023)

- Score: 296 | [HN](https://news.ycombinator.com/item?id=45108066) | Link: https://dgross.ca/blog/linux-home-server-auto-sleep

TL;DR
A home Time Machine server on Ubuntu suspends when idle and wakes on demand without magic‑packet relays; IPv6 disabled. It combines NIC WOL‑unicast; a tiny Ruby ARP stand‑in on an always‑on Pi to answer ARP for the sleeping host; Avahi to answer mDNS; a cron autosuspend script and systemd hooks to stop services that cause spurious wakeups. Troubleshooting exposed NetBIOS noise from a router (fixed with alternate firmware). HN discusses remote‑wake options (router/Tailscale/RTC), NIC/BIOS pitfalls, and PiKVM/SBCs for robust out‑of‑band control.

Comment pulse
- Remote-wake patterns → Send WoL from router/Internet, or auto-start Tailscale/Tasker; add RTC scheduled wake as failsafe — counterpoint: WoL paths often break across reboots/NAT.
- Hardware pitfalls → Some motherboards cut NIC/USB-NIC power in sleep; disable EuP/ErP in BIOS or keep adapters powered (e.g., USB hub with SD slots).
- Out-of-band control → Use Pi as USB gadget/ATX switch or PiKVM for console and power cycling; consider low-watt SBCs (RockPi S) to avoid idle burn.

LLM perspective
- View: Treat “always-on” helper as discovery proxy for sleepers: answer ARP/mDNS, send unicast to wake hosts only when needed.
- Impact: Homelabs can cut idle watts while keeping SSH/backup access; needs NIC unicast-WoL and clean network with minimal unsolicited chatter.
- Watch next: Add NDP proxying for IPv6, upstream ARP offload to Linux, and publish wake latency and power-savings benchmarks.
