# ProofOfThought: LLM-based reasoning using Z3 theorem proving

- Score: 159 | [HN](https://news.ycombinator.com/item?id=45475529) | Link: https://github.com/DebarghaG/proofofthought

- TL;DR
  - ProofOfThought pairs an LLM with the Z3 theorem prover: the model translates questions into constraints, and Z3 derives answers with a readable proof state. It exposes a simple Python API and a JSON DSL, plus batch evaluation. HN readers like LLM+formal-tool hybrids (SymPy, Prolog/Datalog) for verifiable math/logic, but highlight the hard autoformalization gap, oversight burden, and high false positives reported. Authors argue newer models mirror reasoning better and confined-policy verification can deliver high soundness in production.

- Comment pulse
  - Neurosymbolic hybrids outperform pure LLMs on math/logic → LLM drafts code/constraints; solvers execute reliably, producing verifiable artifacts — counterpoint: a dedicated CAS may be simpler.
  - Prefer Prolog/Datalog encodings → LLMs map language to logic well; Z3’s Datalog can be more ergonomic than SMT-LIB for certain problems.
  - Autoformalization is the bottleneck → translating policy/wiki text requires experts; unsound facts inflate false positives; prefer deterministic oracles over LLM-as-judge; newer models reportedly help.

- LLM perspective
  - View: Program synthesis plus constraint solving; correctness hinges on faithful formalization, not solver performance.
  - Impact: Strong fit for policy compliance, access control, and safety checks where models generate candidates and solvers certify.
  - Watch next: Benchmark autoformalization accuracy, FPR/FNR on diverse domains; head-to-head with Prolog/Datalog; human-in-the-loop tooling for reviewing generated constraints.
