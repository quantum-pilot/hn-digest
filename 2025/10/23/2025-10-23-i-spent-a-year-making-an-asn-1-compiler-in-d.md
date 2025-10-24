# I spent a year making an ASN.1 compiler in D

- Score: 237 | [HN](https://news.ycombinator.com/item?id=45681200) | Link: https://bradley.chatha.dev/blog/dlang-propaganda/asn1-compiler-in-d/

- TL;DR
  - A developer spent a year building “dasn1,” an ASN.1-to-D compiler to parse DER/X.509 for a D-native TLS 1.3 stack. The post tours ASN.1’s sprawling specs (x.680–x.683), neat features (constraints, OID-based versioning), gnarly edges (ANY DEFINED BY, value-sequence ambiguities), and how D’s metaprogramming, static imports, typeof, and unit-test ergonomics make codegen bearable. It’s WIP; many semantic transforms and constraints remain. HN discusses protocol-wars history, D’s promise vs libraries/tooling, and calls for specs to ship tested parsers.

- Comment pulse
  - ASN.1 as ISO/ITU “corporate-style” rigor vs IETF pragmatism → complexity and ossification narratives resurfaced. — counterpoint: blame precision goals and later Internet vendor apathy, not “corporate.”
  - D praise → powerful metaprogramming, inline unittests, ergonomics; concern → noisy attributes, weak/fragmented Phobos; hope for Phobos v3 but skepticism.
  - Better spec process → require a working parser + tests before ratification; “a human will use this” design mindset to curb baroque grammar.

- LLM perspective
  - View: Targeting DER/X.509 first is pragmatic; defer x.681–x.683 until TLS path stabilizes.
  - Impact: A solid D ASN.1 layer could unlock credible D TLS and PKI tooling, reducing C dependencies.
  - Watch next: Decode full RFC 5280 suite; publish perf/compat vs asn1c/pyasn1; prototype Information Object Classes or a safer ANY mapping.
