# Towards trust in Emacs

- Score: 175 | [HN](https://news.ycombinator.com/item?id=47778938) | Link: https://eshelyaron.com/posts/2026-04-15-towards-trust-in-emacs.html

### TL;DR

Emacs 30 made files untrusted by default after earlier versions implicitly trusted content, a model implicated in code-execution vulnerabilities. That safer default disables features such as Emacs Lisp Flymake diagnostics without offering a convenient approval path, encouraging users to weaken protection globally. The new MELPA package trust-manager prompts once per project, remembers accept or reject decisions, auto-trusts configuration and load-path files, marks untrusted buffers in the mode line, supports file-level overrides, and clears trust when projects are forgotten. Commenters welcome lower friction but question coarse project-wide trust.

### Comment pulse

- Security barriers that obstruct work push users toward blanket approval, disabled controls, or unmanaged personal machines.
- Users want clearer explanations of what trust enables and which threats each prompt addresses.
- Project trust is convenient — counterpoint: capability-based sandboxes could grant only filesystem, process, network, or evaluation privileges actually needed.

### LLM perspective

- Trust decisions should be scoped, reviewable, expiring, and tied to observable capabilities.
- Safe defaults fail when approval prompts lack immediate context and remediation.
- Watch upstream handling of scratch buffers and finer-grained Emacs permissions.
