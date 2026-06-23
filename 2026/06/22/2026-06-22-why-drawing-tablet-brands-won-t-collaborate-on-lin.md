# Why Drawing Tablet Brands Won't Collaborate on Linux Floss Drivers

- Score: 205 | [HN](https://news.ycombinator.com/item?id=48629064) | Link: https://www.davidrevoy.com/article1154/why-drawing-tablet-brands-wont-collaborate-on-linux-floss-drivers

### TL;DR
Digital artist David Revoy describes failed attempts to get Huion-affiliated tablet brands to share hardware specs so Linux volunteers can write FLOSS drivers. A Huion engineer ultimately declined, citing that the driver infrastructure is branded “Wacom” and fears of indirectly helping a competitor. Revoy argues this Wacom-centric naming now actively blocks collaboration. Hacker News debates whether the obvious fix—renaming or forking to a vendor‑neutral project—is worth the disruption, and whether open-source should bend to corporate branding concerns.

### Comment pulse
- Neutral renaming of “linuxwacom” → could calm rival vendors’ fears, like master→main — counterpoint: letting brands veto names risks corporate influence on community.
- Renaming is nontrivial → code, packages, docs, and distros need coordination; maintainers already overstretched and underfunded.
- Others propose a fork → copy wacom-hid-descriptors under a neutral name, strip Wacom branding, then invite other vendors to collaborate.

### LLM perspective
- View: This is a classic naming/ownership trap; neutral governance and branding are prerequisites for genuine multi-vendor collaboration.
- Impact: Until vendors engage, Linux artists remain reliant on a few volunteers, limiting device choice and delaying support for new hardware.
- Watch next: Look for a vendor-neutral fork or rebrand, plus distro-level backing or funding for input maintainers to break stalemates like this.
