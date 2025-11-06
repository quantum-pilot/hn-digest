# The shadows lurking in the equations

- Score: 247 | [HN](https://news.ycombinator.com/item?id=45823141) | Link: https://gods.art/articles/equation_shadows.html

- TL;DR
    - A site showcases “fuzzy graphs”: color-coding how much an equation F(x,y)=0 is violated (z=|F(x,y)|), highlighting near-solutions and gradients. HN argues it’s a decades-old heatmap/error-surface idea; examples map to standard 3D surfaces and are reproducible in Desmos/CalcPlot3D, with sign-aware plots often better than absolute value. The author concedes overhyped novelty but defends pedagogical value. Commenters note it also surfaces flat valleys and identifiability issues known in optimization.
    - _Content unavailable; summarizing from title/comments._
- Comment pulse
    - This is a |F(x,y)| heatmap/3D plot; decades-old. Desmos reproduces examples; drop abs to show sign; surfaces like hyperbolic paraboloid reappear.
    - Not a “graph of the equation,” just a visualization transform; binary equality slice vs continuous error field — counterpoint: framing helps beginners see near-solutions/structure.
    - Shows error gradients and flat valleys; useful to explain optimization behaviour, unidentifiable models, and failure with noise on too-flat error surfaces.
- LLM perspective
    - View: Call it error-surface or level-set visualization; drop “new graphing” claims and emphasize pedagogy and intuition.
    - Impact: Teachers, ML/control engineers, and graphing tools could add near-solution overlays and sign-aware colormaps.
    - Watch next: Side-by-side with Desmos; benchmarks on learning gains; noise-aware rendering; performance on dense grids.
