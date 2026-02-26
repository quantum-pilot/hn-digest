# The Om Programming Language

- Score: 218 | [HN](https://news.ycombinator.com/item?id=47154971) | Link: https://www.om-language.com/

TL;DR
- Om is an experimental, maximally-simple concatenative, homoiconic language where every program is a function that consumes the rest of the program as data. It uses prefix notation (no data stack), treats all values as operands via a “panmorphic” interface, and is fully Unicode-correct, making any UTF-8 text a valid program and trivial data format. Implemented as an embeddable C++ header-only library, it’s still an early, incomplete proof-of-concept focused on core semantics and recursion-friendly evaluation.

Comment pulse
- Show syntax first → Readers want examples and intuition before formal syntax, build tooling, and dependency details.
- Feels like Forth/concatenative heritage → Prefix concatenation, composability, and homoiconicity echo Forth and Joy—counterpoint: stackless, function-composition model is a notable twist.
- Nice hobbyist language project → People enjoy the intellectual exercise; personal anecdotes about the author add credibility and community interest.

LLM perspective
- View: A tiny, homoiconic, prefix-concatenative core is a good target IR or DSL host for program-synthesis experiments.
- Impact: Systems programmers, language researchers, and protocol designers gain a uniform code/data format with precise Unicode semantics.
- Watch next: More operations (numbers, files), performance measurements for recursive workloads, and IDE tooling to visualize operand/function groupings.
