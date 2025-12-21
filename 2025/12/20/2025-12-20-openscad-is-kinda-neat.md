# OpenSCAD is kinda neat

- Score: 182 | [HN](https://news.ycombinator.com/item?id=46337984) | Link: https://nuxx.net/blog/2025/12/20/openscad-is-kinda-neat/

- TL;DR  
  - Author reimplements a parametric AA/AAA battery holder, originally in Fusion 360, using OpenSCAD’s code-driven modeling. With a few variables they generate customized organizers without heavy GUI CAD, illustrating OpenSCAD’s strengths for simple, repeatable printable parts. Hacker News comments split: some praise its small conceptual surface, git master performance, and libraries like BOSL2; others hit hard limits—no constraints, awkward fillets, lots of math—and point to Python/JS/SDF-based alternatives and mainstream parametric CAD for complex or highly constrained designs.

- Comment pulse  
  - OpenSCAD is neat but limited; SDF-based Python tools (sdf, fncad) give richer logic, easy operations on existing STLs, but weaker CAD interoperability.  
  - Fans love text-based parametric modeling: tiny language, git master renders faster, BOSL2 adds higher-level primitives; feels more controllable than nudging geometry in GUIs.  
  - Critics: absolute coordinates, lack of constraints and solid reasoning make real-world mechanical fits painful—counterpoint: GUI CAD still confusing for many casual users.

- LLM perspective  
  - View: OpenSCAD shines as a “code-first calipers companion,” not a full CAD replacement; perfect for brackets, jigs, organizers, adapters.  
  - Impact: Programmers get an easy on-ramp; complex assemblies with tight tolerances or fillets still require constraint-based CAD or SDF-based workflows.  
  - Watch next: Worth benchmarking OpenSCAD master, CadQuery/build123d, and SDF libraries on complex parametric parts, filleting strategies, and editing messy real-world STLs.
