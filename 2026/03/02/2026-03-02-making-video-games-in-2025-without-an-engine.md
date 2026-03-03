# Making Video Games in 2025 (without an engine)

- Score: 395 | [HN](https://news.ycombinator.com/item?id=47176576) | Link: https://www.noelberry.ca/posts/making_games_in_2025/

### TL;DR
Berry (co-creator of Celeste) argues that in 2025, small teams can happily skip big “do-everything” engines like Unity/Unreal and instead build thin, focused stacks on mature libraries. He uses C# with .NET hot reload, SDL3 (plus a small C# wrapper) for cross‑platform windowing/input/rendering, FMOD for complex audio, and Dear ImGui + reflection for quick custom tools. Native AOT and SDL3’s console ports make C# viable on all major platforms. Engines are still great for large, tech‑heavy or 3D projects—this is a values and scope choice, not dogma.

---

### Comment pulse
- Custom engine works when you’re experienced and keep scope tight → otherwise it becomes a seductive side project that kills actually finishing the game.  
- Off‑the‑shelf engines shine for big teams/AAA ambitions → shared tools let artists, designers, and programmers work in parallel; UE5 especially for photorealism and cinematics — counterpoint: UE5 workflows, performance, and hypey features draw criticism.  
- Some devs thrive on bespoke stacks (e.g., Metropolis 1998 on custom C++/SFML) → deep understanding, minimal friction, small binaries; modern engines can also homogenize how games “feel.”

---

### LLM perspective
- View: Treat “engine vs no engine” as a project‑fit decision; align tooling with game scope, team size, and your tolerance for plumbing.  
- Impact: Solo/small indies gain from lightweight frameworks; content‑heavy or cinematic projects still benefit greatly from Godot/Unity/Unreal ecosystems.  
- Watch next: Benchmarks of Native AOT C# on consoles, SDL3 adoption, and real‑world case studies of mid‑size studios moving off commercial engines.
