# CSS-Doodle

- Score: 112 | [HN](https://news.ycombinator.com/item?id=47000164) | Link: https://css-doodle.com/

### TL;DR

CSS-Doodle is an MIT-licensed web component that turns CSS-like rules into generative graphics and animations. It creates a Shadow DOM grid of cells, then adds selectors, shorthand properties, randomness, math, SVG, shapes, plotting, and GLSL shaders. Authors can install it through npm or a CDN, seed random output for repeatable snapshots, update a doodle programmatically, and export images. Commenters admired how little code produces varied patterns, while debating whether its declarative JavaScript implementation is genuinely CSS or would fit better as a canvas library.

### Comment pulse

- Expressiveness impressed readers → compact aliases and randomized regeneration produce unexpectedly varied artwork from a few declarations.
- CSS-versus-JavaScript framing split opinion → supporters value declarative layout; critics call it a CSS-flavored JavaScript drawing framework.
- DOM grids invite a canvas comparison → the supplied discussion identifies no decisive use case favoring either rendering model.

### LLM perspective

- View: Its strongest idea is a small visual language built atop familiar browser primitives, not strict adherence to CSS.
- Impact: Web artists can prototype repeatable patterns without assembling DOM grids, SVG, randomness, and export tooling themselves.
- Watch next: Browser performance on large grids, accessibility, shader portability, production adoption, and guidance on choosing DOM versus canvas.
