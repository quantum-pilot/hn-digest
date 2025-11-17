# Why use OpenBSD?

- Score: 127 | [HN](https://news.ycombinator.com/item?id=45944595) | Link: https://www.tumfatig.net/2025/why-are-you-still-using-openbsd/

- TL;DR
  - OpenBSD wins fans for a small, auditable base, secure-by-default stance, pledge/unveil sandboxing, and pf’s readable firewall; many report painless upgrades and long-lived servers. Concerns: lower performance, yearly upgrades without LTS, and fewer container/cloud conveniences. Ops recipes lean on packages, Ansible, chroot/vmm, and cloud-init ports; some compare Ubuntu unfavorably to Debian for Linux stability. Building the full OS from source is straightforward; bootstrappability/reproducibility trail Linux efforts. Recent 7.6 networking work helps, but choices like disabling hyperthreading still trade speed for security.

- Comment pulse
  - Security-first OS with pledge/unveil and readable pf → fewer surprises, easy upgrades; servers run for years — counterpoint: blanket 'disable everything' defaults can brick scenarios.
  - Ops reality → Ubuntu upgrades fragile; Debian cleaner. On OpenBSD, use packages + Ansible, chroot/vmm, cloud-init ports; expect yearly upgrades and fewer container workflows.
  - Performance tradeoff → slower web/firewall throughput than Linux; 7.6 improved TCP stack, but disabled hyperthreading and avoided micro-optimizations keep speed behind.

- LLM perspective
  - View: Choose OpenBSD when simplicity, clear configs, and principled security trump raw performance and container-native workflows.
  - Impact: Small teams gain predictable ops; fewer moving parts, strong defaults; trade-offs hit high-throughput, multimedia, and fast-moving cloud-native stacks.
  - Watch next: Track 7.8 networking benchmarks, container/jail plans, reproducible or bootstrappable builds, and broader cloud image support beyond Vultr.
