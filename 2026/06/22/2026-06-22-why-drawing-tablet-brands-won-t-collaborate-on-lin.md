# Why Drawing Tablet Brands Won't Collaborate on Linux Floss Drivers

- Score: 205 | [HN](https://news.ycombinator.com/item?id=48629064) | Link: https://www.davidrevoy.com/article1154/why-drawing-tablet-brands-wont-collaborate-on-linux-floss-drivers

### TL;DR

Artist David Revoy tried to replace his laborious one-tablet-at-a-time Linux support process by connecting Gaomon, Huion, XpPen, and related brands directly with Red Hat’s udev-hid-bpf developers. Gaomon declined, saying participation offered little benefit and would expose specifications through infrastructure branded around competitor Wacom. Revoy notes those specifications are easily recorded from hardware and that Wacom-named repositories already support many vendors; the branding itself blocks collaboration. HN mostly favored a vendor-neutral rename or fork, while noting that renaming interconnected projects across distributions requires scarce maintainer labor and may invite corporate influence.

### Comment pulse

- Neutral naming has concrete value → companies interpret LinuxWacom repositories as competitor-controlled and withhold participation even when code supports their devices.
- A rename is operational work, not search-and-replace → maintainers must coordinate repositories, packages, distributions, compatibility, testing, and documentation across an underfunded ecosystem.
- Forking bypasses governance deadlock → a neutral Linuxtablet project could recruit vendors and later upstream support — counterpoint: corporate demands should not dictate community identity.

### LLM perspective

- **View:** Names are architecture for trust: technically neutral code can still signal ownership, risk, and expected credit through repository branding.
- **Impact:** Linux artists face narrower hardware choices; non-Wacom vendors surrender goodwill and compatibility by protecting specifications competitors can already recover.
- **Watch next:** Estimate rename scope, propose neutral governance, document automated HID capture, measure vendor commitments, and fund maintainers before restructuring.
