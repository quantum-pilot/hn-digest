# A beginner's guide to extending Emacs

- Score: 129 | [HN](https://news.ycombinator.com/item?id=45223239) | Link: https://blog.tjll.net/a-beginners-guide-to-extending-emacs/

- TL;DR
  - The post walks through extending Emacs without prior Elisp by building a reStructuredText :ref: completion backend. It introspects completion-at-point, defines a custom “thing” for bounds, builds candidates via rx + re-builder + re-search-forward, and returns (start end candidates). It then wires mode hooks, scales across files with caches and with-temp-buffer, and adds nicer UI via corfu/company metadata. HN highlights Emacs’s discoverability (describe-*, apropos), the “every key is a function” model, and LLM-assisted live Elisp as a productivity boost for customization.

- Comment pulse
  - LLM + Emacs is a killer app → gptel + Claude, org-mode logs, live eval, backtraces; rapid, versioned customization across machines.
  - Everything is a function call → keys map to commands; describe-key/apropos/docs demystify customization.
  - Emacs introspection eases hacking → info/helpful/edebug/debug-on-error shorten feedback loops — counterpoint: debugging event-loop quirks can still be painful.

- LLM perspective
  - View: Use CAPFs as composable units; prefer rx/re-builder; cache results; minimize expensive look-behind on big buffers.
  - Impact: Faster Sphinx cross-referencing; reusable pattern for adding domain-specific completions across modes.
  - Watch next: Package it; integrate project.el/file-notify; benchmark latency; add metadata/docs; consider tree-sitter for robust token bounds.
