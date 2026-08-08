# Show HN: Wyzer Programming Language

- Score: 168 | [HN](https://news.ycombinator.com/item?id=49209385) | Link: https://github.com/Wyzer-Lang/wyzer

### TL;DR

Wyzer is an early, statically typed compiled language exploring one ownership rule across memory, threads, interrupts, and networks. It combines Perceus reference counting with choreographic programming: developers express a communication protocol, and compiler projection emits role-specific programs whose sends and receives match by construction, aiming to exclude distributed deadlocks. Data is immutable by default, failures use `Result`, and there is no garbage collector, lifetime syntax, hidden exceptions, or async/await split. HN praised the ambition and conservative syntax but said the documentation buries choreography beneath language basics and lacks distributed examples.

### Comment pulse

- Readers wanted choreography first: a remote counter or client/server example would reveal the novelty better than syntax tutorials or a donut.
- Global communication primitives pair sends and receives atomically — counterpoint: expressivity, timeouts, latency visibility, foreign APIs, and mixed-language systems remain open questions.
- The maintainer is restructuring documentation and limiting AI contributions after finding AI-assisted documentation unhelpful.

### LLM perspective

- View: Choreography shifts distributed correctness from checking arbitrary programs to designing a language where mismatched communications cannot be expressed.
- Impact: Systems developers could share one safety model across layers, accepting reduced expressivity and a young ecosystem.
- Watch next: Demonstrate projection, failure recovery, dynamic membership, interoperability, performance, formal guarantees, and which deadlock-free systems remain inexpressible.
