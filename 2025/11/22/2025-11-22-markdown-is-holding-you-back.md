# Markdown Is Holding You Back

- Score: 53 | [HN](https://news.ycombinator.com/item?id=46017782) | Link: https://newsletter.bphogan.com/archive/issue-45-markdown-is-holding-you-back/

- TL;DR  
    - Markdown’s simplicity and ubiquity make it a great lowest-common-denominator, but also a poor source-of-truth for serious technical documentation. It lacks explicit semantics, schemas, and consistency across “flavors,” which hinders reuse, multi-channel publishing, and machine consumption by search or LLMs. The author recommends treating Markdown as an export format, not an authoring master, favoring reStructuredText or AsciiDoc for mid-sized docs and DocBook or DITA for large, structured, enterprise-style content and complex workflows.

- Comment pulse  
    - Markdown isn't limiting → Embed HTML and use AST parsers to recover structure; for websites this is sufficient — counterpoint: HTML usage negates Markdown’s simplicity.  
    - Richer authoring ecosystems → Org-mode, AsciiDoc, Typst, and hand-written HTML offer better semantics, exports, or layout, at the cost of steeper tooling and setup.  
    - Pragmatic stance → Markdown is a minimum-viable, readable format; if your project demands more structure, just switch formats instead of blaming Markdown.

- LLM perspective  
    - View: Markdown as source hinders LLM-based doc agents, which benefit from explicit task/step/note tags and consistent cross-references.  
    - Impact: Teams building AI-assisted docs or complex product guides should pilot AsciiDoc/reStructuredText to evaluate gains in reuse and automation.  
    - Watch next: Benchmarks comparing Markdown vs. structured formats on searchability, LLM answer quality, and multi-channel publishing cost would clarify trade-offs.
