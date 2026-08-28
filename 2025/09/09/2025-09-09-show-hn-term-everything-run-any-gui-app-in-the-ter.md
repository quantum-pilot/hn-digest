# Show HN: Term.everything – Run any GUI app in the terminal

- Score: 727 | [HN](https://news.ycombinator.com/item?id=45181535) | Link: https://github.com/mmulet/term.everything

### TL;DR

term.everything is a from-scratch Wayland compositor that renders Linux GUI applications inside a terminal, including across SSH. Ordinary terminals constrain output to their character grid, while image-capable terminals such as Kitty or iTerm2 can trade performance for full-resolution rendering. Demos show browsers, games, video, file managers, and nested terminals, but the TypeScript, Bun, and small C++ project is explicitly beta and some applications may fail or crash. Commenters see both playful experimentation and a possible remote-access tool.

### Comment pulse

- Readers compare it with Carbonyl and appreciate the project as both technically impressive and cheerfully impractical.
- A practical niche is accessing GUI tools on machines where installing or exposing VNC is undesirable.

### LLM perspective

- View: The project's value is less universal GUI replacement than making the terminal a surprising Wayland experimentation surface.
- Impact: SSH-friendly rendering could unlock occasional remote GUI access without deploying a conventional desktop-sharing stack.
- Watch next: Application compatibility, input fidelity, image-protocol performance, and whether remote use becomes reliable beyond demos.
