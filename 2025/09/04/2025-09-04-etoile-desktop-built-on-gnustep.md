# Étoilé – desktop built on GNUStep

- Score: 251 | [HN](https://news.ycombinator.com/item?id=45123003) | Link: http://etoileos.com/

- TL;DR
    - Étoilé pitched a GNUstep-based, user-first desktop that hides files/processes and bakes in system-wide versioning, collaboration, and composable Services. With news last updated in 2012–2014, it appears dormant. HN reminisces about its Smalltalk/Lisp-inspired ambition and contrasts it with today’s security- and platform-driven priorities. Discussion surfaces active GNUstep desktops, explores hardware/software paths like CHERI and Objective‑S for safe, componentized systems, and debates whether Linux should converge on one framework or embrace fragmentation—and what that means for desktop app viability.

- Comment pulse
    - Why it faded → no distro packaging, GNOME chose GTK, Obj‑C features lagged; community mindshare moved on.
    - Vision lives on → CHERI aims safe composability for small components; Objective‑S explores Smalltalk-like environments.
    - One framework wish vs fragmentation → some want standardization; others value diversity and distrust central control — counterpoint: fragmentation hinders desktop app dev.

- LLM perspective
    - View: Activity-centric desktops need baked-in persistence, identity, and capability-mediated sharing; retrofitting that onto POSIX/process/file metaphors is brittle.
    - Impact: If achieved, would lower integration costs for collaborative apps and enable safe end-user programmability across components.
    - Watch next: Empirical prototypes: per-document timelines, cross-app live collaboration, component sandboxes with zero-copy sharing; measure latency, memory, and failure isolation.
