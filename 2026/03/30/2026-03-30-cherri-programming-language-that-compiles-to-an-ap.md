# Cherri – programming language that compiles to an Apple Shortuct

- Score: 231 | [HN](https://news.ycombinator.com/item?id=47549824) | Link: https://github.com/electrikmilk/cherri

- TL;DR  
Cherri is a Go-based, text-first programming language that compiles directly into Apple Shortcuts, letting you script automations in code instead of Apple’s drag-and-drop editor. It mirrors Shortcut actions almost 1:1, adds a type system, packages, functions, imports, and tooling for macOS, VS Code, and a web playground. HN commenters highlight how painful complex Shortcuts are to build and maintain visually, praise Cherri for enabling git-based workflows, and note its synergy with LLMs that can generate Cherri source.

- Comment pulse  
  - Cherri enables serious automation → one user built ~200 macOS Shortcuts, including OS-only actions, and then had Claude learn Cherri to generate additional workflows.  
  - Text-based Shortcuts dev is overdue → programmers find Apple’s no-code editor slow, fragile, and hard to version; a CLI language plus git feels vastly saner.  
  - Ecosystem questions remain → commenters ask about third-party AppIntents and a social hub for examples — counterpoint: Reddit and MacStories already host many community Shortcuts.

- LLM perspective  
  - View: A typed DSL over Shortcuts turns Apple’s brittle visual automations into maintainable, testable code artifacts.  
  - Impact: Power users, indie devs, and ops teams on macOS can finally treat OS-level automations like normal software projects.  
  - Watch next: richer AppIntents integration, standard libraries of reusable flows, and tighter LLM tooling for round‑trip editing and decompiling Shortcuts.
