# Qt Creator 18 Released

- Score: 131 | [HN](https://news.ycombinator.com/item?id=45761789) | Link: https://www.qt.io/blog/qt-creator-18-released

- TL;DR
  Qt Creator 18 adds experimental Development Containers to automate per-project environments, tabbed editors, and upgraded C++ tooling (LLVM/Clangd 21.1) plus many C++/QML fixes. Projects move Qt Creator settings into .qtcreator/, gain run-configuration syncing, and CMake Test Presets with a CTest locator. Remote Linux improves via tool auto-detection and optional auto-reconnect; Git’s commit editor gets richer file actions. HN commenters praise its lightweight, debugger-friendly C++ experience, note qmake’s deprecation in favor of CMake, and want deeper non-C++ language support. Free upgrade.

- Comment pulse
  - Qt Creator stays a preferred C++ IDE → lightweight and strong debugger/visualizers — counterpoint: CLion’s free edition attracts interest.
  - Good even beyond Qt → solid C++ editor; qmake viewed as deprecated, CMake now standard.
  - Users want broader language tooling → desire for first-class support (e.g., D) beyond C++/QML.

- LLM perspective
  - View: Devcontainer support aligns Creator with VS Code workflows; remote tool auto-detect reduces setup friction.
  - Impact: Embedded and C++ teams get reproducible environments, easier testing via CTest presets, and safer commits from improved Git UI.
  - Watch next: Full devcontainer parity (compose, mounts), richer non-C++ LSPs, and performance gains from LLVM 21.1 across large codebases.
