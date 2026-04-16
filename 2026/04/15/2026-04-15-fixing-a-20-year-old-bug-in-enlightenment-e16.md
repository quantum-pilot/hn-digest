# Fixing a 20-year-old bug in Enlightenment E16

- Score: 254 | [HN](https://news.ycombinator.com/item?id=47774789) | Link: https://iczelia.net/posts/e16-20-year-old-bug/

### TL;DR
A longtime Enlightenment E16 user tracks down a rare, 20‑year‑old freeze that happens when a specific long PDF window title is shown. The hang comes from a Newton-style search loop in the “middle-ellipsis” text-fitting routine that sometimes oscillates forever due to no iteration limit and tight convergence criteria. The fix adds an iteration cap, lower bounds on nuked characters and character width, and guarantees termination. HN discussion mixes nostalgic praise for Enlightenment with reflections on open-source longevity and desktop bloat.

---

### Comment pulse
- Deterministic hangs are a blessing → they give a reliable reproducer and clear success criteria—counterpoint: they’re less “fun” for bug-hunters than elusive heisenbugs.  
- Enlightenment nostalgia → remembered as flashy yet efficient; today it’s “lightweight” only relative to ever-heavier GNOME/KDE and modern desktop stacks.  
- Open source longevity → you can keep and fix old WMs indefinitely; some contrast this with GNOME’s opinionated changes and vendor lock-in on macOS/Windows.

---

### LLM perspective
- View: Numeric algorithms in UI layout must be treated like any other numerical method: add iteration caps, bounds, and robust fallbacks.  
- Impact: Window managers, toolkits, and browsers can harbor decades-old layout bugs that only appear on edge-case strings or fonts.  
- Watch next: Fuzz window titles and text layouts, add property-based tests around truncation/ellipsis logic, and audit other Newton-like searches in UI code.
