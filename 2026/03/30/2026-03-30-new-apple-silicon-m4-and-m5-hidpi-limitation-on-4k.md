# New Apple Silicon M4 and M5 HiDPI Limitation on 4K External Displays

- Score: 301 | [HN](https://news.ycombinator.com/item?id=47569502) | Link: https://smcleod.net/2026/03/new-apple-silicon-m4-m5-hidpi-limitation-on-4k-external-displays/

### TL;DR
Apple’s M4/M5 Macs silently drop support for “true” HiDPI on ordinary 4K external monitors. Where M2/M3 could render at 7680×4320 and downscale (“looks like 3840×2160” with sharp text), M4/M5 now cap the HiDPI backing buffer at 6720 pixels wide, limiting users to a smaller “3360×1890 HiDPI” or a full 4K mode with blurry low‑DPI text. The root cause is a new per‑sub‑pipe framebuffer budget in the display driver, which only Apple can change; community workarounds don’t bypass it.

---

### Comment pulse
- Escalate to Apple leadership → Several report past display bugs only got fixed after emailing Tim Cook; others note partial, hacky fixes and more regressions followed.
- Painful workarounds → Users describe extreme contortions with BetterDisplay, DisplayLink, multi-virtual-monitors to get sharp, high-refresh UIs—counterpoint: some happily use low-DPI 4K and don’t notice fuzziness.
- Why 8K backing on 4K? → macOS text/UI rendering is tuned for 2× scale; overscaled framebuffers then downscaled yield sharper text than native 1× or fractional scaling.

---

### LLM perspective
- View: This looks like an Apple display-controller resource policy change that accidentally downgraded non-Apple 4K ergonomics.
- Impact: Power users with 4K externals on M4/M5 get worse text clarity or less workspace vs older Macs, harming “just works” credibility.
- Watch next: macOS point releases adjusting IOMFBMaxSrcPixels, dynamic per-pipe allocation, or explicit “full HiDPI” toggle for external displays.
