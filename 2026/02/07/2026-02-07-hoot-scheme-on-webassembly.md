# Hoot: Scheme on WebAssembly

- Score: 162 | [HN](https://news.ycombinator.com/item?id=46923254) | Link: https://www.spritely.institute/hoot/

### TL;DR

Hoot is Spritely’s self-contained toolchain for compiling Scheme to WebAssembly and running Wasm through an included interpreter on Guile’s virtual machine. Release 0.9.0 supports R7RS-small and part of Guile Scheme, targeting recent Firefox, Chrome, Safari, and Node.js runtimes. Packages are available through Guix, Debian testing or unstable, Homebrew, and signed source archives. Commenters welcomed another route to browser programming without JavaScript, while debating Guile versus Racket performance, libraries, modules, tooling, reproducibility, and whether Hoot could work with Cloudflare Workers.

### Comment pulse

- Scheme reaches the browser → commenters welcomed renewed Wasm language work and another way to avoid writing JavaScript.
- Guile divides opinion → critics preferred Racket’s ecosystem and metaprogramming; defenders cited faster startup, stronger I/O, fibers, libraries, and Guix reproducibility.
- Edge deployment is unresolved → a commenter asked about Cloudflare Workers, but the supplied discussion offered no answer.

### LLM perspective

- View: Hoot combines a Scheme compiler with lower-level Wasm tooling rather than presenting only a browser-language frontend.
- Impact: Guile projects gain a web target and portable tooling, though ecosystem depth and implementation choice may shape adoption.
- Watch next: Stable-package availability, browser compatibility, Cloudflare Workers support, debugger and macro tooling, performance, and richer Guile compatibility.
