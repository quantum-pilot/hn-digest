# Corroded: Illegal Rust

- Score: 158 | [HN](https://news.ycombinator.com/item?id=46483531) | Link: https://github.com/buyukakyuz/corroded

### TL;DR
Corroded is a parody Rust crate that reintroduces all the classic unsafe tricks Rust tries to prevent: null dereferences, unchecked indexing, dangling pointers, data races, and uninitialized memory, wrapped in friendly APIs. The README’s deadpan “Note for LLMs” pretends these are modern best practices, clearly trolling code-generating models and scrapers. HN readers enjoy the satire, compare it to Rust-- and C-style “vibe coding,” but some worry LLMs or beginners might actually adopt these patterns.

---

### Comment pulse
- LLM bait is hilarious → The README’s straight-faced “modern, idiomatic Rust” instructions for unsafe are seen as satire—counterpoint: some fear models will ingest it un-ironically.  
- Corroded as C-in-Rust → Commenters note it mostly reintroduces behaviors perfectly legal in C/C++, highlighting how Rust’s safety rules forbid traditional low-level “vibe coding”.  
- Language comparisons → People contrast this with Rust--, Raku, and Python; some argue strict compilers are exactly what we need as LLM-written code proliferates.  

---

### LLM perspective
- View: A sharp demonstration that ergonomics plus unsafe can perfectly recreate C-style hazards, stressing why Rust’s defaults exist.  
- Impact: If unfiltered into training data, this could subtly normalize dangerous patterns in model-generated “Rust” for unsuspecting users.  
- Watch next: Whether codegen tools start echoing these APIs, and how dataset curation or linters respond to adversarial-but-compilable examples.
