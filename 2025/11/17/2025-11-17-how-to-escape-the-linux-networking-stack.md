# How to escape the Linux networking stack

- Score: 87 | [HN](https://news.ycombinator.com/item?id=45954638) | Link: https://blog.cloudflare.com/so-long-and-thanks-for-all-the-fish-how-to-escape-the-linux-networking-stack/

- TL;DR
  - Cloudflare tried to forward outbound traffic from shared IP/port “soft‑unicast” slices via TUN+SNAT while also letting apps open local sockets. Conntrack silently rewrote socket source ports outside assigned ranges, breaking flows. They tested fixes: pre-creating conntrack entries (slow/fragile), reserving 5‑tuples using TCP_REPAIR/TCP Fast Open plus routing rule hacks, and ultimately disabling tcp_early_demux to bypass early socket delivery. Despite minimal perf impact, they chose to terminate/proxy TCP for simplicity, visibility, and reliability; SLATFATF (“fish”) mostly handles ICMP.

- Comment pulse
  - Cloudflare should use userspace TCP/IP → promises fewer context switches and copies — counterpoint: kernel TCP with io_uring/zero-copy is competitive; Cloudflare previously justified kernel choice.
  - Why Linux over FreeBSD → broader driver support, tooling, and Cloudflare's kernel expertise; article doesn't address it directly.
  - Readers sought soft‑unicast explainer and enjoyed Hitchhiker references → background improves comprehension; SLATFATF name is a Douglas Adams nod.

- LLM perspective
  - View: Pick one authority for tuple ownership; bind phantom sockets or fully proxy, don’t mix SNAT with autonomous sockets.
  - Impact: Disabling early demux is viable; expect small softirq increases; verify on your traffic mix, especially off-peak inefficiency.
  - Watch next: Kernel-level features: per-interface demux toggles, conntrack tuple reservations, or documented socket-vs-forward precedence controls and observability hooks.
