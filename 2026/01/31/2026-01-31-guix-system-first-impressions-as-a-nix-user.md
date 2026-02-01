# Guix System First Impressions as a Nix User

- Score: 140 | [HN](https://news.ycombinator.com/item?id=46835612) | Link: https://nemin.hu/guix.html

## TL;DR
An experienced NixOS user revisits Guix System 1.5.0 and finds installation surprisingly painful: very slow binary substitutes, KDE/Wayland broken on a modern Nvidia GPU, and confusing multi-instance `guix pull` behavior. Switching to the Nonguix channel with proprietary kernel/firmware and Nvidia drivers finally yields a stable daily driver with Steam and modern apps. Once running, Guix’s Scheme-based config, built-in `guix home`, and hackability feel nicer than Nix language, though Guix still trails in docs, service breadth, infra speed, and desktop polish.

## Comment pulse
- Guix works fine on homelab servers with `guix deploy` and Scheme-powered configs, but has fewer ready-made services and packages than NixOS’s huge, fresh nixpkgs set.  
- Nixpkgs’ massive Git repo is painful; some users rely on shallow clones, time-limited fetches, or weekly rebased forks to keep local overlays manageable.  
- Some feel Guix under-serves power-desktop use (no first-class ZFS root, missing apps like RustDesk) — counterpoint: ext4 remains dominant and Guix+ZFS configs already exist.

## LLM perspective
- Guix now looks viable for daily drivers if you accept rough edges, slower infra, and frequent manual reading of manuals.  
- NixOS users into Scheme or FSF ideals might trial Guix on workstations, while retaining Nix for servers and existing tooling.  
- Watch: Guix substitute servers performance, desktop GPU/Wayland stability, and emerging tools for translating or sharing configurations between Nix and Guix.
