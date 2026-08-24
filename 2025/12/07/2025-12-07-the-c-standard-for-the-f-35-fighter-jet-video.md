# The C++ standard for the F-35 Fighter Jet [video]

- Score: 160 | [HN](https://news.ycombinator.com/item?id=46183657) | Link: https://www.youtube.com/watch?v=Gv4sDL9Ljww

### TL;DR

The video presents the Joint Strike Fighter’s 142-page C++ rules as a safety-critical subset that bans or constrains most language features to improve determinism, analyzability, and mission assurance. Topics include exceptions, recursion, cyclomatic complexity, mandatory control-flow handling, and forbidding heap allocation after initialization. It connects those rules to aerospace history and the shortage of Ada developers and tooling. Commenters compared satellite practices, debated whether the guidance transfers to ordinary embedded systems, and asked how static analysis and justified rule exceptions are handled.

### Comment pulse

- Fixed memory placement can aid degraded hardware → satellite software may patch around failed cells when variables retain known addresses.
- Ada lost on ecosystem availability → C++ offered more engineers, middleware, and tooling despite requiring a heavily restricted profile.
- Defensive branches help diagnosis → explicitly handling impossible states surfaces rare scale-dependent failures instead of silently ignoring them.

### LLM perspective

- View: Safety comes from a constrained, enforceable programming model, not from a language label alone.
- Impact: Real-time teams trade expressiveness and dynamic flexibility for predictable timing, memory behavior, and reviewability.
- Watch next: Enforcement tooling, approved deviations, modern drone workloads, and whether newer safety languages meet ecosystem needs.
