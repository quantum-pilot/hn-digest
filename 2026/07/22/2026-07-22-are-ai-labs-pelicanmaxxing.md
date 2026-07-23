# Are AI Labs Pelicanmaxxing?

- Score: 351 | [HN](https://news.ycombinator.com/item?id=49010129) | Link: https://dylancastillo.co/posts/pelicanmaxxing.html

- TL;DR  
  Dylan Castillo tests whether AI labs overfit (“pelicanmaxx”) to Simon Willison’s famous SVG benchmark: “a pelican riding a bicycle.” He prompts seven frontier models with 48 animal–vehicle combinations (1,008 SVGs), scores them using an LLM judge, and runs difficulty-adjusted regressions. Pelicans, bicycles, and the pelican‑bicycle combo all perform mediocrely with no statistically robust lab-specific boost. Composition patterns (e.g., always facing right) match broader biases, not memorization. HN discussion shifts toward SVG-wide optimization and benchmark gaming more generally.

- Comment pulse  
  Benchmarks invite overfitting → Like TPC/Quake-era tuning: you must excel just to be considered, but naive hard-coding gets exposed by adjacent tests.  
  Right-facing bikes → Likely inherited from photography and sales imagery showing the drivetrain; reinforces that models mimic data conventions, not mechanics understanding.  
  Quantitative vindication → Many are glad this undercuts casual “they trained on it” claims, though some argue limited generalization still can’t rule out targeted training.

- LLM perspective  
  View: Fun micro-study shows how to probe benchmark overfitting with cheap, systematic, multi-model experiments plus LLM judges.  
  Impact: Encourages community-run evals that pressure labs to avoid narrow benchmark gaming and disclose SVG/structured-output tuning.  
  Watch next: Replicate with multiple judges, larger grids, and different mediums (code, text tasks) to detect subtler benchmaxxing patterns.
