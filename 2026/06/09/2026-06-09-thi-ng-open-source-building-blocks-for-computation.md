# Thi.ng – open-source building blocks for computational design and art

- Score: 180 | [HN](https://news.ycombinator.com/item?id=48437743) | Link: https://thi.ng

### TL;DR

thi.ng is Karsten Schmidt’s open-source computational-design toolkit, grown since 2006 into roughly 350 subprojects spanning graphics, geometry, data structures, visualization, simulation, fabrication, and more. Its bottom-up philosophy favors small, composable, mostly functional modules rather than a framework. The TypeScript umbrella monorepo contains 216 packages, about 245,000 lines of code and documentation, 185 examples, almost no third-party dependencies, and an Apache-2.0 license. HN praised its unusually thoughtful, atomic libraries but wondered why adoption remains limited; language preferences and weak discoverability surfaced, alongside reports of Safari/GPU rendering glitches on the showcase site.

### Comment pulse

- Language preference limits reach → admirers port selected modules rather than adopt Clojure or TypeScript, helping explain the toolkit’s low visibility.
- Atomic packaging lowers adoption cost → dependency-free TypeScript modules can be selected individually instead of importing a framework.
- Showcase polish drew criticism → users reported GPU flicker and broken iOS zoom — counterpoint: the author suspects Safari and could not reproduce one issue.

### LLM perspective

- **View:** thi.ng behaves like a curated standard library for creative computing: breadth without forcing one application architecture.
- **Impact:** Creative coders can replace scattered dependencies with interoperable primitives, but must invest in catalog exploration and API learning.
- **Watch next:** Evaluate bundle size, tree-shaking, browser compatibility, maintenance status, documentation paths, and cross-package consistency for a representative project.
