# Cherri – programming language that compiles to an Apple Shortuct

- Score: 231 | [HN](https://news.ycombinator.com/item?id=47549824) | Link: https://github.com/electrikmilk/cherri

### TL;DR

Cherri is a GPL-licensed text language that compiles directly into runnable Apple Shortcuts, giving large automations functions, scopes, types, includes, Git packages, raw actions, and source control. The Go implementation offers a CLI, VS Code extension, macOS IDE, web playground, Shortcut importing, and signing, while much of its own action library is written in Cherri. HN users welcomed escaping fragile touchscreen editing; one event-automation user with 200 Shortcuts said an LLM quickly learned the syntax and generated compilable examples. Open questions include third-party AppIntents support, examples, and discoverability.

### Comment pulse

- Text, diffs, reuse, and version control address the maintenance cliff that makes complex visual automations painful.
- Users wanted more real-world examples and social discovery, not only language documentation.
- Third-party AppIntents remain a key compatibility question because many useful Shortcut actions come from installed apps.

### LLM perspective

- **View:** Cherri succeeds by preserving Apple’s execution platform while replacing its least scalable authoring interface.
- **Impact:** Shortcut projects can become reviewable software assets rather than opaque, manually edited personal artifacts.
- **Watch next:** AppIntent coverage, compiler fidelity, signing reliability, import round-trips, package security, and sustained maintainer support.
