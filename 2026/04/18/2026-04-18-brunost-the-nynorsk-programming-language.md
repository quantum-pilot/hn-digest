# Brunost: The Nynorsk Programming Language

- Score: 129 | [HN](https://news.ycombinator.com/item?id=47756320) | Link: https://lindbakk.com/blog/introducing-brunost

### TL;DR

Brunost is an interpreted programming language whose keywords and identifiers must be Nynorsk, checked against a bundled dictionary. Written in Zig and compiled to WebAssembly for a playground, it offers mutable and locked variables, conditionals, functions, loops, modules, exceptions, loose types, and a Game of Life example. Its creator rejects production use and plans only a few features before treating it as finished. Hacker News became a language committee, correcting Bokmål leakage and grammar while proposing gendered declarations, agreement-aware loops, `og` before a list’s final item, and `blir` for mutation.

### Comment pulse

- Native speakers found non-Nynorsk keywords and malformed adjectives — counterpoint: the creator expected mistakes, earned a school grade of two, and welcomed corrections.
- Proposals made grammar executable: noun gender could determine declarations and loop agreement, while incorrect forms could reduce a program’s grade.
- Dictionary enforcement exposed practical limits around abbreviations like BMI, permitted loanwords, and typing æ/ø/å alongside braces on a U.S. layout.

### LLM perspective

- **View:** The joke succeeds because natural-language correctness becomes a type system, revealing both linguistic structure and dictionary-based validation’s brittleness.
- **Impact:** Learners can explore interpreter, WebAssembly, editor, and language-server work without the expectations of a serious production ecosystem.
- **Watch next:** Hashmaps, FFI, file I/O, web serving, loanword policy, grammatical agreement, documentation, highlighting, and the promised mascot.
