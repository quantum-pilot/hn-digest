# Ghostty – Terminal Emulator

- Score: 581 | [HN](https://news.ycombinator.com/item?id=47206009) | Link: https://ghostty.org/docs

### TL;DR

Ghostty is a GPU-accelerated, native-UI terminal for macOS and Linux with zero-configuration defaults, themes, keybindings, settings, and VT documentation. Its creator says the larger story is libghostty: a shared terminal core already embedded by more than a dozen projects, whose bug reports strengthen the main app. Ghostty 1.3 was expected within weeks with search, scrollbars, and VT improvements, while a nonprofit publishes finances and pays contributors. HN users praised speed and polish but cited stable-release search gaps, SSH rendering and terminfo friction, and preferences for WezTerm, Kitty, Foot, or tmux.

### Comment pulse

- Search’s absence drove users away — counterpoint: tip builds already include it, and version 1.3 was imminent.
- SSH sessions can render incorrectly when remote hosts lack matching terminfo; resets or copied definitions help inconsistently, making daily use frustrating.
- AI coding has pushed newcomers into terminals, creating demand for discoverable window management and text interactions beyond traditional terminal semantics.

### LLM perspective

- **View:** libghostty may matter more than another GUI because it amortizes protocol correctness across specialized terminal interfaces.
- **Impact:** Embedders gain a mature core; shared adoption supplies broader testing and reduces dependence on one flagship application.
- **Watch next:** Version 1.3 stability, search ergonomics, SSH compatibility, embedder growth, contributor continuity, and Linux packaging.
