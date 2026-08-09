# Claude Tips for 3D Work

- Score: 195 | [HN](https://news.ycombinator.com/item?id=47365299) | Link: https://www.davesnider.com/posts/claude-3d

### TL;DR

Claude can write much of a web project after a human establishes architecture, but it struggles to reason about occlusion and spatial relationships in complex 3D scenes. Dave Snider’s remedy is to make visual state machine-readable: scripts regenerate STLs, drive the application, position cameras, capture multiple views, expose layout data, and place debug markers. Claude then inspects screenshots and repeats changes until geometry matches the request without human-fed images. HN endorsed tooling as shared language, while users reported both successful CAD scripting and costly or unreliable modeling loops.

### Comment pulse

- Screenshot validation works → rendered views expose mistakes coordinates and logs miss — counterpoint: repeated image passes can quadruple model costs.
- Human ownership varies → the author keeps design and early architecture; others would delegate conventional code but guard sensitive or novel systems.
- CAD results remain uneven → one FreeCAD tower succeeded immediately, while enclosure attempts needed decomposition and repeated feature-level iteration.

### LLM perspective

- **View:** Agent reliability improves when environments expose inspectable state and a closed correction loop.
- **Impact:** 3D teams must invest in capture, camera, selection, and marker tooling before delegating visual changes.
- **Watch next:** Image-loop cost, geometry regression tests, scene-understanding benchmarks, and reusable CAD inspection interfaces.
