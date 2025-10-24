# Programming with Less Than Nothing

- Score: 418 | [HN](https://news.ycombinator.com/item?id=45678511) | Link: https://joshmoody.org/blog/programming-with-less-than-nothing/

- TL;DR
  - An interview parody where the candidate implements FizzBuzz purely with S/K combinators and point‑free style: booleans, numerals, arithmetic via a Y combinator, then runs it on a lazy JS interpreter (Skoobert) to avoid eager-evaluation stack blowups, prints fizz/buzz/number, and finally inlines everything into one gargantuan S/K expression. HN debates what combinators are good for, notes lambda calculus is generally more concise, shows how to simulate laziness with thunks in eager languages, and splits between “clever party trick” and “great explainer.”

- Comment pulse
  - Combinators as minimal instruction set → Pure, stateless functions compose; an SK base can underlie Lisp or VMs—counterpoint: performance requires richer primitives than graph rewriting.
  - Lambda calculus vs CL size → LC encodes programs shorter; fastest LC interpreters translate to larger combinator bases; eager languages can emulate laziness with thunks.
  - Showcase vs substance → Many enjoyed the stunt; others wanted clearer exposition and practical numerics (e.g., two’s-complement) beyond Church encodings.

- LLM perspective
  - View: A crisp demonstration of universality and evaluation strategy trade-offs, wrapped in humor; not a template for interview solutions.
  - Impact: Reinforces compiler back-end ideas: targeting combinators or bytecodes, lazy vs eager runtimes, and point-free transformations.
  - Watch next: Publish Skoobert benchmarks, a tiny Lisp atop a pragmatic combinator set, and a thunked Y-combinator FizzBuzz in vanilla JS.
