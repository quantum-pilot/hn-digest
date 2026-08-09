# Leanstral: Open-Source foundation for trustworthy vibe-coding

- Score: 233 | [HN](https://news.ycombinator.com/item?id=47404796) | Link: https://mistral.ai/news/leanstral

### TL;DR

Mistral released Leanstral, an Apache‑2.0 sparse code agent with 120B total and 6B active parameters, specialized for Lean 4 proof engineering in realistic repositories. Lean itself verifies parallel attempts, while Vibe, a limited-period API, downloadable weights, and MCP support broaden access. On Mistral’s FLTEval, one pass scored 21.9 for $18; two scored 26.3 for $36, beating Sonnet’s 23.7 at $549, while 16 passes reached 31.9 but remained below Opus’s 39.6 at $1,650. HN welcomed open specialization but questioned benchmark framing and whether maximum quality outweighs cost.

### Comment pulse

- Repeated verified attempts change economics → pass@2 beats Haiku and Sonnet cheaply — counterpoint: Opus still leads substantially on correctness.
- Formal feedback resembles red-green TDD → Lean supplies an exact acceptance signal rather than relying on subjective code review.
- Openness matters beyond leaderboard rank → downloadable weights and diverse training organizations benefit sensitive or locally controlled proof workflows.

### LLM perspective

- **View:** Specialized agents can convert inference budget into verified outputs, making pass scaling more meaningful than unverified sampling.
- **Impact:** Lean users gain a local, inspectable assistant for migrations, repository proofs, and formalized software specifications.
- **Watch next:** FLTEval release, reproducible costs, Codex comparisons, proof novelty, hallucinated specifications, and performance outside the FLT repository.
