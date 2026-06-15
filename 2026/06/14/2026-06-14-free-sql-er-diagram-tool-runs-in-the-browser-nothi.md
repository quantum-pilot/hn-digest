# Free SQL→ER diagram tool, runs in the browser, nothing uploaded

- Score: 351 | [HN](https://news.ycombinator.com/item?id=48523992) | Link: https://sqltoerdiagram.com/

## TL;DR
A browser-based, open-source tool turns SQL `CREATE TABLE` / `ALTER TABLE` into an interactive ER-style diagram with drag-and-drop layout, notes, and PNG/SVG export. It runs entirely client-side, keeping schemas local, and encodes projects directly into the URL instead of using a backend or user accounts. HN readers highlight its smooth performance with large schemas, debate how strictly an ER diagram can be derived from SQL, and discuss implementation tricks like canvas rendering and surgical SQL editing.

---

## Comment pulse
- Mobile-first UX shines → panning, zooming, selection, and editing feel native on phones; some want the diagramming engine reusable beyond ER diagrams.
- ER vs tables distinction → purists argue SQL yields only physical diagrams, not conceptual ER models—counterpoint: for everyday schema exploration, table-level graphs are usually sufficient.
- Implementation/ops concerns → URL-encoded schemas may hit length limits; questions about license clarity, plus requests for straight-line connectors and view-based sub-diagrams.

---

## LLM perspective
- View: This exemplifies a pattern: devtools moving fully client-side, eliminating signup, telemetry, and vendor lock-in for everyday workflows.
- Impact: Teams with regulated or proprietary databases gain a safe, disposable way to explore unfamiliar schemas without VPN-accessible services.
- Watch next: Benchmarks on very large schemas, import-from-live-DB connectors, and modularizing the canvas engine for general-purpose diagramming.
