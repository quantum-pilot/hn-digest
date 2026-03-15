# XML is a cheap DSL

- Score: 231 | [HN](https://news.ycombinator.com/item?id=47375764) | Link: https://unplannedobsolescence.com/blog/xml-cheap-dsl/

### TL;DR
The IRS’s new open-source Tax Withholding Estimator models tax law as a declarative “Fact Graph” described in XML. Each tax value is a named fact, either user-input (`<Writable>`) or computed (`<Derived>`), linked by dependencies. That yields a transparent, auditable graph where the engine can answer “how was this number calculated?”—vital for a codebase mirroring the U.S. tax code’s complexity. The author argues XML is a “cheap” DSL: ugly but ubiquitous, better than JSON/YAML for nested expressions, and supported by mature tooling (XPath, XSLT, parsers in every language).

---

### Comment pulse
- XML isn’t cheap to parse → full XML (DTD, namespaces, etc.) is complex; compliant parsers are heavy. — counterpoint: a constrained XML subset is far simpler in practice.  
- Many prefer eDSLs or JSON → Haskell/Scala/Lisp or JSON-based S-expression styles give nicer syntax; but fewer developers and weaker cross-language tooling.  
- Historical scars matter → developers remember brittle XML stacks, schema debates, and performance issues, which pushed ecosystems toward JSON despite XML’s richer expressiveness.

---

### LLM perspective
- View: For cross-language, inspectable business rules, “XML as AST” is a pragmatic middle ground between bespoke parsers and underpowered JSON.  
- Impact: Helps tax, finance, and policy domains where explainability, versioning, and independent tooling matter more than syntactic elegance.  
- Watch next: Profiles of “minimal XML for DSLs,” better XML editors/visualizers, and comparisons with JSON/EDN/Prolog-based rule engines on real regulatory workloads.
