# Kotlin creator's new language: talk to LLMs in specs, not English

- Score: 267 | [HN](https://news.ycombinator.com/item?id=47350931) | Link: https://codespeak.dev/

### TL;DR

CodeSpeak presents an LLM-powered language/workflow where teams version plain-text specifications and regenerate production code, mixing managed output with handwritten files. It claims 5–10× smaller maintained sources; four case studies show 5.9–9.9× line-count reductions while expanding or preserving tests. Commenters dispute calling it a language and question whether prose can capture incidental behavior, cross-spec interactions, manual fixes, and stable results across changing nondeterministic models. Supporters argue that persistent, reviewable prompts and cheap regeneration make higher-level specifications valuable even when they leave implementation freedom.

### Comment pulse

- Specifications preserve intent better than transient chats → diffs expose requirement changes and keep agent instructions alongside source history.
- Generated code remains information-bearing → unspecified choices, bugs, and hand edits can diverge from documents or disappear during regeneration.
- Formal verification is proposed → counterpoint: useful high-level specs are concise precisely because they permit multiple valid implementations.

### LLM perspective

- **View:** This works best when tests define hard behavior and prose captures design intent, with code treated as generated state.
- **Impact:** Teams may review smaller artifacts but spend more on regeneration, verification, and spec-code reconciliation.
- **Watch next:** Code-to-spec takeover, manual-change workflows, model migration reproducibility, and results on long-lived multi-module systems.
