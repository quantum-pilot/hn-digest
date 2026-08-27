# Markdown Is Holding You Back

- Score: 53 | [HN](https://news.ycombinator.com/item?id=46017782) | Link: https://newsletter.bphogan.com/archive/issue-45-markdown-is-holding-you-back/

### TL;DR

The author argues Markdown’s simplicity becomes a liability for large technical-documentation systems because headings and lists encode presentation, not domain meaning. Flavor differences, MDX components, and custom plugins weaken portability, while missing semantics complicate validation, reuse, syndication, and multi-format publishing. He recommends reStructuredText or AsciiDoc for richer developer docs and DocBook or DITA for structured enterprise publishing. Commenters counter that Markdown ASTs and embedded HTML cover many needs, and that its readability and low authoring cost explain its durable success.

### Comment pulse

- Raw HTML extends Markdown → frequent use undermines Markdown’s convenience and cannot always mix freely with Markdown blocks.
- Semantic schemas enable reliable transformation → procedures, notes, commands, and references remain distinguishable to machines.
- Most authors do not share enterprise constraints → lightweight, readable source often matters more than industrial reuse.

### LLM perspective

- View: Markdown is not universally limiting; it becomes lossy when content types must survive multiple publishing systems.
- Impact: Documentation teams must trade author accessibility against validation, reuse, portability, and transformation guarantees.
- Watch next: Inventory actual reuse failures before migrating, then prototype AsciiDoc or structured XML on representative documents.
