# LittleSnitch for Linux

- Score: 1259 | [HN](https://news.ycombinator.com/item?id=47697870) | Link: https://obdev.at/products/littlesnitch-linux/index.html

- TL;DR  
  - Little Snitch is now on Linux as a per-application outbound traffic monitor and blocker, using eBPF on kernel ≥6.12 with BTF. It offers a browser-based UI, rule sets plus downloadable blocklists, and advanced tuning via TOML configs, but explicitly targets privacy/telemetry control rather than hard security. The eBPF probe and UI are GPL, while the daemon is proprietary yet free. HN debates bypass resistance, early Fedora/Btrfs breakage, and whether a proprietary network tool can succeed in a FOSS-first ecosystem.

- Comment pulse  
  - App firewalls can be bypassed via trusted programs → commenters note process/parent matching and SELinux/AppArmor help, but full “leak control” is hard.  
  - Early adopter reports Fedora/Btrfs installs pegging CPUs and failing to start → maintainer acknowledges limited testing, eBPF fragility, and promises rapid 1.0.1 fixes.  
  - Many prefer OpenSnitch’s full openness for privileged networking components → strong ideological resistance to closed daemons handling traffic, even if free—counterpoint: author intentionally experiments with this free-but-proprietary model.

- LLM perspective  
  - View: This is a usability upgrade for outbound monitoring on Linux, not a replacement for kernel-level MAC or IDS.  
  - Impact: Most relevant for desktop users wanting telemetry visibility; serious hardening still needs SELinux/AppArmor plus dedicated firewalls.  
  - Watch next: Comparative benchmarks vs OpenSnitch on attribution accuracy, latency, and stability across distros/filesystems and under heavy connection churn.
