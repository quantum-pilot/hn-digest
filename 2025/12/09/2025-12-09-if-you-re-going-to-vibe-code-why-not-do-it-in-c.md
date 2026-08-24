# If you're going to vibe code, why not do it in C?

- Score: 281 | [HN](https://news.ycombinator.com/item?id=46207505) | Link: https://stephenramsay.net/posts/vibe-coding.html

### TL;DR

Stephen Ramsay dislikes vibe coding’s loss of craft and comprehension but believes it can build robust systems. Since programming languages help humans express and reason about software, he asks whether model-generated programs should instead target C, assembly, or a vibe-oriented language pairing pseudocode with machine output and tests. He likens resistance to doubts about stored-program computers and compilers. Commenters challenged his premise that models avoid C’s memory and correctness traps, arguing that requirements, abstractions, static checks, and reviewability become more important when humans write less.

### Comment pulse

- Engineers reported agents forgetting frees and edge cases in C, while Rust’s compiler, lifetimes, and package tooling supplied immediate corrective feedback.
- Requirements remain the bottleneck — counterpoint: proponents said models can accelerate dependency research, legacy translation, and implementation under strong architectural direction.
- Some found repeated prompting fragmented attention and learning; smaller verifiable steps or model-generated specifications made the workflow more manageable.

### LLM perspective

- View: Model authorship strengthens the case for machine-checkable constraints; it does not erase human-oriented semantics.
- Impact: Language choice determines how cheaply teams can detect, review, and repair generated mistakes.
- Watch next: Agent language benchmarks, defects, specification-first workflows, intermediate representations, and maintenance by humans who did not generate code.
