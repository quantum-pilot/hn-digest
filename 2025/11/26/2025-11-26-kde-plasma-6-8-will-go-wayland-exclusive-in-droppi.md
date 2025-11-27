# KDE Plasma 6.8 Will Go Wayland-Exclusive in Dropping X11 Session Support

- Score: 112 | [HN](https://news.ycombinator.com/item?id=46058531) | Link: https://www.phoronix.com/news/KDE-Plasma-68-Wayland-Exclusive

### TL;DR
KDE announced that starting with Plasma 6.8 its desktop will only support Wayland sessions, dropping the traditional X11 session while still running X11 apps via XWayland. Developers say most users already run Wayland and that focusing on one display stack enables new features and faster development. Plasma 6.7 will keep X11 sessions, with bugfixes into early 2027 for holdouts. HN discussion centers on Wayland’s remaining gaps: accessibility APIs, session stability, and mature remote-desktop workflows.

### Comment pulse
- Wayland a11y immature; each compositor rolls custom APIs, virtual keyboards lag. KDE FAQ notes plans, few guarantees — counterpoint: one backend may focus effort.  
- Some welcome KDE aligning with GNOME’s Wayland-only path but prefer Plasma’s configurability; GNOME criticized as rigid despite earlier Wayland maturity.  
- Users report compositor crashes taking down whole Wayland sessions, unlike recoverable X11; remote desktop workflows (x11vnc-style) remain patchy despite KRDP, GNOME Remote Desktop, wayvnc suggestions.

### LLM perspective
- View: Dropping X11 sessions is overdue; dual-stack maintenance slows compositor innovation and discourages app developers from targeting Wayland-native features.  
- Impact: Short term pain for niche workflows (remote access, assistive tech, exotic GPUs); mainstream desktop users likely unaffected given XWayland shims.  
- Watch next: Key signals: a11y protocols maturing in wlroots/KWin, better crash-recovery patterns, and major distros shipping Plasma Wayland as sole option.
