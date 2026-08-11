# Making Video Games in 2025 (without an engine)

- Score: 395 | [HN](https://news.ycombinator.com/item?id=47176576) | Link: https://www.noelberry.ca/posts/making_games_in_2025/

### TL;DR

Celeste developer Noel Berry argues that making a game without a general-purpose engine can reduce overhead when a small team needs only narrow, opinionated systems. His stack uses C#, SDL3 for cross-platform input and GPU abstraction, a thin custom framework, Dear ImGui for editors, simple asset scripts, FMOD for audio, and Native AOT for consoles. The goal is not an engine product but game-specific plumbing built only when required, preserving control, debuggability, portability, and long-term buildability. He recommends Godot or Unreal when their tooling or advanced 3D features fit.

### Comment pulse

- Custom code can fit stylized or mechanically focused games — counterpoint: Unreal’s mature authoring stack lets large multidisciplinary teams parallelize complex production.
- Veterans warned engine-building creates seductive checklist progress while the game stalls; add only proven necessities and generalize reusable code afterward.
- Readers linked shared engines to visual sameness, while others valued their familiar look and cited custom-engine performance advantages over UE5 remakes.

### LLM perspective

- **View:** This is a scope argument, not an anti-engine rule: choose the smallest stack that serves the actual game.
- **Impact:** Small teams gain control and longevity; complex productions risk rebuilding expensive collaboration, content, rendering, and deployment systems.
- **Watch next:** Team composition, 3D ambition, console certification, tool-building time, and whether custom plumbing accelerates playable milestones.
