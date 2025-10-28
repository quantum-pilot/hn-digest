# Rust cross-platform GPUI components

- Score: 460 | [HN](https://news.ycombinator.com/item?id=45719004) | Link: https://github.com/longbridge/gpui-component

- TL;DR
  - GPUI Component is a Rust desktop UI kit atop GPUI with 60+ native‑style components, themes, dock layouts, charts, Markdown/HTML, a fast editor with Tree‑Sitter, and virtualized tables/lists; optional Wry WebView. It already powers Longbridge Pro and inherits maturity from Zed’s GPUI. HN praises the breadth and responsiveness and sees it as a major step for Rust UIs, while noting huge dependency trees (especially GTK/libadwaita on Linux), framework‑owned event loops, and missing visual designers; several Qt comparison claims were challenged.

- Comment pulse
  - Most complete Rust UI kit → 60+ components; gallery runs well; adoption still early — counterpoint: GPUI is used in Zed and Longbridge Pro.
  - Dependency bloat concerns → 900–1000 crates; Linux pulls GTK/libadwaita due to server-side decorations; debate over many small crates vs monolith.
  - Framework vs library → owns event loop, complicates embedding; tooling gap: few visual designers; Slint shows a designer path.

- LLM perspective
  - View: Desktop-first Rust UI kit with breadth and performance; credible alternative to Iced/egui when web targets aren’t needed.
  - Impact: Small teams building native-feel tools; fintech and IDE-like apps gain charts, docking, editors without Electron or Qt.
  - Watch next: API stabilization, Windows/Linux polish, dependency trimming, visual designer/markup, and performance benchmarks against egui/Iced and Qt widgets.
