# Dillo, a multi-platform graphical web browser

- Score: 193 | [HN](https://news.ycombinator.com/item?id=45826266) | Link: https://github.com/dillo-browser/dillo

- TL;DR
  - Dillo, a tiny multi‑platform browser dating to 1999, remains beloved for speed on low‑power machines. The maintainer is moving off GitHub to a minimal, JS‑free, self‑hosted stack with CI via git hooks; GitHub will later be archived. HN asked for a supported‑features list, warned about confusion with the old domain, and compared Dillo to newer lightweight engines (e.g., Blitz/Servo) pursuing modern CSS support, while debating cgit vs Forgejo and sharing heavy nostalgia.
  - _Content unavailable; summarizing from title/comments._

- Comment pulse
  - Self‑hosting shift → nginx/cgit/bug tracker, CI via hooks; JS‑free so Dillo can develop Dillo — counterpoint: why not Forgejo/Gitea; beware old domain confusion.
  - Use case → Ultra‑light browsing revives very old laptops and Pine Tab 2; users bookmark lightweight sites to avoid missing features.
  - Ecosystem → Blitz reuses Servo components, targets modern CSS (Flexbox/Grid/floats); open questions: JavaScript engine choice and Dillo’s supported elements list.

- LLM perspective
  - View: Dillo optimizes for simplicity, not web completeness; self‑hosting aligns with that philosophy and reduces external dependencies.
  - Impact: Benefits low‑spec devices, hobbyist OSes, offline/embedded setups; smaller attack surface for development infrastructure.
  - Watch next: Publish compatibility matrix, clarify domain ownership, timeline for GitHub archival, and stance on JS support or integrations.
