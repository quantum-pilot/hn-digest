# A walk through of the DeltaNet family of linear attention variants

- Score: 282 | [HN](https://news.ycombinator.com/item?id=49085909) | Link: https://blog.doubleword.ai/you-could-have-come-up-with-kimi-delta-attention

## TL;DR
The article demystifies Kimi Delta Attention by deriving it step‑by‑step from standard softmax attention. It reframes attention as a fixed-size associative memory matrix updated with a delta rule: instead of adding new values, the model writes prediction errors at specific keys. DeltaNet adds this error-based update; Gated DeltaNet adds global forgetting; KDA refines this to per-key-channel decay via a diagonal-plus-low-rank transition. Finally, it shows how the same recurrence is implemented twice: a simple recurrent kernel for decoding and a chunkwise, tensor-core-friendly schedule for training.

---

## Comment pulse
- Math notation debate → Some love bra–ket’s clarity and terseness; others prefer explicit types or pseudocode for readability. — counterpoint: article’s notation switch earns praise.  
- Accessibility concern → Symbols like k, q, S are never fully defined, making the piece opaque to readers without prior attention/ML background.  
- “You could have come up with…” → Title feels dismissive; turning a hard research contribution into hindsight-trivial “you too” marketing annoys several readers.

---

## LLM perspective
- View: Error-based, gated linear attention is becoming a practical, drop-in alternative to softmax for long-context LLMs.  
- Impact: Inference providers, open-source model authors, and compiler/kernel teams gain clearer mental models for optimizing KDA-style attention.  
- Watch next: Benchmarks vs FlashAttention on quality/latency, open implementations in major frameworks, and training large models natively on KDA.
