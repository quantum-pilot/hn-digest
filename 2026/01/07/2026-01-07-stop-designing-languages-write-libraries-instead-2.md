# “Stop Designing Languages. Write Libraries Instead” (2016)

- Score: 215 | [HN](https://news.ycombinator.com/item?id=46525640) | Link: https://lbstanza.org/purpose_of_programming_languages.html

### TL;DR
The essay argues that while most day‑to‑day productivity comes from libraries and frameworks, languages are decisive because they constrain which libraries can exist and how usable they are. Ruby on Rails works because it leans on Ruby’s metaprogramming, first‑class functions, dynamic typing, and GC; you can’t straightforwardly recreate that experience in Java or C. A general‑purpose language’s real purpose is to empower library authors; ongoing research tries to make core mechanisms like type systems and object models themselves library‑extensible.

---

### Comment pulse
- Prolog as “just a library” is contested → its logic variables, bidirectional rules, and search space management don’t map cleanly onto ordinary library calls in mainstream languages.  
- Powerful internal DSLs (Scala, Haskell, Lisps, Raku) enable elegant domain code but often impose steep learning curves and multiple mini‑languages on future maintainers.  
- Many participants emphasize pragmatism: choose tools that communicate intent clearly; suggestions range from Clojure and Elixir to Nushell, OCaml, Raku, Python, and PowerShell for scripting/DSL needs.

---

### LLM perspective
- View: Judge a language by how much leverage it gives library authors to encode domain concepts concisely and safely.  
- Impact: Teams may prefer ecosystems where advanced frameworks feel natural, not bolted on, reducing ceremony and boilerplate in everyday code.  
- Watch next: Languages and runtimes that expose type systems, effects, and object models as programmable layers, plus better cross‑language interop (WASM, FFI, codegen).
