# DeepSeek OCR

- Score: 850 | [HN](https://news.ycombinator.com/item?id=45640594) | Link: https://github.com/deepseek-ai/DeepSeek-OCR

### TL;DR

DeepSeek-OCR is an open model and toolkit for converting document images to text or Markdown while studying “visual-text compression.” The repository provides vLLM and Transformers inference, multiple fixed and dynamic resolutions, grounding prompts, figure parsing, and reported PDF throughput around 2,500 tokens per second on an A100. Discussion highlights the paper's claim of near-lossless OCR around tenfold token compression and 60% accuracy around twentyfold compression, but real-document tests still showed omissions and hallucinated text, and commenters dispute benchmark quality and dataset transparency.

### Comment pulse

- Readers debated whether fewer vision tokens represent true information compression or simply richer continuous embeddings.
- An independent newspaper-page test looked strong but omitted fields and hallucinated a bridging passage.
- Practitioners said composed layout-and-OCR pipelines may still outperform end-to-end models on complex documents.

### LLM perspective

- View: The compression framing is more novel than the OCR interface, but token-count ratios need careful interpretation.
- Impact: Fewer context tokens could lower downstream model cost if extraction accuracy remains dependable.
- Watch next: Independent OmniDocBench results, business-document tests, dataset disclosure, and hallucination controls.
