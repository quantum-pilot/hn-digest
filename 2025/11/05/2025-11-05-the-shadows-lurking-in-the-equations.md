# The shadows lurking in the equations

- Score: 265 | [HN](https://news.ycombinator.com/item?id=45823141) | Link: https://gods.art/articles/equation_shadows.html

TL;DR
- The piece promotes “FuzzyGraph,” which colors the residual of an equation (how far LHS and RHS differ) to reveal hidden structure: singularity “black holes,” “shadow lines” from divided constraints, and “underwater islands” indicating near‑solutions that surface after small parameter changes. HN notes this is a residual heatmap (or 3D surface colored in 2D), long‑known in math/optimization, but agrees it’s a clean, didactic framing that surfaces gradients and near‑solutions well. The author concedes the intro oversold novelty and positions it as an alternate visualization.

Comment pulse
- Not new: it's a residual heatmap z=|F(x,y)|; replicate in Desmos/CalcPlot3D; Example 4 is a hyperbolic paraboloid; sign-aware plots capture symmetry better.
- Useful for intuition: reveals near-solutions and gradient shape; good pedagogy; author softens hype, frames as alternative view — counterpoint: calling it 'new graphing' misleads.
- Mathematical caveat: some equations reduce (cancel denominators), so "shadows" are artifacts; optimization view: flat error valleys imply unidentifiability under noise.

LLM perspective
- View: Residual heatmaps unify implicit curves and optimization landscapes; toggling signed vs absolute residual clarifies structure and symmetry.
- Impact: Educators, numerical methods courses, and model-fitting practitioners gain a quick intuition aid without 3D navigation friction.
- Watch next: Open-source the renderer; add contours, gradient arrows, and noise simulations; compare against standard level-set/contour plots on benchmark equations.
