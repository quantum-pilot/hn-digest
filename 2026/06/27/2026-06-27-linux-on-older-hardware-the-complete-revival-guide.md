# Linux on Older Hardware: The Complete Revival Guide

- Score: 199 | [HN](https://news.ycombinator.com/item?id=48668747) | Link: https://www.fosslinux.com/158206/linux-on-older-hardware-revival-guide.htm

### TL;DR

Linux can extend the useful life of PCs excluded by Windows 11 by matching distro and desktop to RAM, testing from a live USB, enabling zram, trimming unused services, and replacing HDDs with SSDs. The guide recommends antiX/Puppy below 2GB, Lubuntu at 2–4GB, and Xubuntu/Linux Lite above 4GB, while acknowledging failing drives, thermals, or 32-bit limits. HN readers supported revival but challenged universal tuning: zram may favor high swappiness, browsers dominate low-memory failures, and cheap RAM upgrades are not always compatible.

### Comment pulse

- Zram guidance may be reversed → commenters argued compressed swap benefits from high swappiness, unlike slow disk swap.
- Distro prescriptions are not universal → users reported success with Arch/niri, Bodhi, and upgraded Mac Pros under very different constraints.
- RAM upgrades often beat extreme tuning → cheap DDR3 can transform old PCs — counterpoint: soldered memory and firmware limits block many laptops.

### LLM perspective

- **View:** Treat revival as workload triage: storage, memory expandability, browser use, and thermals usually dominate.
- **Impact:** Successful reuse lowers replacement costs and e-waste while turning marginal machines into servers, labs, or thin clients.
- **Watch next:** Verify claimed idle-memory and browser savings on real hardware, especially zram behavior and aging GPU-driver support.
