# Introduction to Compilers and Language Design (2021)

- Score: 264 | [HN](https://news.ycombinator.com/item?id=48793454) | Link: https://dthain.github.io/books/compiler/

### TL;DR

Douglas Thain’s free one-semester textbook teaches compiler construction by having undergraduates build a C-like language that emits working x86 or ARM assembly. Assuming C, data structures, and computer architecture, it proceeds from scanning and parsing through ASTs, semantics, intermediate representation, memory, assembly, code generation, and optimization, with starter code and staged tests. Former students endorsed completing the project. HN noted the material stays deliberately close to C and suggested C4, a tiny self-compiling compiler, for extension exercises. Discussion contrasted it with the less-practical Dragon Book and balanced Tiger Book.

### Comment pulse

- Building the entire compiler is the curriculum → staged implementation turns abstract phases into one working artifact and reveals how interfaces between phases constrain design.
- The C focus is a boundary, not an accident → one semester favors familiar syntax and architecture over broad language-design exploration.
- No single classic covers everything → Dragon emphasizes foundations but lacks modern depth and practicality — counterpoint: Tiger better balances implementation with theory.

### LLM perspective

- **View:** A small end-to-end compiler teaches more systems judgment than isolated parser exercises because every representation must survive downstream use.
- **Impact:** The project connects theory to machine behavior, giving students concrete intuition for language semantics, ABI constraints, optimization, and debugging.
- **Watch next:** Full-project completion rates, ARM versus x86 difficulty, self-hosting extensions, garbage collection, SSA, register allocation, and modern optimization follow-ons.
