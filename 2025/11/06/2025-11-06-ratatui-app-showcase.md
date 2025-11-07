# Ratatui – App Showcase

- Score: 699 | [HN](https://news.ycombinator.com/item?id=45830829) | Link: https://ratatui.rs/showcase/apps/

- TL;DR
  - Ratatui’s showcase aggregates dozens of Rust terminal apps (gitui, yazi, bottom, taskwarrior‑tui, etc.), illustrating a vibrant TUI ecosystem for file management, monitoring, networking, APIs, and even games. HN credits the boom to modern GPU‑accelerated terminals and avoiding heavy GUI stacks, with debate over Rust’s “dreadful” GUI state versus genuine TUI preference. Commenters note GUI complexity (cyclic references, signals/slots), share resources and browsers (Lynx, w3m, Browsh), and see TUIs as a pragmatic middle ground between traditional CLIs and full desktop GUIs.

- Comment pulse
  - TUIs rising as GUIs are heavy and Rust GUI lags → terminals are simpler, testable, cross‑platform — counterpoint: many choose TUIs for their own merits.
  - Rust GUIs face ownership/cycle hurdles (parent–child refs, signal/slot patterns) → ergonomic mismatch slows Qt-like toolkits; Zed shows it’s possible, but bespoke.
  - Wish for a polished TUI web browser → existing Lynx/w3m/Browsh/chawan help; skeptics say text-cell rendering wastes GPU acceleration — counterpoint: reader-mode UX in-terminal suffices.

- LLM perspective
  - View: Ratatui turns the terminal into a consistent UI substrate for CRUD/data tooling without browser plumbing.
  - Impact: DevOps, data engineers, and backend teams can ship cross‑platform tools faster; fewer Electron apps for internal dashboards.
  - Watch next: Terminal protocol support (sixel, GPU shaders, Kitty text sizing) and accessibility/internationalization in TUIs; Ratatui roadmap on async/render performance.
