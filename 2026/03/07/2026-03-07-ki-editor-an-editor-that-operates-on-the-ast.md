# Ki Editor - an editor that operates on the AST

- Score: 350 | [HN](https://news.ycombinator.com/item?id=47286311) | Link: https://ki-editor.org/

### TL;DR

Ki is a modal, multi-cursor editor built around direct syntax-node selection and manipulation. Its Selection Modes aim to make movement and bulk operations consistent across words, lines, and AST structures, reducing the keystroke gymnastics of text-only editing. HN readers connected the model to JetBrains expand-and-shrink selection, tree-sitter text objects, paredit, and structural search. They liked node-level delete, copy, and replace operations but identified discoverability as the main obstacle; broader discussion warned that tree-only editors sacrifice plain-text tooling, tolerate incomplete thought poorly, and require incompatible version-control ecosystems.

### Comment pulse

- Generic expand, shrink, inside, and around operations avoid requiring users to memorize every language’s node names.
- Labeling visible nodes can solve jump discoverability, though colors or scopes might make structural boundaries continuously apparent.
- Fully syntax-valid editing sounds safe — counterpoint: programmers routinely pass through incomplete states, and text preserves universal tooling.

### LLM perspective

- **View:** Ki’s practical opportunity is AST-aware text editing, not replacing source files with opaque trees.
- **Impact:** Refactoring-heavy developers gain precise multi-node operations; occasional users face learning costs for benefits they may rarely need.
- **Watch next:** Language coverage, parser-error behavior, transformation previews, undo semantics, performance, and integrations with LSP and agents.
