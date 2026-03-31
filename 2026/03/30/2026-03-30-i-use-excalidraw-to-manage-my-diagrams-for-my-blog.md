# I use Excalidraw to manage my diagrams for my blog

- Score: 267 | [HN](https://news.ycombinator.com/item?id=47571376) | Link: https://blog.lysk.tech/excalidraw-frame-export/

- TL;DR  
  The author wanted a fast way to keep blog diagrams in sync with text, including light/dark variants. Manual Excalidraw exports took ~45 seconds per change, and a first attempt using a GitHub Action plus a renderer CLI was slow, buggy, and couldn’t run on an ARM Mac. They instead forked the Excalidraw VS Code extension so any frame named `export_<name>` is auto-exported to `<name>.light.exp.svg` and `<name>.dark.exp.svg`, enabling instant local preview. HN discusses Excalidraw’s UX issues, alternatives like Mermaid, and dark-mode SVG techniques.

- Comment pulse  
  Excalidraw UX feels brittle → users hit buggy arrow resizing, sticky auto-attachments, unreliable undo/redo, and missing features like long-stalled math mode.  
  Automation patterns vary → others embed Excalidraw directly into CMSs, wire it to Claude via MCP, or mix in Mermaid text diagrams plus post-processing.  
  SVG theming tradeoffs → CSS-based color adaptation could avoid duplicate files, but GitHub’s limited dark-mode SVG support keeps many on per-theme exports.

- LLM perspective  
  View: This is a classic “scratch your own itch” dev tool: small scope, huge subjective quality-of-life gain.  
  Impact: Anyone blogging technical content with Excalidraw gets reproducible, theme-aware diagrams without CI friction or manual export drudgery.  
  Watch next: Upstream Excalidraw/VS Code extension may adopt frame-based auto-export; worth tracking for standardized naming, theming, and multi-target outputs.
