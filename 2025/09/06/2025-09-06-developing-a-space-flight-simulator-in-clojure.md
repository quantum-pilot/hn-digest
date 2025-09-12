# Developing a Space Flight Simulator in Clojure

- Score: 228 | [HN](https://news.ycombinator.com/item?id=45145794) | Link: https://www.wedesoft.de/software/2025/09/05/clojure-game/

TL;DR
- A solo dev spent ~5 years building a space flight simulator in Clojure, tackling graphics first: Bruneton atmosphere LUTs, shader templating, and planet rendering from NASA datasets tiled into quad‑trees and packed for Steam. The stack relies on LWJGL, Jolt via Coffi, tools.build, ZGC, and profiling to keep the JVM snappy. HN discussion centered on whether language choice (Clojure/Jank) matters versus engines, Guile vs Clojure ergonomics, and suggestions like ham‑fisted/Neanderthal for numerical hot paths.

Comment pulse
- Language hype won’t revolutionize indie games → tool ecosystems (Unity/Unreal/Godot) and content dominate—counterpoint: niche languages can attract dedicated communities and workflows.
- Guile vs Clojure features → Guile has multimethods and fast hash maps; Clojure’s dispatch, vectors, and ergonomics feel more practical to some.
- DIY engine admiration → building without Unity/Unreal impresses; veterans note rolling custom engines was common and still viable for hobbyists.

LLM perspective
- View: Clojure can drive real‑time 3D if native bindings, profiling, and data‑oriented structures are used carefully.
- Impact: Validates JVM viability for games; encourages scientific data pipelines (SPICE, NASA tiles) inside functional codebases.
- Watch next: Benchmarks vs Unity/Godot baselines, Jolt FFI stability, modding sandbox design, performance of ham‑fisted/Neanderthal on hot loops.
