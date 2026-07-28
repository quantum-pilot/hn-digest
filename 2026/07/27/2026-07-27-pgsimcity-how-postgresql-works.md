# PGSimCity - How PostgreSQL Works

- Score: 884 | [HN](https://news.ycombinator.com/item?id=49063754) | Link: https://nikolays.github.io/PGSimCity/

- TL;DR  
  PGSimCity is an open‑source, SimCity‑style 3D visualization of PostgreSQL internals, built with WebGL2. It aims to show processes, sessions, and scheduling as a living “city,” helping people grasp how the engine works. HN commenters find the idea exciting but the current prototype overwhelming: too many popups, auto‑advancing tours, and unclear metaphors make it hard to map visuals to database concepts. Suggestions center on simplifying the UX, adding interactive query walkthroughs, and reusing the approach for other complex systems.

- Comment pulse  
  Visualization is impressive but cognitively overloaded → dense animations, greebling, popups, and auto‑tour make it hard to build a coherent mental model.  
  UX should favor interaction over narration → users want to run their own queries and step through flows, not passively watch an info‑heavy scripted tour.  
  Concept has strong educational potential → could clarify scheduling, internals, or even Kubernetes/cloud systems—counterpoint: without clearer metaphors, it risks being more spectacle than teaching tool.

- LLM perspective  
  View: Treat this as a UX‑heavy educational product: prioritize learnability and progressive disclosure over maximal visual fidelity.  
  Impact: Best suited for engineers learning Postgres internals, trainers, and teams onboarding to database operations and performance tuning.  
  Watch next: Iterations adding query‑driven demos, reduced popup noise, and domain extensions (e.g., Kubernetes, debugging flows) with measured learning outcomes.
