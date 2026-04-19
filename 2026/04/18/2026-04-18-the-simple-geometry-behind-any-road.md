# The simple geometry behind any road

- Score: 120 | [HN](https://news.ycombinator.com/item?id=47788207) | Link: https://sandboxspirit.com/blog/simple-geometry-of-roads/

## TL;DR
An indie dev describes a geometric method for generating roads in games using only lines and circular arcs instead of offset Bezier splines. Roads are defined by cross‑section “profiles”; between two profiles, the engine constructs fillets: arc‑then‑line or S‑shaped combinations found via a cubic Hermite spline–based intermediary profile. Edge cases are largely avoided by tool‑level placement constraints. HN readers discuss how this differs from real‑world clothoid‑based design and the implications for vehicle physics and 3D geometry.

## Comment pulse
- Game curves vs engineering curves → Real roads, railways use clothoids for continuous curvature and jerk; author approximates them with chained arcs, accepting non‑ideal offsets.  
- Lateral force discontinuity → Straight‑to‑arc fillets cause instantaneous lateral acceleration; bad for realism — counterpoint: games can cheaply smooth forces or animations separately.  
- Beyond 2D aesthetics → Readers connect this to transit‑map styling, 3D alignment and superelevation, and motion‑planning problems like jerk‑limited toolpaths for 3D printers.  

## LLM perspective
- View: Treat this as a pragmatic CAD‑inspired modeler for artists, not a highway‑engineering simulator; prioritize controllable shapes over physical optimality.  
- Impact: Could simplify procedural city tools, racing‑game track editors, and indie engines that misuse Bezier offsets and suffer artifacts.  
- Watch next: Extend constructions to 3D (grade, banking), benchmark against clothoid approximations, and expose controls like curvature or comfort limits.
