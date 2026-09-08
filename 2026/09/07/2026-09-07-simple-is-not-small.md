# Simple Is Not Small

- Score: 238 | [HN](https://news.ycombinator.com/item?id=49558685) | Link: https://jyn.dev/simple-is-not-the-same-as-small/

### TL;DR

The essay separates small programs from simple ones, defining complexity as unnecessary coupling. A concise Unix word-frequency pipeline couples aggregation to sorting, becoming awkward when output order changes; a larger Clojure version separates those concerns. Likewise, Rust structs couple static field knowledge to fixed representation, whereas Clojure schemas can remain inspectable data. Large systems can still feel simple if their interfaces hide well-decoupled machinery. The author argues simplicity is broadly valuable, while smallness mainly reflects resource constraints. Commenters challenged the Unix and type-system examples as selectively framed.

### Comment pulse

- Readers linked the thesis to interface-versus-implementation simplicity, noting developers switch between being maintainers and downstream users.
- Unix defenders proposed extensible tools or awk—counterpoint: the author’s larger point concerned hidden coupling, not command availability alone.
- Practitioners agreed clean modularity demands repeated design work that organizations rarely budget, especially beyond isolated scripts.

### LLM perspective

- View: Line count is visible; coupling is consequential because it determines how many assumptions change together.
- Impact: Teams optimizing for small implementations may transfer complexity into interfaces, integration, debugging, or future modifications.
- Watch next: Evaluate designs through change scenarios, dependency graphs, failure isolation, and the assumptions required to prove correctness.
