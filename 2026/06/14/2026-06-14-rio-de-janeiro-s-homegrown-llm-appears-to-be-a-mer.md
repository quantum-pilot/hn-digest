# Rio de Janeiro's "homegrown" LLM appears to be a merge of an existing model

- Score: 369 | [HN](https://news.ycombinator.com/item?id=48528371) | Link: https://github.com/nex-agi/Nex-N2/issues/4

### TL;DR

Nex-AGI researchers allege Rio de Janeiro’s advertised 397B “homegrown” model was simply an element-wise blend of Nex-N2 Pro and Qwen3.5, not independently post-trained. Their evidence: without Rio’s system prompt, it identified as Nex in 95 of 120 trials and never as Rio; tensor analysis found near-perfect collinearity with an approximately 57/43 merge across all layers. Rio’s page later credited both models and blamed an incorrect upload, saying a distilled version existed. HN debated fraud versus mishap, while agreeing that releasing the promised model would make the claim testable.

### Comment pulse

- The dispute concerns capability claims more than open-weight reuse → undisclosed merging and alleged nonexistent post-training could mislead citizens, funders, and evaluators.
- An upload mistake remains plausible → researchers say virality and mayoral promotion outran coordination — counterpoint: delayed delivery weakens the explanation.
- Linear weight blending can work → Nex shares Qwen’s base architecture, although leaderboard gains may conceal broader quality regressions.

### LLM perspective

- **View:** Open weights make model lineage auditable, turning tensors into reproducible provenance evidence rather than relying on branding.
- **Impact:** Public-sector AI teams need disclosure logs covering base models, merges, training runs, benchmark protocols, and funding.
- **Watch next:** Verify whether Rio publishes the claimed distilled checkpoint and whether independent tests reproduce its stated improvements.
