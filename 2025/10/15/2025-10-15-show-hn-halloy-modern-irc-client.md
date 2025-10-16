# Show HN: Halloy – Modern IRC client

- Score: 276 | [HN](https://news.ycombinator.com/item?id=45590949) | Link: https://github.com/squidowl/halloy

- TL;DR
    - Halloy is a cross‑platform, Rust + Iced GUI IRC client with modern IRCv3.2 features (SASL, DCC, notifications, themes) and packages on Flathub/Snap. HN likes its polish and as a learning reference for Iced, but flags two gaps: no screen‑reader accessibility yet (blocked on Iced’s roadmap) and missing tabs/tray, which hurts multi‑server power users. Workarounds exist (buffer=replace-pane), some prefer Quassel, while others report smooth daily use with soju bouncers and praise Rust’s native, single‑binary distribution.

- Comment pulse
    - Accessibility missing → Iced lacks screen‑reader support; roadmap targets a future release. — counterpoint: planned, but timeline uncertain for users needing it now.
    - Tabs/tray ergonomics lacking → Multi‑server setups feel unwieldy; no minimize‑to‑tray; workaround: set buffer to replace‑pane; some stick with Quassel.
    - Developer take → Halloy is a strong Iced showcase; Rust favored for safety, single binary, cross‑platform; alternatives like GTK exist, Electron avoided.

- LLM perspective
    - View: Lean, native IRC shows Rust+Iced can replace Electron for real desktop apps.
    - Impact: Encourages Iced adoption; pressures Rust GUIs to prioritize a11y, tabs, and tray UX.
    - Watch next: Iced screen‑reader milestone, Halloy tabs/tray roadmap, memory/CPU benchmarks vs Electron/Tauri.
