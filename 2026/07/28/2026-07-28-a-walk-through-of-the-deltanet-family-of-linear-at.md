# A walk through of the DeltaNet family of linear attention variants

- Score: 282 | [HN](https://news.ycombinator.com/item?id=49085909) | Link: https://blog.doubleword.ai/you-could-have-come-up-with-kimi-delta-attention

### TL;DR

The tutorial derives Kimi Delta Attention from ordinary causal attention. Removing softmax compresses history into a fixed-size matrix but turns writes into interfering additions. DeltaNet instead writes the prediction error, approximating assignment; Gated DeltaNet adds one learned forgetting rate; KDA upgrades that to per-key-channel retention. It then shows equivalent recurrent Triton kernels for low-latency decoding and chunkwise matrix operations for training and prefill. Commenters valued the bra-ket/conventional-notation toggle but debated terseness, undefined variables, accessibility, and whether the title understates how difficult architectural invention is.

### Comment pulse

- Notation is real friction → inconsistent symbols impede cross-paper learning, while the article’s live bra-ket switch helps readers choose a representation.
- Terseness trades onboarding for fluency → equations become compact after learning symbols — counterpoint: pseudocode and explicit types may be clearer initially.
- Simple hindsight is not simple invention → a clean derivation can conceal the hard creative work required to discover the architecture.

### LLM perspective

- View: KDA separates three memory problems: compact storage, targeted correction, and selective forgetting.
- Impact: Implementers can map one recurrence to different hardware schedules without changing model semantics.
- Watch next: Compare recurrent and chunkwise numerical equivalence, throughput, memory use, and training stability across sequence lengths.
