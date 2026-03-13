# Avoiding Trigonometry (2013)

- Score: 202 | [HN](https://news.ycombinator.com/item?id=47348192) | Link: https://iquilezles.org/articles/noacos/

### TL;DR
Quilez argues that internal 3D graphics code should avoid trigonometric functions and angles, and instead work directly with vectors, dot products, and cross products. He shows a common “align object to direction” routine that computes an angle via `acos(dot)` and then feeds it into `sin`/`cos`, and replaces it with a purely vector-based formula derived from dot/cross relationships. This removes clamps, normalizations, roots, and trig, improving stability and clarity. HN discusses rational trigonometry, complex/quaternion representations, and the trade‑off between intuitive angle APIs and robust internals.

---

### Comment pulse
- Vector-first math → Dot/cross, complex numbers, quaternions, or spinors can encode rotations without trig, avoiding gimbal lock, NaNs, and fragile special cases.  
- Angle-based APIs → Angles are intuitive abstractions; performance/precision rarely bottlenecks — counterpoint: in games/sims rare trig bugs surface as nasty, long-tail glitches.  
- Broader math angles → Links to Rational Trigonometry, Householder reflections, geometric/geometric projective algebra; suggests alternative “foundations” where angles are secondary or absent.

---

### LLM perspective
- View: Use trig only at system boundaries; keep core math in vectors, matrices, or quaternions for robustness.  
- Impact: Graphics engines, physics, robotics can see fewer numerical edge cases and simpler debugging paths.  
- Watch next: Compare real-world engine bugs and performance under trig-heavy vs vector/quaternion pipelines; update libraries to hide vector internals behind angle-friendly APIs.
