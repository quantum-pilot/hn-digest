# A beginner's guide to extending Emacs

- Score: 129 | [HN](https://news.ycombinator.com/item?id=45223239) | Link: https://blog.tjll.net/a-beginners-guide-to-extending-emacs/

### TL;DR

This tutorial teaches Emacs extensibility by building completion for reStructuredText references. Starting from `describe-key`, the author traces `completion-at-point` into its hook, studies existing implementations, writes Elisp to identify bounds and collect candidates, and installs the function for relevant buffers. Extensions then add project-wide cached references, mode hooks, candidate types, and contextual documentation. The larger lesson is that Emacs exposes functions, variables, source, and documentation for live inspection. Commenters emphasized built-in discovery tools and described LLM-assisted, immediately evaluable customization workflows.

### Comment pulse

- Several readers said understanding that every key press invokes a function unlocked their mental model of Emacs.
- Experienced users recommended `info`, `apropos`, describe commands, debuggers, and source inspection as learning tools.

### LLM perspective

- View: The tutorial succeeds by teaching a discovery loop, not merely presenting a finished configuration snippet.
- Impact: Introspection turns customization into incremental investigation and reduces dependence on opaque extension APIs.
- Watch next: Apply the same loop to another mode, then measure cache invalidation and project-scale completion performance.
