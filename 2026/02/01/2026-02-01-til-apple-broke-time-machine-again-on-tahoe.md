# TIL: Apple Broke Time Machine Again on Tahoe

- Score: 154 | [HN](https://news.ycombinator.com/item?id=46848699) | Link: https://taoofmac.com/space/til/2026/02/01/1630

### TL;DR
macOS Tahoe silently stopped doing Time Machine backups to the author’s Synology NAS for about two months, with no warnings. The culprit appears to be Apple tightening SMB defaults (now requiring signing), which many NAS devices don’t match out of the box. A workaround is to override SMB behavior via `/etc/nsmb.conf` on the Mac and tune Synology’s SMB options, but this feels fragile. The author is moving Time Machine duties to a dedicated Docker container on a Proxmox+ZFS host, and criticizes Apple’s QA and opaque changes.

---

### Comment pulse
- Apple’s QA and platform direction are deteriorating → long-standing bugs, noisy Console logs, Unix/scripting de‑emphasis erode trust in macOS reliability.
- Time Machine over the network is fragile → frequent sparsebundle corruption and resets; some report it works fine locally or “used to” work well.  
- Design issues with network backups → network FS approach amplifies fragility; encrypted sparsebundles behave better, while many users layer third‑party tools like Arq for real safety.

---

### LLM perspective
- View: Critical infrastructure like backups must fail loudly; silent backup breakage is worse than not backing up at all.
- Impact: Power users migrate to self‑hosted, containerized backup targets, weakening trust in Apple’s “it just works” narrative.
- Watch next: Tools that continuously verify and alert on backup health, plus Apple documentation or release notes around protocol/security changes.
