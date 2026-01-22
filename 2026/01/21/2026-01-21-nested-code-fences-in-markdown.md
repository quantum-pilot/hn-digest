# Nested code fences in Markdown

- Score: 178 | [HN](https://news.ycombinator.com/item?id=46705201) | Link: https://susam.net/nested-code-fences.html

- TL;DR
    - CommonMark and GFM don’t really support “nested” backtick fences; a later ``` just closes the first fence and leaks content. This post explains the official workarounds: use tildes or longer backtick runs for outer fences, and use multi-backtick inline spans plus leading/trailing spaces to safely include literal backticks. HN readers relate this to GitHub suggestions, LLM prompting, and Markdown’s famously messy ecosystem, with CommonMark praised as a much-needed, if belated, standard.

- Comment pulse
    - Multi-character fences (```` ... ```` or ~~~ ... ~~~) are already standard in GitHub suggestions, JupyterBook, etc.; they generalize cleanly to show nested ``` blocks.
    - Markdown’s ecosystem feels like edge-case soup; CommonMark is praised as the closest thing to a real spec and testable standard—counterpoint: fragmentation remains entrenched.
    - People note these tricks help when prompting LLMs or delimiting content in code, and even serve as markdown-renderer test cases and benchmarks.

- LLM perspective
    - View: Variable-length fence delimiters effectively emulate nesting, avoiding changes to Markdown grammar while still representing arbitrarily complex literal code.
    - Impact: Writers of docs, chatbots, and tooling can reliably embed Markdown, code, and literal backticks inside each other.
    - Watch next: more editors and renderers advertising full CommonMark compliance, plus richer linting to flag ambiguous or non-portable fence usage.
