# “Why not just use Lean?”

- Score: 244 | [HN](https://news.ycombinator.com/item?id=47922079) | Link: https://lawrencecpaulson.github.io//2026/04/23/Why_not_Lean.html

## TL;DR

Paulson argues against the idea that “real” formalized math must use Lean, revisiting 60 years of prior systems (AUTOMATH, Boyer–Moore/ACL2, LCF, Coq, HOL, Isabelle, Mizar). He criticizes Lean-centric “cultism,” the assumption that propositions-as-types define all proof assistants, and the overhead of proof terms, advocating the LCF-style kernel and Isabelle’s strengths: powerful automation, readable proofs, and avoiding dependent-type complexity. He predicts AI-assisted translation will reduce lock‑in, so system choice should emphasize ergonomics and expressiveness rather than fashion.

## Comment pulse

- Lean attracts programmers: good FP tooling, expressive language, and examples of verified “real” code—counterpoint: spec clarity and developer skill still bottleneck software verification.

- Agda/Coq fans see Lean as less elegant but more usable; network effects and Mathlib matter, yet LLMs may shrink library and ecosystem lock‑in.

- Isabelle praised for logic but criticized for tooling, culture, and RAM use; Lean defenders correct Paulson’s claim that Lean must retain giant proof objects.

## LLM perspective

- View: Competing proof-assistant foundations are complementary; over-focusing on Lean or propositions-as-types risks discarding valuable LCF and set-theoretic traditions.

- Impact: Mathematicians and PL researchers may prioritize readability, automation quality, and interop over foundations, especially as AI reduces ecosystem isolation.

- Watch next: Mature hammer-style tools in Lean, AI-driven library translation between systems, and concrete memory/latency benchmarks for large-scale formalizations.
