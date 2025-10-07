# Why do LLMs freak out over the seahorse emoji?

- Score: 669 | [HN](https://news.ycombinator.com/item?id=45487044) | Link: https://vgel.me/posts/seahorse/

- TL;DR
  - LLMs often insist a seahorse emoji exists. Using the logit lens on Llama‑3.3, the author shows models form a “seahorse + emoji” latent, but Unicode lacks that token. The lm_head then snaps to nearby emoji bytes (fish/horse), and autoregressive feedback makes some models spiral until they update the belief. Humans share this false memory; a proposal was rejected in 2018. Discussion debates “hallucination” vs tokenization/unembedding mismatch, alongside Unicode mix-ups and anecdotes of models melting down or looping.

- Comment pulse
  - It’s not hallucination; it’s an internal “seahorse+emoji” without a token → lm_head picks nearest emoji; RL on rollouts teaches avoidance. — counterpoint: Classic hallucination.
  - Unicode confusion persists → people recall a rejected 2018 proposal; some miscite U+1F99C as seahorse (it’s parrot), fueling LLM confidence.
  - Anecdotes: models loop or “melt down,” Copilot stuck, SCP-style jokes highlight meme-driven priors and miscalibrated certainty.

- LLM perspective
  - View: Treat this as unembedding mismatch plus belief priors, not purely reasoning failure.
  - Impact: Improves evals for hallucination taxonomy; guides RL/RLAIF to penalize unreachable-token intents.
  - Watch next: Benchmarks using non-existent emoji/entities; interventions in sampler/logit bias; tokenizer audits for emoji byte quirks.
