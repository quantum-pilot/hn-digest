# DeepSeek OCR

- Score: 850 | [HN](https://news.ycombinator.com/item?id=45640594) | Link: https://github.com/deepseek-ai/DeepSeek-OCR

- TL;DR
  - DeepSeek-OCR reframes OCR as “context optical compression,” converting pages into short vision-token sequences to cut LLM context cost. The paper claims ~10× near-lossless compression and ~60% accuracy at 20×, with multi-resolution modes and vLLM/Transformers inference. HN debates the information-theory: continuous vision embeddings versus discrete text IDs, resolution/patch trade-offs, and quadratic token compute savings. Early tests look strong but show hallucination/merge errors. Benchmarks favor OmniDocBench; pipelines (layout→OCR) still beat end-to-end VLMs; cloud OCR likely wins on real business docs.

- Comment pulse
  - Vision vs text → text uses discrete IDs; vision tokens are continuous embeddings, denser but larger. — counterpoint: benefits depend on resolution and patch size.
  - Compression motivation → fewer vision tokens cut quadratic LLM compute; downscaling images trades detail for context; propose rendering text as images to shrink tokens.
  - Reality check → prefer OmniDocBench; pipelines (layout→reading order→OCR) beat end-to-end VLMs; cloud OCR often wins on business docs; early tests show hallucinations/merging errors.

- LLM perspective
  - View: Treat OCR as token-budget compression; exploit semantic embeddings to pack pages while managing resolution-induced information loss.
  - Impact: Cheaper long-document QA/RAG, faster batch OCR on GPUs, and potential on-device OCR if smaller variants emerge.
  - Watch next: OmniDocBench scores vs Azure/Google, standardized compression–accuracy curves, table/CJK stress tests, and clarity on training data and licensing.
