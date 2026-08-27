# Neural audio codecs: how to get audio into LLMs

- Score: 322 | [HN](https://news.ycombinator.com/item?id=45655161) | Link: https://kyutai.org/next/codec-explainer

### TL;DR

Raw audio produces tens of thousands of samples per second, making direct autoregressive modeling slow and too short-context for coherent speech. Kyutai’s explainer builds vector-quantized autoencoders, then residual vector quantization, to compress audio into discrete token levels an ordinary Transformer can predict and decode. More levels improve sound but increase sequence cost. Mimi compresses more aggressively and adds semantic tokens that preserve words while discarding speaker identity, improving linguistic coherence. Even then, native-audio models often lean on text streams and lag text models in reasoning and vocal understanding.

### Comment pulse

- Codec tradeoff → neural codecs achieve far greater compression than MP3, while conventional codecs are cheaper to run.
- Capability debate → missing pitch recognition may reflect weak audio generalization, synthetic training data, or safeguards.
- Architecture idea → hierarchical models could separate low-frequency semantic planning from high-frequency acoustic generation.

### LLM perspective

- View: Tokenization determines whether models learn speech structure or merely attach audio rendering to text reasoning.
- Impact: Better codecs reduce training cost but may discard prosody, identity, or semantics needed downstream.
- Watch next: Semantic-acoustic benchmarks, continuous latents, token scheduling, and models trained on richer non-synthetic speech.
