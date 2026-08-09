# Node.js needs a virtual file system

- Score: 222 | [HN](https://news.ycombinator.com/item?id=47413195) | Link: https://blog.platformatic.dev/why-nodejs-needs-a-virtual-file-system

### TL;DR

Platformatic proposes `node:vfs`, an experimental core virtual filesystem that mounts memory or embedded assets beneath normal paths so `node:fs`, `import`, `require`, and unaware dependencies can use them. Its userland preview adds SQLite and sandboxed real-directory providers, but must duplicate module resolution, patch private/global APIs, and cannot fully handle native modules or cache invalidation—reasons the author argues core support is necessary. HN focused less on use cases than governance: Claude Code generated much of the roughly 14,000-line PR, raising review burden, provenance, security, and Developer Certificate questions.

### Comment pulse

- Embedded Node users welcomed loading bundled JavaScript without temporary files and saw VFS mounts as a safer plugin boundary.
- Skeptics said blobs already cover runtime ESM, RAM disks serve tests, and spawned programs remain outside Node-level virtualization.
- Large AI-authored changes should be split into reviewable commits — counterpoint: core maintainers are already scrutinizing the design.

### LLM perspective

- **View:** Module-resolution integration must justify adding a process-global abstraction to core.
- **Impact:** SEA, test, and plugin authors could reuse unchanged libraries instead of maintaining filesystem shims.
- **Watch next:** Permission-model integration, mount isolation, native-addon semantics, cache cleanup, API stability, and reviewer sign-off.
