# Fix your tools

- Score: 175 | [HN](https://news.ycombinator.com/item?id=47112174) | Link: https://ochagavia.nl/blog/fix-your-tools/

- TL;DR  
  - An OSS maintainer couldn't hit a debugger breakpoint, wasted time adding logs, then realized the real blocker was the misconfigured debugger itself. Fixing that one-line issue made the underlying bug easy to find and inspired a broader lesson: invest in your tools because they amplify every future effort. HN discusses when tool-fixing becomes yak shaving, how much “axe sharpening” is appropriate, and why simpler, composable tools often beat complex automation platforms for reliability and debuggability.

- Comment pulse  
  - Fixing tools risks yak shaving and emotional procrastination; invest in recurring tasks, pay debt gradually — counterpoint: chronic neglect makes everything slower and costlier later.  
  - Axe-sharpening mindset: clean or refactor code while changing it; sharpen tools repeatedly during work, not only in big upfront bursts.  
  - Complex all-in-one automation platforms often fail silently or hit limits; simple scripts plus focused utilities stay transparent, scalable, and easier to debug.

- LLM perspective  
  - View: Treat broken tools as first-class bugs; allocate a small timebox to fix them before adding ad-hoc workarounds.  
  - Impact: Teams that routinely improve debuggers, build systems, and scripts shorten feedback loops, making every subsequent feature or fix cheaper.  
  - Watch next: Develop heuristics and tooling that detect friction automatically and suggest refactors, automation, or simpler alternatives before complexity explodes.
