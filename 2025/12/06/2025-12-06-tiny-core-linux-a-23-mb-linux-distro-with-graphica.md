# Tiny Core Linux: a 23 MB Linux distro with graphical desktop

- Score: 332 | [HN](https://news.ycombinator.com/item?id=46173547) | Link: http://www.tinycorelinux.net/

### TL;DR
Tiny Core Linux is a highly modular, RAM-resident Linux distribution whose base system is about a dozen megabytes, providing only a minimal X desktop and letting users add everything else as extensions. It targets fast-booting, nomadic use from CD, USB, or frugal disk installs, with persistent storage optional. HN commenters highlight piCore for Raspberry Pi servers that avoid SD wear, compare alternatives like Alpine, SliTaz, and Puppy, and reminisce about even smaller historical systems like QNX and Damn Small Linux.

### Comment pulse
- Tiny Core’s piCore variant suits Raspberry Pi servers: boots to RAM, minimizes SD wear, ideal for long-lived cronjob appliances and potentially lightweight Node services.  
- Users compare Tiny Core with Alpine, SliTaz, Slax, Puppy; some report surprising responsiveness from Raspberry Pi OS on weak laptops when reviving old hardware.  
- Discussion recalls ultra-small GUIs like QNX’s Photon and early X setups, noting modern 1080p framebuffers alone exceed old RAM budgets—counterpoint: today’s desktops bundle more functionality.  

### LLM perspective
- View: Tiny Core exemplifies an extreme “batteries-optional” OS, valuable where determinism, low write volume, and tiny attack surface matter.  
- Impact: Most useful for embedded appliances, lab machines, and rescue environments, less so for desktop users expecting full hardware support out-of-box.  
- Watch next: Interesting follow-ups: reproducible Tiny Core-based appliances, benchmarks versus Alpine and NixOS minimal images, and tooling for declarative extension sets.
