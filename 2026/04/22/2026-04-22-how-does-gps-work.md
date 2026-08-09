# How does GPS work?

- Score: 212 | [HN](https://news.ycombinator.com/item?id=47861087) | Link: https://perthirtysix.com/how-the-heck-does-gps-work

### TL;DR

GPS estimates distance from signal travel time: each satellite supplies a sphere, three narrow it to a usable 3-D point, and a fourth lets the receiver solve clock offset alongside position. Receivers combine 8–12 satellites, prefer well-spread geometry, filter building reflections, and can also use GLONASS, Galileo, and BeiDou. Satellite clocks require relativistic modeling. Readers liked the interactive explanation but challenged its claim that an uncorrected 38-microsecond daily satellite-clock drift directly becomes roughly 10 km of position error, because solving receiver clock bias absorbs common offsets.

### Comment pulse

- Fundamental ground stations maintain the reference frame using quasar interferometry, inter-station comparisons, and satellite laser ranging, even tracking continental drift.
- Engineers wanted visible equations and a clearer approximation: receiver clock frequency is stable briefly, while its fixed time offset remains unknown.
- Interactive 3-D teaching impressed readers — counterpoint: claims that AI was necessary for the visualization drew skepticism.

### LLM perspective

- Correct the relativity section by separating common clock bias from residual orbit- and satellite-specific timing errors.
- Add an equation recap showing the four unknowns, linearization, convergence, and why one geometric solution is discarded.
- Connect the visualization to live receiver data only with explicit permission and a no-upload mode.
