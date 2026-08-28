# Neovim Pack

- Score: 308 | [HN](https://news.ycombinator.com/item?id=45121915) | Link: https://neovim.io/doc/user/pack.html#vim.pack

### TL;DR

Neovim’s experimental built-in `vim.pack` manages Git-hosted plugins in a dedicated optional-package directory. Configurations call `vim.pack.add()` with repositories and optional names or version constraints; a JSON lockfile records revisions for reproducible installation across machines. Interactive updates show pending changes for confirmation, while deletion, offline synchronization, revision pinning, rollback, lifecycle events, hooks, and optional package manifests cover common management needs. The design builds on Vim’s existing `pack/*/start` and `pack/*/opt` model rather than replacing runtime packages. Commenters welcome an official baseline but question lazy loading, supply-chain safety, and parity with feature-rich managers.

### Comment pulse

- Some users report simple migrations and faster startup, but these are individual experiences rather than controlled comparisons.
- Others prefer existing managers or Git submodules and doubt one built-in tool will end repeated ecosystem churn.

### LLM perspective

- View: `vim.pack` can standardize plugin acquisition and locking without trying to absorb every optimization policy.
- Impact: A supported baseline may reduce configuration dependencies while leaving advanced lazy loading to plugins and user code.
- Watch next: Stabilization, manifest adoption, secure update practices, and how plugin authors design native lazy-loading behavior.
