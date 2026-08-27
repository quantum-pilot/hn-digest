# I spent a year making an ASN.1 compiler in D

- Score: 237 | [HN](https://news.ycombinator.com/item?id=45681200) | Link: https://bradley.chatha.dev/blog/dlang-propaganda/asn1-compiler-in-d/

### TL;DR

Bradley Chatha recounts a year building dasn1, an unfinished ASN.1 compiler in D motivated by a toy pure-D stack for X.509 and TLS 1.3. The compiler has generated code that parses several certificates, but the author emphasizes ASN.1's sprawling notation, scattered specifications, ambiguity, constraints, versioning, and repeated semantic checks. D helped through templates, static imports, `typeof`, unit-test features, and generator-friendly syntax, while the project exposed how quickly compiler complexity overwhelms both architecture and the programmer's working memory.

### Comment pulse

- ASN.1 veterans sympathized with the difficulty and debated its historical standards context.
- D users praised language features but cited tooling, ecosystem, verbosity, and standard-library rough edges.
- One reader flagged a likely error in the article's set-intersection example.

### LLM perspective

- View: The project is most valuable as an honest map of complexity, not yet as a production compiler.
- Impact: D's metaprogramming reduced generator work, but could not simplify ASN.1's semantic and specification burden.
- Watch next: Broader certificate coverage, clearer compliance boundaries, and fixes for contested examples.
