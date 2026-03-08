# Ki Editor - an editor that operates on the AST

- Score: 350 | [HN](https://news.ycombinator.com/item?id=47286311) | Link: https://ki-editor.org/

### TL;DR
Ki Editor is a modal, multi-cursor code editor that works directly on the abstract syntax tree, letting you select, move, and refactor syntax nodes instead of plain text. HN readers relate it to JetBrains’ expand/shrink selection, tree-sitter incremental selection, and Lisp/paredit workflows. Some recall fully structural editors where only valid programs exist, but argue those hit usability and ecosystem walls. Others highlight practical AST tools like ast-grep and note that discoverability and real refactor workloads will determine Ki’s long-term appeal.

### Comment pulse
- AST-aware selection already exists (JetBrains Ctrl+W, Neovim incremental, Mathematica, paredit); Ki feels like a focused, editor-wide version—counterpoint: VS Code’s implementation is too coarse.  
- Pure syntax-tree editors eliminating invalid programs fascinate people, but real use hits friction: heavy custom tooling, no plain-text files, cognitive strain enforcing constant correctness.  
- Value of AST editing is workload-dependent; some rarely need big refactors, others prefer ast-grep; discoverability stays hard despite color-scope ideas and Ki’s label hints.  

### LLM perspective
- View: Hybrid editors combining text with AST operations likely win: keep files textual but expose rich node selections, refactors, and multi-cursor transformations.  
- Impact: If Ki matures, it mainly benefits power users in large codebases, language-tool authors, and teams doing repetitive, cross-repo mechanical changes.  
- Watch next: Compare Ki’s workflows against JetBrains, Neovim, and ast-grep on real refactors; watch tree-sitter, LSP, and structural VCS experiments converge with such editors.
