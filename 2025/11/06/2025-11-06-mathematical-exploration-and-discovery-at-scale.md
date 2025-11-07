# Mathematical exploration and discovery at scale

- Score: 214 | [HN](https://news.ycombinator.com/item?id=45833162) | Link: https://terrytao.wordpress.com/2025/11/05/mathematical-exploration-and-discovery-at-scale/

- TL;DR
    Terence Tao et al. used DeepMind’s AlphaEvolve—an LLM-guided evolutionary coding agent—to explore 67 math optimization problems by evolving code that generates candidate inputs. This yielded scale, adaptability, and interpretable constructions; it rediscovered known optima, made slight improvements (e.g., finite-field Kakeya/Nikodym), and inspired human proofs, but didn’t crack major conjectures and required hardened verifiers to prevent exploits. HN characterizes it as pragmatic, compute-heavy program synthesis—useful but hype-prone—with debate over whether gains reflect LLM generalization or the evolutionary framework and expert oversight.

- Comment pulse
    - Framing: Evolutionary coding agents guided by LLMs, not LLM 'genius'; useful and scalable; avoid hype — counterpoint: Others argue this shows LLMs generalize beyond memorization.
    - Attribution: Evolutionary optimization and rigorous verifiers did the work; LLMs provided mutations; significant expert effort needed to prevent exploit-y solutions.
    - Scope: First heavy-compute passes on many problems; some AlphaEvolve outputs later improved by humans; 'robustness' renamed 'adaptability' highlighting easy integration across tasks.

- LLM perspective
    - View: LLM-guided program synthesis plus strict verification is a workable pattern for math-style search, not theorem proving.
    - Impact: Scales heuristic exploration, yields interpretable candidates, and records negative results; shifts expert time to designing non-exploitable scoring.
    - Watch next: Benchmarks for verifier robustness, ARC-style synthesis, harder number-theory tasks, and proof pipelines linking Deep Think with Lean/AlphaProof.
