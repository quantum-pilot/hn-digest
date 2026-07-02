# Box3D, an open source 3D physics engine

- Score: 395 | [HN](https://news.ycombinator.com/item?id=48745445) | Link: https://box2d.org/posts/2026/06/announcing-box3d/

- TL;DR
    - Box3D is a new open source 3D rigid‑body physics engine by Box2D creator Erin Catto, entering a sparse ecosystem of modern FOSS 3D physics libraries. Commenters highlight Box2D’s deep influence on indie games and RL benchmarks, and expect Box3D’s clean C API to be similarly attractive. Determinism across platforms is a key concern for networked and replayable games, and people note that robust 3D physics still involves hard trade‑offs in collision handling and numerical stability.
    - *Content unavailable; summarizing from title/comments.*

- Comment pulse
    - Box2D’s legacy → Powered hits like Angry Birds; creator initially went uncredited until confronted at a talk, illustrating how invisible foundational libraries often are.
    - Sparse open 3D engines → Aside from ODE, Bullet, Newton Dynamics and Jolt, options are few, so a modern, ergonomic C‑API engine is welcomed.
    - Determinism and difficulty → Cross‑platform determinism for networking/replays is desired; floating‑point quirks and collision trade‑offs complicate this — counterpoint: disallowing -ffast-math suggests intent.

- LLM perspective
    - View → If Box3D proves as clean and stable as Box2D, it may become the default FOSS 3D engine.
    - Impact → Open, well‑documented 3D physics lowers dependence on Unity/Unreal internals, helping custom engines, novel games, and reproducible simulation research.
    - Watch next → Determinism guarantees, language bindings, and benchmarks against Bullet, Jolt, and commercial engines will decide real‑world adoption.
