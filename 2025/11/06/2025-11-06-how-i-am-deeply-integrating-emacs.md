# How I am deeply integrating Emacs

- Score: 201 | [HN](https://news.ycombinator.com/item?id=45832341) | Link: https://joshblais.com/blog/how-i-am-deeply-integrating-emacs/

- TL;DR
  An Emacs-centric workflow on Wayland: the author skips EXWM (single-threaded Emacs, X11-only) and instead uses Hyprland plus a Go “Emacs Launcher” to trigger emacsclient commands system‑wide. Keybindings open vterm, a Universal Launcher, org-capture/agenda, dirvish, pass, mu4e, elfeed, EMMS, and “edit-anywhere” for browser text. The result is an almost-all-in-Emacs desktop. HN debates whether tools or motivation matter more, praises Emacs as a programmable “visual shell,” surfaces accessibility gaps (Emacspeak, NVDA), and shares capture-from-anywhere patterns.

- Comment pulse
  - Tooling helps only if motivation exists → better tools reduce friction, but mastery matters more — counterpoint: avoiding tools often masks inertia.
  - Emacs accessibility is uneven → Emacspeak/speechd-el work on Linux; Windows with NVDA misses Emacs commands; GUI/Calendars poorly spoken; development appears paused.
  - Seamless capture wins → phone dictation to inbox.org or Twilio-to-todo pipelines keep ideas flowing; daily triage empties inbox and refiles.

- LLM perspective
  - View: Replicating EXWM affordances with a Wayland WM plus emacsclient yields most benefits without X11 or global hangs.
  - Impact: Makes Emacs-first setups viable for Wayland users; encourages keyboard-driven workflows; highlights unmet accessibility needs.
  - Watch next: Wayland-native EXWM alternatives, Emacs async/threading improvements, revived Emacspeak/Windows support, and measurable latency/throughput benchmarks for launcher workflows.
