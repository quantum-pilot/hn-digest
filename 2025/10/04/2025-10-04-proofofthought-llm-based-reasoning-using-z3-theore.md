# ProofOfThought: LLM-based reasoning using Z3 theorem proving

- Score: 159 | [HN](https://news.ycombinator.com/item?id=45475529) | Link: https://github.com/DebarghaG/proofofthought

### TL;DR

ProofOfThought is a sparse research repository wrapping an LLM and Z3 theorem prover behind Python APIs. The model translates natural-language questions into formal facts, rules, and goals; Z3 evaluates the resulting program, making the formalized reasoning inspectable and executable. It accompanies a NeurIPS 2024 workshop paper and includes batch evaluation. HN saw value in pairing fuzzy language models with deterministic solvers for mathematics and policy checks, but stressed the autoformalization gap: a proof is reliable only if the generated premises, constants, and rules faithfully represent reality.

### Comment pulse

- Solvers provide deterministic verification → LLM-generated SymPy, Prolog, Lean, or Z3 artifacts can be tested, edited, and reviewed.
- Formalization remains the weak link → incorrect or invented premises can yield valid proofs of the wrong model.
- Human review does not disappear → business-policy prototypes still required engineers to check translations and resolve ambiguous source documents.

### LLM perspective

- View: Neurosymbolic systems relocate uncertainty from inference into translation; they do not eliminate it.
- Impact: Compliance and reasoning tools gain auditable intermediate artifacts, but reviewers inherit a demanding semantic-validation task.
- Watch next: Benchmark newer models, false positives, calibration, adversarial formalizations, reviewer effort, and domain-specific soundness.
