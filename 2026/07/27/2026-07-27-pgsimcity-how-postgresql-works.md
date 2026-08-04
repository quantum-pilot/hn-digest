# PGSimCity - How PostgreSQL Works

- Score: 884 | [HN](https://news.ycombinator.com/item?id=49063754) | Link: https://nikolays.github.io/PGSimCity/

### TL;DR

PGSimCity is an independent, open-source 3D visualization that models PostgreSQL internals as an animated city. Its creator labels it an early, unreviewed prototype likely to contain inaccuracies and invites corrections; running it requires JavaScript and WebGL2. Commenters admire the ambition and see potential for databases, Kubernetes, deployment systems, and debugging, but many find the tour visually overwhelming, transient, and hard to map back to concrete engine concepts. Their clearest request is an interactive query walkthrough with pausing, reduced overlays, and a visible start-to-finish path.

### Comment pulse

- Visual richness exceeds cognitive bandwidth → animated objects, flashing states, text boxes, and disappearing explanations obscure the underlying database metaphors.
- Tours should surrender control → users want pausing, manual progression, transparent or hideable overlays, and less screen obstruction.
- A query should anchor the lesson → tracing one request from parsing through output could organize foreground work and parallel background processes.

### LLM perspective

- View: Spatial metaphors teach systems only when each visual object has a stable, explicit mapping to a technical concept.
- Impact: A focused design could give learners intuition that static architecture diagrams rarely convey, especially for concurrency and scheduling.
- Watch next: User-test comprehension, add playback controls, validate explanations with PostgreSQL experts, and measure whether learners can predict query behavior.
