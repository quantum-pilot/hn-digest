# Deno Desktop

- Score: 1009 | [HN](https://news.ycombinator.com/item?id=48626137) | Link: https://docs.deno.com/runtime/desktop/

### TL;DR

`deno desktop`, arriving in Deno 2.9 and available in canary builds, packages TypeScript or supported web-framework projects as cross-platform desktop binaries containing code, Deno, and a rendering backend. It defaults to native OS webviews for size, offers bundled CEF for consistent rendering, uses in-process bindings, cross-compiles, and includes HMR plus binary-diff updates with rollback. HN readers welcomed an Electron/Tauri alternative but focused on runtime distribution, security boundaries, and cross-platform backend tradeoffs.

### Comment pulse

- Shared CEF could shrink apps → skeptics expect divergent Chromium versions, stale runtimes, and embedded-login restrictions to erode the benefit.

- Compile-time permissions do not provide desktop sandboxing → commenters wanted user-facing grants — counterpoint: prompts cannot guarantee an untrusted binary honors them.

- Backend choice trades consistency against maintenance → CEF standardizes rendering, while native webviews shrink bundles but inherit platform-specific bugs.

### LLM perspective

- **View:** Deno Desktop’s differentiation is integration: one runtime coordinates frameworks, packaging, bindings, debugging, updates, and distribution.

- **Impact:** Web teams gain a shorter desktop path, while maintainers assume responsibility for backend security, compatibility, and update policy.

- **Watch next:** Evaluate Deno 2.9 stability, binary sizes, CEF-sharing design, Linux behavior, signing workflows, and runtime permission support.
