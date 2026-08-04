# Project Glasswing: what Mythos showed us

- Score: 266 | [HN](https://news.ycombinator.com/item?id=48179732) | Link: https://blog.cloudflare.com/cyber-frontier-models/

### TL;DR

Cloudflare tested Anthropic’s Mythos Preview without general-release safeguards across more than 50 repositories and found a qualitative gain: it could combine low-severity primitives into exploit chains, generate proofs, compile them, and revise failed hypotheses. High coverage still required a custom pipeline of narrow parallel hunts, independent adversarial validation, gap filling, deduplication, reachability tracing, and structured reporting; generic coding-agent sessions wandered and produced noise. HN found the harness distinction useful but judged the post promotional and under-quantified, while highlighting inconsistent model refusals and the transferable value of adversarial review.

### Comment pulse

- The post lacked proof of superiority → commenters wanted concrete numbers and surprises, seeing its claims as balanced promotion rather than an evaluation.
- The novelty is orchestration, not invocation → defenders distinguished Cloudflare’s multi-stage harness from a standard coding agent — counterpoint: the article obscured that distinction.
- Adversarial review travels well → using a separate agent to disprove findings impressed commenters as useful beyond coding, even if the lesson was familiar.

### LLM perspective

- **View:** Capability belongs to a model-system pair; exploit reasoning without coverage, validation, and reachability analysis does not create a scanner.
- **Impact:** Security teams need orchestration, sandboxing, human triage, and regression gates; faster discovery alone can increase operational risk.
- **Watch next:** Publish precision, recall, exploit success, repository coverage, validation rejection, refusal consistency, remediation regressions, and comparisons under identical harnesses.
