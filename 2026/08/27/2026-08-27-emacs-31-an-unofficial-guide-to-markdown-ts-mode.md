# Emacs 31: An unofficial guide to Markdown-ts-mode

- Score: 174 | [HN](https://news.ycombinator.com/item?id=49464543) | Link: https://rahuljuliato.com/posts/markdown-ts-mode-emacs-31

### TL;DR

Emacs 31 includes experimental markdown-ts-mode, a feature-rich Tree-sitter editor covering CommonMark and most GitHub Flavored Markdown. After loading the built-in library and installing Markdown’s main and inline grammars, users gain structured heading and list operations, folding, markup hiding, task toggles, language-aware fenced blocks, table editing, inline images, navigation, export, and table-of-contents tools. The mode remains experimental because its API and behavior may change, while external grammar versions, compilation tooling, indirect buffers, and Emacs Tree-sitter limitations still create rough edges.

### Comment pulse

- Users welcomed an Org-like Markdown workflow; others argued Markdown cannot reproduce Org’s agenda and document model coherently.
- Critics called grammar installation under-integrated, while supporters noted the mode can prompt and compile known grammars.
- Emacs users recommended Magit plus agent-shell, gptel, Ghostel, or terminal agents for reviewing generated changes.

### LLM perspective

- View: The mode is already capable enough for daily editing, but “built-in” does not yet mean dependency-free setup.
- Impact: Native structured Markdown could reduce collaboration friction for Emacs users who cannot standardize on Org files.
- Watch next: Stabilize APIs, improve grammar discovery, clarify automatic file association, and address parser behavior in indirect buffers.
