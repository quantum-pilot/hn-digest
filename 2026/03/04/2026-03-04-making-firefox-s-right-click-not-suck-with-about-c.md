# Making Firefox's right-click not suck with about:config

- Score: 233 | [HN](https://news.ycombinator.com/item?id=47251480) | Link: https://joshua.hu/firefox-making-right-click-not-suck

### TL;DR

On macOS, Firefox’s context menu can reach 26 rows, so the author maps 13 `about:config` switches that remove translation, screenshots, text-fragment links, cleaned-link sharing, accessibility inspection, AI chat and previews, OCR, visual search, autofill, Services, and printing. The result drops to 15 rows, but several switches disable entire features, while remaining items require `userChrome.css` or cannot be removed cleanly. The proposed real fix is a toolbar-style context-menu editor. Commenters favored configurability while defending some apparent clutter as established interface convention.

### Comment pulse

- Vivaldi’s editable menus were the recurring model: preserve power features while letting each user remove noise.
- Disabled commands preserve location and discoverability; ellipses signal that another dialog or input step follows.
- Some criticized the article’s hostility; counterpoint: unwanted AI and privacy-sensitive defaults make anger understandable.

### LLM perspective

- **View:** The problem is not menu length alone, but Firefox coupling visibility controls to feature availability.
- **Impact:** A native editor could serve minimalists without silently disabling printing, translation, or accessibility tools.
- **Watch next:** Whether Mozilla exposes per-command visibility independently of feature flags and custom CSS.
