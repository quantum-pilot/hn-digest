# My temporary PHP fix from 2014 has nearly 20M installs. Today I'm deprecating it

- Score: 337 | [HN](https://news.ycombinator.com/item?id=49718773) | Link: https://jakeasmith.com/blog/http-build-url/

### TL;DR

A 174-line PHP polyfill written during AOL's 2014 PHP migration became a nearly 20-million-install dependency, still receiving more than 400,000 monthly installs and appearing in WPML, Debian, Ubuntu, and other projects. After years away, its author found a path-handling bug that can remove every letter “a,” but chose deprecation over risky maintenance or transferring a widely trusted package. Users should migrate to PHP League's URI library or PHP 8.5's native URI API; the abandoned package remains installable without fixes.

### Comment pulse

- Temporary fixes become infrastructure → a narrowly scoped compatibility shim persisted because it worked and downstream packages embedded it beyond its author's visibility.
- Deprecation limits supply-chain risk → replacing an inactive maintainer could create an attractive takeover path, while supported URI alternatives now exist.
- Fixing can be as risky as waiting → widespread undocumented dependencies may rely on current behavior, though commenters debated shipping the known one-line correction.

### LLM perspective

- View: Dependency popularity can outlive both its original problem and the maintainer's capacity, turning simplicity into hidden operational responsibility.
- Impact: Downstream projects must inventory bundled copies and plan explicit migrations rather than assuming package deprecation automatically removes exposure.
- Watch next: Replacement guidance, dependency-tree updates, distributions removing bundled copies, and whether unresolved behavior blocks migration.
