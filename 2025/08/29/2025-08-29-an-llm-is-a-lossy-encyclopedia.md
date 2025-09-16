# An LLM is a lossy encyclopedia

- Score: 512 | [HN](https://news.ycombinator.com/item?id=45062046) | Link: https://simonwillison.net/2025/Aug/29/lossy-encyclopedia/

- TL;DR
    - Simon Willison proposes LLMs as “lossy encyclopedias”: they compress broad facts but drop specifics. Don’t expect niche, exact setups; give a correct example and let the model act on it. HN echoes using expert supervision—like guiding a junior dev—and warns of confident mistakes (e.g., wrong drug dosages). Others argue lossiness doesn’t explain hallucinations, preferring LLMs as interfaces over retrieval-backed sources. Broader concern: fabricated quotes and a need to preserve trustworthy records.

- Comment pulse
    - Use with supervision → Users must know the domain; LLMs confidently err (e.g., 10× dosage); treat them like junior engineers and make them audit outputs.
    - Analogy contested → Lossy media degrades; LLMs fabricate and vary— counterpoint: compression artifacts can swap digits; better model is UI + retrieval, not built-in knowledge.
    - Preserve sources → AI will flood discourse; LLMs invent quotes without citations; local archives and Internet Archive become critical integrity backstops.

- LLM perspective
    - View: Treat LLMs as lossy compressors over text; ground with exemplars, tools, or docs for precision tasks.
    - Impact: Product design shifts to retrieval-first systems with citations and quote verification; UX must expose uncertainty and encourage cross-checking.
    - Watch next: Benchmarks for fine-grained specificity; calibrated confidence and self-audits; local-first archives and provenance metadata integrated into AI outputs.
