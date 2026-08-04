# GPT-5.6 used a prompt to close a 30-year gap in convex optimization

- Score: 482 | [HN](https://news.ycombinator.com/item?id=48957779) | Link: https://old.reddit.com/r/math/comments/1uxj3cy/after_openais_cdc_proof_announcement_gpt56_used_a/

### TL;DR

The linked source was blocked, so the available account comes entirely from discussion. Commenters describe a claimed proof that optimizing bounded convex Lipschitz functions requires Ω(d²) function evaluations, matching the runtime of a roughly 30-year-old algorithm and closing its lower-bound gap. A knowledgeable reader called that a genuine, though niche, contribution. Attribution is contested: the researcher reportedly spent a year exploring the problem with earlier models, supplied a ten-page prompt containing plausible techniques and the ultimately useful max-of-affine-functions construction, then obtained the result from GPT-5.6 Sol Pro in 148 minutes.

### Comment pulse

- Experts separated upper and lower bounds → timing an algorithm gives an upper bound, while proving Ω(d²) requires ruling out every faster algorithm.
- Credit was the main fault line → supporters saw model-assisted discovery; skeptics saw a human-curated technique, extensive prior work, and misleading “148 minutes” framing.
- Training concerns broadened the debate → automating tractable research may remove the junior problems that teach future mathematicians to become independent experts.

### LLM perspective

- **View:** The result matters independently of authorship, but evaluating AI contribution requires a provenance trail from prior chats through verification.
- **Impact:** Long expert prompts make mathematical taste scarce, shifting researchers from direct proving toward problem formulation, orchestration, and verification.
- **Watch next:** Independent proof review, formalization, exact model and tool disclosure, prompt publication, memory-access clarification, and comparison against expert-only baselines.
