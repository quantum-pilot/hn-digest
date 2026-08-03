# Meshdiff – visually compare two STL versions in the browser, client-side

- Score: 171 | [HN](https://news.ycombinator.com/item?id=49143479) | Link: https://meshdiff.com/

### TL;DR
Meshdiff is a browser-based, fully client-side tool for visually comparing two STL 3D models, useful for 3D printing and CAD change review. It shows model differences without uploading files, fitting the “local-first” trend of WebGL/three.js/wasm apps. Hacker News commenters like the concept and suggest synchronized viewports, more precise highlighting of geometric changes (scale/shift/rotation), and integration into developer workflows such as GitHub PR previews for 3D assets.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Add synchronized/locked views → rotating one viewport should rotate the others, improving side‑by‑side comparison efficiency.
- Clarify terminology → many initially thought “STL” meant C++ “Standard Template Library”; it’s actually the common stereolithography file format for 3D printing.
- Extend workflow integration → embed as GitHub PR/branch diff viewer and highlight exact dimensional/transform deltas for robust 3D review.

---

### LLM perspective
- View: This fits a growing niche of browser-native inspection tools replacing heavyweight desktop viewers for focused tasks like diffs.
- Impact: Improves review quality for hardware teams, indie makers, and OSS CAD repos by making visual diffs trivial to share.
- Watch next: CI integrations, numeric tolerance-based diffing, and richer camera/annotation tools will determine real adoption in professional pipelines.
