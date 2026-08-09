# New Apple Silicon M4 and M5 HiDPI Limitation on 4K External Displays

- Score: 301 | [HN](https://news.ycombinator.com/item?id=47569502) | Link: https://smcleod.net/2026/03/new-apple-silicon-m4-m5-hidpi-limitation-on-4k-external-displays/

### TL;DR

An M5 Max investigation finds macOS omits 3840×2160 HiDPI on ordinary 4K external displays, capping sharp output at 3360×1890; M2/M3 systems offered the full mode. Firmware analysis attributes the M4/M5 regression to a hardcoded 6,720-pixel single-stream framebuffer width, below the 7,680-pixel backing store required for 2× 4K despite higher budgets on other sub-pipes. EDID, port, display-count, and private-API experiments failed; a virtual-display mirroring app works imperfectly. HN users corroborated upgrade problems and criticized macOS handling of non-Apple displays.

### Comment pulse

- One prior DisplayPort refresh-rate regression reportedly improved after emailing Tim Cook — counterpoint: replies said the earlier fix remained incomplete.
- Some users suspected Apple favors its monitors; others blamed broader regression-testing failures rather than deliberate discrimination.
- BetterDisplay helps unusual configurations, but ordinary resolution-switching tools cannot select a scaling mode absent from WindowServer’s list.

### LLM perspective

- **View:** The evidence isolates a policy constant, not display bandwidth; exhaustive negative tests make that diagnosis unusually persuasive.
- **Impact:** Owners upgrading computers can lose usable workspace on unchanged monitors, turning a performance purchase into a display downgrade.
- **Watch next:** Apple feedback response, DCP firmware changes, results across M4/M5 variants, and virtual-mirror compatibility after macOS updates.
