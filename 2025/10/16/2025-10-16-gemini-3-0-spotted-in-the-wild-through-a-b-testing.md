# Gemini 3.0 spotted in the wild through A/B testing

- Score: 265 | [HN](https://news.ycombinator.com/item?id=45607758) | Link: https://ricklamers.io/posts/gemini-3-spotted-in-the-wild/

- TL;DR
    Rick Lamers surfaced a likely Gemini 3.0 checkpoint via Google AI Studio’s A/B test and used SVG generation (Xbox controller) as a fast quality proxy popularized by Simon Willison. The model’s SVG beat Gemini 2.5 Pro’s, with ~24s higher first-token latency and ~40% longer outputs, suggesting more internal reasoning but not heavy test-time compute. HN split: practitioners praise Gemini 2.5 for UI/web dev, creative writing, and math; skeptics dismiss single‑prompt A/B hype, noting missing tool/grounding tests and limited internal access to 3.0 at Google.

- Comment pulse
    - Gemini 2.5 often best for UI/UX web dev, creative writing, and math → users report stronger code advice and nuanced feedback versus Claude/GPT.
    - A/B SVG wins don’t prove real performance → single prompts miss tool-calls, multi-file ingest, grounding, latency trade-offs — counterpoint: visual tasks correlate well in practice.
    - Internal availability unclear → Googlers say 3.0 isn’t broadly accessible; experiments may hit tuned 2.5 variants.

- LLM perspective
    - View: SVG skill is a decent smoke test, not a benchmark; wait for diverse evals before declaring leadership.
    - Impact: If 3.0 improves coding and tool reliability, IDE copilots and agent frameworks could consolidate around Google’s stack.
    - Watch next: Hard benchmarks: SWE-bench Verified, HumanEval+, AgentBench; tool-use stability, retrieval grounding quality, latency/price per token, context size, multimodal fidelity.
