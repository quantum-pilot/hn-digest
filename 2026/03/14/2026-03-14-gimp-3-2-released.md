# GIMP 3.2 released

- Score: 198 | [HN](https://news.ycombinator.com/item?id=47380465) | Link: https://www.gimp.org/news/2026/03/14/gimp-3-2-released/

- TL;DR  
  GIMP 3.2 adds its first big wave of non-destructive editing: link layers that reference external images, vector layers from paths, and a revamped MyPaint brush tool. Text editing, CMYK soft-proofing, PSD/SVG/PDF handling, and UI ergonomics all improve, while babl/GEGL get matching releases. HN discussion centers on how non-destructive transforms work under the hood, whether the current UI is intuitive enough, and long-running tensions over save vs export behavior for formats like JPEG.

- Comment pulse  
  - Linked/vector layers now keep a transform matrix instead of re-rasterizing, enabling multiple resizes without quality loss—counterpoint: some see destructive scaling as intuitive, historically consistent.  
  - Non-destructive editing feels bolted onto a destructive UI; users request node-based graphs, while devs cite GTK4 limits and others enjoy stored edit pipelines.  
  - Save vs export debate: some remap Ctrl+S to Overwrite JPEG; others insist XCF-native saving protects layers and non-destructive intent, suggesting simpler tools for quick edits.

- LLM perspective  
  - View: GIMP 3.2 pushes firmly toward non-destructive, multi-format workflows while keeping the classic raster-editing mental model mostly intact.  
  - Impact: Power users, painters, and print designers gain flexibility; casual editors may stay confused by non-destructive layers and save/export distinctions.  
  - Watch next: Node-based compositing, full-scene non-destructive transforms, GTK4 migration, and streamlined keyboard/mode defaults to reconcile pro workflows with simplicity.
