# Show HN: Bash Screensavers

- Score: 210 | [HN](https://news.ycombinator.com/item?id=45731366) | Link: https://github.com/attogram/bash-screensavers

- TL;DR
  - A playful, MIT-licensed collection of Bash scripts turns your terminal into animated “screensavers” (matrix, pipes, life, stars, tunnel, etc.). Run ./screensaver.sh to choose or randomize. HN enjoys the whimsy but flags high CPU for some savers and cursor visibility. Others suggest using KDE’s plasma-wallpaper-application to make them real wallpapers/locks. Some note parallels to Emacs’s long-standing zone.el. Bash ≥3.2; quickstart is git clone && ./screensaver.sh.

- Comment pulse
  - Hide the cursor → Cursor visible during animation feels off; should default to tput civis and restore on exit — counterpoint: easy patch.
  - Whimsy improves onboarding → Tests live in a 'jury' folder that “judges” savers, making QA visible and fun.
  - Not new, but delightful → Several savers echo Emacs zone.el (circa 2000), showing enduring appeal of terminal art.

- LLM perspective
  - View: Cute terminal art meets real usability if it idles efficiently and hides UX papercuts.
  - Impact: Best for tinkerers, streamers, and Linux desktops; also a teachable playground for Bash control flow and TUI tricks.
  - Watch next: Publish per-saver CPU/frame-rate benchmarks, default cursor hiding, packaged installs (AUR/Homebrew), and guides for KDE/other DE wallpaper or lockscreen integration.
