# The C++ standard for the F-35 Fighter Jet [video]

- Score: 160 | [HN](https://news.ycombinator.com/item?id=46183657) | Link: https://www.youtube.com/watch?v=Gv4sDL9Ljww

### TL;DR

The supplied video description presents the F-35 Joint Strike Fighter C++ standard as a deliberately restricted subset designed for safety-critical aviation software. It says the video covers aircraft-software history, the Pentagon’s language proliferation, exceptions, recursion, cyclomatic complexity, memory preallocation, and future safety practices. Comments add that C++ was selected partly because Ada talent, middleware, and tooling were scarce, and highlight rules such as avoiding operational heap allocation and requiring explicit final branches. Because only a description is supplied, detailed historical claims remain unverified here.

### Comment pulse

- Readers said workforce and ecosystem availability, not language purity alone, drove the choice of restricted C++ over Ada.
- Satellite developers described fixed memory placement as useful for diagnosing and patching around failed memory cells.
- Commenters wanted to know how rules are statically enforced and how often projects approve exceptions.

### LLM perspective

- View: Safety standards trade language expressiveness for analyzability, predictable resources, and reviewable control flow.
- Impact: The restricted subset demands specialized tooling and discipline beyond ordinary embedded C++ practice.
- Watch next: Examine the 142-page standard, enforcement tooling, approved deviations, and evidence from deployed systems.
