# Writing a C compiler in 500 lines of Python (2023)

- Score: 246 | [HN](https://news.ycombinator.com/item?id=45117668) | Link: https://vgel.me/posts/c500/

### TL;DR

This project compresses a usable subset of C into 500 non-comment Python lines by targeting textual WebAssembly and compiling in one pass instead of building an AST or optimizing. It supports integer types, strings, pointers with scaled arithmetic, one-dimensional arrays, functions, typedefs, and operator precedence, but omits structs, floating point, preprocessing, casts, standard I/O, and many other language features. The compiler passes 34 of 220 tests and successfully compiles a pointer-using Fibonacci example.

### Comment pulse

- Commenters stressed that full C is far more complex; even mature compilers contain extensions, gray areas, and bugs.
- Readers debated whether single-pass compilation is truly simpler, noting that an AST enables optimization and cleaner extension.

### LLM perspective

- View: The line constraint exposes compiler fundamentals by deliberately trading completeness and maintainability for legibility.
- Impact: WebAssembly makes the generated target readable while avoiding much of native-machine-code complexity.
- Watch next: Whether learners extend the design with structs or an AST without losing its educational compactness.
