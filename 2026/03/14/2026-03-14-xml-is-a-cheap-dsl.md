# XML is a cheap DSL

- Score: 231 | [HN](https://news.ycombinator.com/item?id=47375764) | Link: https://unplannedobsolescence.com/blog/xml-cheap-dsl/

### TL;DR

The IRS’s open-source Tax Withholding Estimator encodes tax rules as an XML “Fact Dictionary,” a declarative dependency graph of writable and derived values. Compared with imperative JavaScript, the graph preserves intermediate reasoning, schedules questions only when needed, and makes calculations auditable. XML is verbose, but named elements, attributes, comments, ordered children, ubiquitous parsers, XPath, and cross-language tooling make it a low-cost foundation for a custom DSL. HN agreed with the use case but disputed “cheap,” citing XML’s full specification, parser complexity, performance, and leaner JSON or embedded-language alternatives.

### Comment pulse

- “Cheap” means ecosystem reuse → teams avoid designing and porting a parser while gaining universal query tools — counterpoint: compliant XML engines are heavyweight.
- Other syntaxes read better → S-expressions, Prolog, KDL, functional eDSLs, or compact tagged JSON can express the same declarative graph.
- Schema design determines human readability → XML’s structure helps only when semantic names replace paper-form codes and needless ceremony.

### LLM perspective

- **View:** A constrained XML profile can capture most benefits while explicitly banning risky or irrelevant specification features.
- **Impact:** Public contributors can inspect tax logic across languages without depending on the Scala engine.
- **Watch next:** Fact Graph audit tools, schema evolution, nonprogrammer views, parser profiles, and independent implementations.
