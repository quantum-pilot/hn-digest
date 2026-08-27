# Mise: Monorepo Tasks

- Score: 285 | [HN](https://news.ycombinator.com/item?id=45491621) | Link: https://github.com/jdx/mise/discussions/6564

### TL;DR

Mise’s experimental Monorepo Tasks discovers project tasks across one repository, assigns location-prefixed names, inherits and overrides tool versions and environments, supports wildcard execution, and runs each task in its proper context from anywhere. It targets polyglot teams wanting more coordination than Just or Taskfile without Bazel’s hermetic complexity, while lacking sophisticated remote caching. HN users praised combining runtime management and common task entry points, but debated caching boundaries, disabled GitHub issues, PATH management, and whether broader responsibilities could undermine mise’s useful simplicity.

### Comment pulse

- Tool and task management reinforce each other → commands receive correct language versions and environments without manual activation.
- Caching scope is contested → local source/output checks exist, while remote build caching remains an explicit anti-goal.
- Breadth creates adoption anxiety → prospective users worry one tool controlling runtimes, CLIs, environment, tasks, and PATH becomes difficult to replace.

### LLM perspective

- View: Mise occupies a pragmatic layer above scripts and below dependency-aware build systems.
- Impact: Polyglot teams can standardize onboarding and CI without adopting a hermetic build model.
- Watch next: Test wildcard semantics, trust propagation, nested overrides, local caching, performance, issue governance, and feature stability.
