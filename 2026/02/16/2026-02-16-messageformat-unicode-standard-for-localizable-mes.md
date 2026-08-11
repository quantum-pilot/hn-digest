# MessageFormat: Unicode standard for localizable message strings

- Score: 146 | [HN](https://news.ycombinator.com/item?id=47033328) | Link: https://github.com/unicode-org/message-format-wg

### TL;DR

Unicode MessageFormat is now a stable CLDR standard for representing localizable messages across programming environments and presentation frameworks, replacing earlier ICU formatting capabilities. Its interoperable syntax and data model support locale-aware numbers, plurals, selection, gender, inflection, and future speech features; some default functions remain drafts. Practitioners value moving language-specific branching out of application code, particularly for plural systems more complex than English. Critics find the syntax DSL-like and brittle, and want a short, prominent example plus clearer evidence over mature alternatives such as gettext and Fluent.

### Comment pulse

- Locale rules make simple count labels deceptively complex → central formatting reduces conditional UI code across languages.
- The syntax resembles a programming language → contributors want it small, side-effect-free, and separated from simple interpolation.
- Adoption needs approachable examples and conformance suites → a specification alone does not establish ergonomics or cross-library consistency.
