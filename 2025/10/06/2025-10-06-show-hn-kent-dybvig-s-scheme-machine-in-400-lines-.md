# Show HN: Kent Dybvig's Scheme Machine in 400 Lines of C (Heap-Memory Model)

- Score: 180 | [HN](https://news.ycombinator.com/item?id=45491609) | Link: https://gist.github.com/swatson555/8cc36d8d022d7e5cc44a5edb2c4f7d0b

### TL;DR

This gist implements the heap-based Scheme machine described in section 3.4 of Kent Dybvig's dissertation in roughly 400 lines of C. The compact interpreter includes tokenization and a heap-memory execution model, offering a readable bridge between formal implementation ideas and runnable low-level code. Commenters identified it as an educational realization of Dybvig's dissertation rather than a production Scheme, and connected it to his later work on Chez Scheme, compiler teaching, and other small interpreter or C-backend experiments.

### Comment pulse

- Former students praised Dybvig's ability to teach recursion and optimizing compilers.
- Readers valued compact interpreters as hackable explanations, while distinguishing them from highly optimized implementations.

### LLM perspective

- View: The gist's value is explanatory compression: a concrete machine small enough to understand end to end.
- Impact: Minimal implementations expose continuations, allocation, and evaluation choices hidden by production runtimes.
- Watch next: Annotated tests, garbage collection behavior, and conformance boundaries would improve its teaching utility.
