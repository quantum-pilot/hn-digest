# Why XML tags are so fundamental to Claude

- Score: 147 | [HN](https://news.ycombinator.com/item?id=47207236) | Link: https://glthr.com/XML-fundamental-to-Claude

### TL;DR

The author argues that XML helps Claude distinguish instructions from nested content because paired delimiters mark transitions between direct discourse and quoted or embedded material. The broader claim connects such boundaries across human language, programming and even DNA; XML itself is merely one explicit notation. Hacker News disputed Claude's uniqueness and the lack of evidence that XML beats Markdown, quotation marks or JSON. Possible advantages include named closing tags, web-heavy training data and Anthropic's tool syntax, but commenters treated the secret-sauce thesis as speculative without controlled tests.

### Comment pulse

- Named start and end tags may ease long-range matching → unlike Markdown sections or brackets, closure repeats the section identity.
- Model-specific post-training may explain gains → it does not establish a universal linguistic principle.
- Anecdotes favor XML — counterpoint: one user observed no difference, and the article supplies no controlled comparison.

### LLM perspective

- **View:** XML is a practical prompt schema, not evidence of Claude-specific language understanding.
- **Impact:** Structured boundaries can separate untrusted data, examples and instructions.
- **Watch next:** Cross-model ablations measuring accuracy, injection resistance and token overhead across XML, Markdown and JSON.
