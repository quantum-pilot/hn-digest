# Replacing a 3 GB SQLite db with a 10 MB FST (finite state transducer) binary

- Score: 160 | [HN](https://news.ycombinator.com/item?id=48082676) | Link: https://til.andrew-quinn.me/posts/replacing-a-3-gb-sqlite-database-with-a-7-mb-fst-finite-state-trandsucer-binary/

### TL;DR
A Finnish–English “pocket dictionary” app needed fast offline prefix search over tens of millions of agglutinative word forms. A trie-based Go implementation stayed small for base words but blew up when inflections were added, leading to a hacked-on 3 GB SQLite FTS database download. Revisiting the problem in Rust with BurntSushi’s `fst` crate, the author rebuilt the mapping as a finite state transducer (a minimal DAFSA-style automaton), shrinking it to a 10 MB static binary—while learning value from first shipping the “bad easy” SQLite solution.

---

### Comment pulse
- Start with the dumb-but-obviously-correct version → it works, builds intuition, then serves as an oracle when you optimize later.  
- LLM twist: use it to write the simple reference implementation plus exhaustive tests, then let it generate aggressive optimizations guarded by those tests.  
- FSTs/DAFSAs have a rich history from DAWG and Scrabble engines; key win is merging identical suffix subgraphs, not regex-style pattern matching.

---

### LLM perspective
- View: FSTs are ideal when you have a large, static string-to-value map with heavy prefix/suffix redundancy and tight memory constraints.  
- Impact: Offline search tools, dictionaries, and embedded NLP can become dramatically smaller and more responsive on low-end hardware.  
- Watch next: Better FST builders, language-agnostic bindings, and benchmarks versus compressed SQLite/tries on real-world corpora and devices.
