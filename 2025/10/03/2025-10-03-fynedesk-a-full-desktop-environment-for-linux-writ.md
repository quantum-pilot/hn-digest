# FyneDesk: A full desktop environment for Linux written in Go

- Score: 244 | [HN](https://news.ycombinator.com/item?id=45458122) | Link: https://github.com/FyshOS/fynedesk

- TL;DR
  - FyneDesk is an open-source Linux/Unix desktop, written in Go atop the Fyne GUI toolkit, aiming for a simple, material-design experience. Today it’s X11-based; a Wayland transition is planned. 0.4.0 (Mar 2024) added virtual desktops; active work continues on a develop branch. Extras include a crash-recovery runner and modular tools for displays, brightness, Wi‑Fi and compositing. HN welcomes the ambition but urges Wayland; maintainers invite contributions and sponsorships from a four-person core team.

- Comment pulse
  - Wayland missing → Users want native Wayland; maintainers say transition begins after next release, pending upstream. — counterpoint: XWayland runs X apps under Wayland today.
  - Activity concern → Master lags, but develop branch is 100+ commits ahead; building from develop is encouraged.
  - Motivation/vision → Volunteer project with 4 core maintainers; goal: best desktop for developers/learners, with an integrated app editor on the roadmap.

- LLM perspective
  - View: Go-native DE validates Fyne for complex UX; success hinges on smooth Wayland migration and portal ergonomics.
  - Impact: Stable Wayland support could attract NVIDIA users and education-focused distros seeking a lightweight, hackable developer-first desktop.
  - Watch next: Publish milestone roadmap, CPU/RAM/compositor benchmarks versus XFCE/LXQt, packaging in major repos, and progress on xdg-desktop-portal UX.
