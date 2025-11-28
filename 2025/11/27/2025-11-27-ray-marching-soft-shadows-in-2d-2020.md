# Ray Marching Soft Shadows in 2D (2020)

- Score: 175 | [HN](https://news.ycombinator.com/item?id=46066695) | Link: https://www.rykap.com/2020/09/23/distance-fields/

- TL;DR  
Kaplan walks through a 2D WebGL lighting demo that uses signed distance fields and ray marching to render shadows from text. Instead of stepping 1px along each light ray, the shader advances by the distance-to-nearest geometry, guaranteeing no occluder is skipped and staying fast. Soft shadows come from tracking the minimum sceneDist/rayProgress ratio along the ray plus quadratic light falloff, with jitter to hide banding. HN discusses artifacts, UX of interactive figures, cone-tracing interpretations, and gradient-based optimizations.

- Comment pulse  
  - Interactive demo UX needs work → many images are clickable but unlabeled; noise and banding suggest a final blur pass could cheaply hide artifacts.  
  - Soft shadows as cone tracing → treating each ray as a thin cone explains partial coverage and extends naturally to depth-of-field and antialiasing effects.  
  - Use SDF gradients to step further → gradient-informed marching can cut iterations, but robust step bounds for curved geometry are mathematically tricky and reduce simplicity.

- LLM perspective  
  - View: Distance-field ray marching plus a simple heuristic ratio yields attractive 2D soft shadows with minimal shader complexity.  
  - Impact: Useful for games, UI, and motion graphics needing cheap soft lighting on vector text or abstract 2D geometry.  
  - Watch next: benchmark gradient-guided steps, temporal reprojection, and blue-noise jitter to reduce banding without heavy blur or extra samples.
