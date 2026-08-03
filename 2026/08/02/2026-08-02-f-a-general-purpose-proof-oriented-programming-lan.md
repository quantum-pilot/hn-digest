# F*: A general-purpose proof-oriented programming language

- Score: 146 | [HN](https://news.ycombinator.com/item?id=49143925) | Link: https://fstar-lang.org/

- TL;DR  
  F* is a dependently typed, proof-oriented programming language aimed at writing code and machine-checked proofs together, with compilation to C and other backends. It underpins verified cryptographic libraries and a full TLS stack used in Firefox and Windows components. Hacker News discussion focuses less on the theory and more on ergonomics: discoverability of syntax examples, the steep “Dwarf Fortress” learning curve, and how F* supports gradual migration from C by specifying and calling existing C code during verification.  

  *Content unavailable; summarizing from title/comments.*

- Comment pulse  
  - Docs discoverability debate → some want a homepage sandbox and syntax samples; others prioritize type system, memory model; tutorial exists but feels buried.  
  - Industrial use → F* powers verified cryptography and a TLS stack in Firefox/Windows, finding real vulnerabilities; backed by Microsoft Research’s Project Everest work.  
  - Interop and migration → language can call existing C code while asserting specifications, enabling incremental porting of large, effectful systems into a verified core.

- LLM perspective  
  - View: F* sits between Coq and production C, targeting high-assurance components rather than general app development today.  
  - Impact: Security-sensitive libraries, protocols, and parsers gain strongest benefits; mainstream developers mainly consume resulting verified C libraries.  
  - Watch next: clearer onboarding materials, better IDEs, and more case studies could broaden adoption beyond research groups and security teams.
