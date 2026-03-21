# Wayland set the Linux Desktop back by 10 years?

- Score: 312 | [HN](https://news.ycombinator.com/item?id=47448328) | Link: https://omar.yt/posts/wayland-set-the-linux-desktop-back-by-10-years

## TL;DR
Author argues Wayland has misdirected 17 years of effort: security-by-default breaks familiar Unix composability (screen capture, automation), performance isn’t clearly better, core features depend on fragile, fragmented compositor extensions, and distros are forcing an unfinished replacement while X11 still works. They predict a future protocol will supplant both. HN commenters split: some echo “forced migration with regressions,” others say Wayland now works excellently, enabled per‑monitor scaling, and drove essential cleanups in the Linux graphics/audio stacks.

## Comment pulse
- Wayland works well for many → Fedora/GNOME/AMD users report stable desktops, portals, fractional scaling; view article as outdated rant — counterpoint: others still see regressions.  
- Forced migration concern → Some distros/DEs ship Wayland-only GNOME, so users feeling broken workflows or stuttery KDE/dual-monitor setups perceive being compelled before readiness.  
- Architectural payoff vs missing features → Commenters note Wayland forced big driver/graphics cleanups, like PulseAudio did for audio, but automation, portals, window-state basics remain inconsistent.  

## LLM perspective
- View: Wayland’s story shows how replacing core infrastructure mixes real technical wins with long regressions for power users and edge workflows.  
- Impact: Most typical desktop users on mainstream distros may benefit, while automation-heavy, multi‑monitor, NVIDIA or niche‑tool users still pay migration costs.  
- Watch next: Track portal/permission APIs, NVIDIA driver maturity, and whether DEs standardize on feature-rich protocols that restore scripting without gutting isolation.
