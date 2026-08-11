# Can you reverse engineer our neural network?

- Score: 252 | [HN](https://news.ycombinator.com/item?id=47146487) | Link: https://blog.janestreet.com/can-you-reverse-engineer-our-neural-network/

### TL;DR

Jane Street describes a puzzle that exposes every integer weight in a hand-built neural network yet defeats normal gradient search by returning zero for almost every input. Solver Alex decoded the final layers as a 16-byte equality check, reduced millions of graph nodes, tried integer and SAT solvers, then recognized repeated circuitry as MD5. After exhaustively tracing an accidental long-input bug that proved irrelevant, he extracted the target hash and brute-forced its hinted two-word input. HN solvers compared the task to binary reverse engineering and mechanistic interpretability.

### Comment pulse

- Recognition beat optimization → periodic blocks, additions, XORs, constants, and shifts revealed a known hash rather than an arbitrary learned function.
- Once MD5 was identified, ordinary tooling won → a larger wordlist and hashcat found the answer almost immediately.
- Interpretability puzzles can open career doors → commenters reported interviews and confidence gains from comparable challenges.

### LLM perspective

- **View:** Structural priors and human design intent can matter more than brute-force compute.
- **Impact:** Researchers need visualization, graph reduction, and hypothesis-testing tools alongside gradient methods.
- **Watch next:** Jane Street’s new challenge, which asks solvers to reorder shuffled network layers.
