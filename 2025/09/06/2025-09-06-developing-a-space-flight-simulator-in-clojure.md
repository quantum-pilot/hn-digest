# Developing a Space Flight Simulator in Clojure

- Score: 228 | [HN](https://news.ycombinator.com/item?id=45145794) | Link: https://www.wedesoft.de/software/2025/09/05/clojure-game/

### TL;DR

After nearly five years, a developer has built the difficult foundations of a cross-platform space-flight simulator in Clojure: planetary terrain, atmospheric scattering, shadows, volumetric clouds, orbital data, vehicle physics, and native OpenGL/Jolt integration. The implementation leans on immutable data and controlled concurrency, precomputes expensive lookup tables, packages 655,350 terrain files into randomly accessible archives, profiles JVM performance, and uses ZGC. A playtest exists, but cockpit, Moon, station, sound, controls, and launch infrastructure remain future work.

### Comment pulse

- Clojure developers praise the technical ambition and suggest performance libraries, while debating whether functional languages appeal broadly to indie developers.
- Readers especially admire building a custom graphics stack instead of relying on Unity or Unreal.

### LLM perspective

- View: Clojure works here because the developer engineered around its boundaries instead of treating graphics and native integration as effortless.
- Impact: The project demonstrates JVM functional tooling across simulation, asset pipelines, concurrency, profiling, and low-level foreign interfaces.
- Watch next: Flight completeness, performance under full workloads, Windows parity, mod sandboxing, and conversion from playtest to release.
