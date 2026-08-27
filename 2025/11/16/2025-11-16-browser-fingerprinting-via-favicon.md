# Browser fingerprinting via favicon

- Score: 162 | [HN](https://news.ycombinator.com/item?id=45947770) | Link: https://github.com/jonasstrehle/supercookie

### TL;DR

Supercookie demonstrates encoding a browser identifier in which path-specific favicons are cached: later requests reveal cached bits because the browser fetches only missing icons. The project claims this can survive ordinary cookie and cache clearing, VPN use, restarts, and sometimes private browsing. Its compatibility table references older browser versions, so it does not establish current exposure. Commenters recognized the work as dating to 2021, reported persistent favicon mix-ups, and found the demo fixed, functional, or trapped in redirect loops depending on setup.

### Comment pulse

- Separate favicon storage creates a tracking side channel → request absence can disclose previously cached per-path state.
- Current vulnerability status is unclear → the supplied tests and browser versions are several years old.
- Persistent wrong icons offered anecdotal support for cache isolation → counterpoint: display bugs do not prove successful identification.

### LLM perspective

- View: Convenience caches need the same partitioning and deletion semantics as explicit browsing data.
- Impact: Users may remain linkable after taking privacy steps they reasonably expect to reset identity.
- Watch next: Retest current browsers across profiles and private modes, then document vendor fixes and cache-clearing behavior.
