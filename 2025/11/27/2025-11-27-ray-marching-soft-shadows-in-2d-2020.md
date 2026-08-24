# Ray Marching Soft Shadows in 2D (2020)

- Score: 175 | [HN](https://news.ycombinator.com/item?id=46066695) | Link: https://www.rykap.com/2020/09/23/distance-fields/

### TL;DR

A WebGL demo renders stylized 2D shadows from a distance field. For each pixel, ray marching advances toward the light by the known safe distance to the nearest glyph, avoiding slow one-pixel steps and missed obstacles. Softness comes from minimizing the ratio between scene distance and ray progress, then applying quadratic light falloff; the result is attractive rather than physically exact. Commenters praised the interactive explanation, suggested clearer affordances, and discussed cone tracing, gradients, blur, banding, and mobile noise.

### Comment pulse

- Gradient-aware stepping may reduce samples → surface orientation helps, but curved geometry can require higher derivatives to preserve safe bounds.
- Softness trades accuracy for aesthetics → jitter reduces banding but adds grain — counterpoint: post-processing blur might hide both artifacts cheaply.
- Interactive figures need signposting → readers missed that several images could be dragged or touched.

### LLM perspective

- View: The tutorial succeeds by exposing an intuitive approximation and its visible compromises rather than claiming physical realism.
- Impact: Game and web developers gain a compact shader technique for typography, lighting, antialiasing, or depth-of-field effects.
- Watch next: Gradient-aware stepping, cone coverage, adaptive limits, artifact comparisons, mobile performance, and clearer demo captions.
