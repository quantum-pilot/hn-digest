# Genode OS Framework

- Score: 119 | [HN](https://news.ycombinator.com/item?id=45384653) | Link: https://genode.org

- TL;DR
  - Genode is an open-source framework for composing secure OSes on microkernels using capabilities and least authority across drivers, services, and apps. Its flagship Sculpt OS targets PCs/phones with sandboxed drivers and VMs. Recent releases add a fair, low-latency scheduler, hardened APIs via GCC 14, and updated graphics/network/storage drivers. HN focuses on real-world viability, desktop usability, and kernel backends (NOVA, seL4), with long-term observers noting continuity and striking configurability.

- Comment pulse
  - Works in practice → Maintainers use Sculpt daily on x86/ARM; USB image with presets enables quick desktop/browser trials.
  - Powerful but UX rough → Presets help, but real use requires docs and manual composition; framework-first, desktop polish catching up — counterpoint: progress shown in recent videos/talks.
  - Kernel choices matter → NOVA is default; seL4 supported; performance and hardware support vary widely, influencing deployment.

- LLM perspective
  - View: Compositional OS as enforcement plane; Genode shows policy can be assembled and auditable at component boundaries.
  - Impact: Could harden kiosks, industrial HMIs, and sensitive developer laptops without monolithic kernels; VM support eases migration.
  - Watch next: Measure end-to-end latency under the new scheduler; track GPU, Wi‑Fi, and browser updates for daily-driver viability.
