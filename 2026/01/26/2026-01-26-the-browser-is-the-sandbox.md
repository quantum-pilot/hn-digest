# The browser is the sandbox

- Score: 327 | [HN](https://news.ycombinator.com/item?id=46762150) | Link: https://simonwillison.net/2026/Jan/25/the-browser-is-the-sandbox/

### TL;DR

Paul Kinlan’s Co-do demo tests whether mature browser isolation can host local coding agents without a heavyweight container. A user grants a folder, chooses an LLM provider, and exposes file tools while network access is constrained through CSP and nested sandboxed iframes; WebAssembly in workers handles untrusted execution. Simon Willison highlights the lighter deployment model and cross-browser read-only directory selection, but notes thin iframe documentation and Chrome-only File System Access support. Commenters add that host CLI access, durable workflows, and browser inconsistencies remain limiting.

### Comment pulse

- Browsers offer a capability model → users explicitly grant files and approved network endpoints while hostile generated code stays inside established isolation.
- Local productivity remains constrained → safe access to host commands and writable files is harder than isolated computation.
- Client-only agents trade infrastructure for edge cases → commenters found long-running state and reliability harder than server-backed orchestration.

### LLM perspective

- View: The browser is a credible least-authority shell for bounded agents, not a universal operating-system sandbox.
- Impact: Small tools can deploy cheaply without local containers, while advanced workflows still need supervised host integration.
- Watch next: Cross-browser File System Access, iframe tests, sandbox escapes, offline state recovery, and reproducible Co-do security audits.
