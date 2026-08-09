# Open source CAD in the browser (Solvespace)

- Score: 273 | [HN](https://news.ycombinator.com/item?id=47586614) | Link: https://solvespace.com/webver.pl

### TL;DR

SolveSpace now offers an experimental browser build of its compact parametric 2D/3D CAD application, compiled with Emscripten from the latest development branch. It carries a performance penalty and browser-specific bugs, but the maintainers say small models are often quite usable. After its initial load it has no network dependencies, and the generated static files can be self-hosted. HN praised SolveSpace’s lightweight, direct interface for laser-cut parts, while debating whether mature desktop alternatives better serve complex work.

### Comment pulse

- A maintainer says chamfers and fillets top the roadmap, but general cases—especially three-way corners—remain exceptionally difficult.
- Dune 3D was proposed as a successor — counterpoint: it uses SolveSpace underneath, while FreeCAD offers broader capability.
- FreeCAD users praised its improved interface and depth, though one found rendering comparatively underdeveloped.

### LLM perspective

- **View:** Browser delivery fits SolveSpace because its compact architecture enables a useful tool without server infrastructure.
- **Impact:** Students, collaborators, and occasional makers gain zero-install access, while desktop remains safer for serious models.
- **Watch next:** Browser bug reports, performance on larger assemblies, persistence and file workflows, plus progress on edge finishing.
