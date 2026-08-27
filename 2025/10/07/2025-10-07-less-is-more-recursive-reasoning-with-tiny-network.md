# Less is more: Recursive reasoning with tiny networks

- Score: 197 | [HN](https://news.ycombinator.com/item?id=45506268) | Link: https://alexiajm.github.io/2025/09/29/tiny_recursive_models.html

### TL;DR

The proposed Tiny Recursion Model uses a seven-million-parameter network to repeatedly update a latent state and revise a candidate answer. Its author reports 45% accuracy on ARC-AGI-1 and 8% on ARC-AGI-2, arguing that iterative computation can solve selected reasoning tasks without giant foundation models or the biological hierarchy invoked by an earlier HRM design. Commenters found the direction promising but warned that specialized training, augmentation, test-time procedures, and benchmark framing make direct comparisons with general-purpose language models potentially misleading.

### Comment pulse

- Readers emphasized ablations and matching evaluation settings before treating the reported scores as a general reasoning breakthrough.
- Others saw recurrence as promising for spatial reasoning, control, and iterative error correction.

### LLM perspective

- View: TRM demonstrates parameter efficiency on narrow tasks, not a general replacement for large language models.
- Impact: Reusing a small network across steps can trade model size for iterative computation and specialization.
- Watch next: Test matched baselines, out-of-distribution transfer, compute cost, and integration with general architectures.
