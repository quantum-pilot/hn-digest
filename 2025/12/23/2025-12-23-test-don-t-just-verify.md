# Test, don't (just) verify

- Score: 154 | [HN](https://news.ycombinator.com/item?id=46364973) | Link: https://alperenkeles.com/posts/test-dont-verify/

### TL;DR

The author argues AI can accelerate formal specifications and proof generation, with small symbolic checkers validating probabilistic output, but verification cannot replace testing. Autoformalization may mistranslate intent, extraction enlarges the trusted computing base, production performance lacks tractable universal models, and false conjectures can waste proof search. Verification-guided development instead pairs a simple verified reference with a fast implementation, then uses differential random testing to check equivalence. HN commenters support stronger guarantees but dispute several technical simplifications and the article's pessimism.

### Comment pulse

- Testing supplies falsification → counterexamples quickly reject bad theorems that proof search might pursue indefinitely.
- Verification improves everyday reasoning → invariants, static types, and correctness-by-construction help even without full proofs.
- Critics challenge the framing → Lean optimizes arithmetic, hardware models exist, and reusable verified libraries may reduce specification burden.

### LLM perspective

- View: Proofs and tests answer complementary questions: logical universality versus behavior under real implementations and environments.
- Impact: AI-assisted teams can use proof checkers safely only if specifications and trusted boundaries receive independent scrutiny.
- Watch next: Measure autoformalization errors, proof maintenance, differential-test coverage, extraction trust, and production performance gaps.
