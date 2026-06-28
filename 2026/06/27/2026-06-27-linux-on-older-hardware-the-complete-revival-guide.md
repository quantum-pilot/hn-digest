# Linux on Older Hardware: The Complete Revival Guide

- Score: 199 | [HN](https://news.ycombinator.com/item?id=48668747) | Link: https://www.fosslinux.com/158206/linux-on-older-hardware-revival-guide.htm

- TL;DR
    - HN readers describe how to revive old PCs and Chromebooks with Linux using lightweight distros, correct swap/zram tuning, and targeted hardware upgrades. Swappiness guidance in the article is challenged: HDD swap and zram need opposite strategies. With 8–16GB RAM, even 10-year-old machines can run modern Wayland desktops comfortably, but 2GB-era devices require ultra-light setups and careful swap use. Browsers and hard RAM caps from chipsets or soldered memory often matter more than the choice of Linux distro.
    - *Content unavailable; summarizing from title/comments.*

- Comment pulse
    - Swap/zram tuning differs: low swappiness for slow HDD swap to avoid paging; high for zram so compression starts early and delays disk I/O.
    - Distro choice matters under 2GB: antiX, Puppy, Bodhi, eXe all viable; crashes often due to heavy browsers and disabled swap — counterpoint: not the distro.
    - Hardware economics debated: some say DDR3 upgrades to 8GB are trivial; others note DDR2, soldered RAM, and chipset caps keep many machines stuck at 2–4GB.

- LLM perspective
    - View: Old desktops with upgradeable GPUs are ideal for local AI workloads, beyond simple web browsing or office use.
    - Impact: Linux prolongs hardware life, reducing e-waste and providing cheap development, media, and thin-client machines for individuals and small organizations.
    - Watch next: Smarter swap/zram defaults and lighter browsers could noticeably improve usability on fixed-RAM Chromebooks and early Core 2 laptops.
