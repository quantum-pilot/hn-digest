# Unlimited OCR: One-shot long-horizon parsing

- Score: 430 | [HN](https://news.ycombinator.com/item?id=48643426) | Link: https://github.com/baidu/Unlimited-OCR

### TL;DR

Baidu’s open Unlimited-OCR model parses multiple document pages in one generation while limiting long-output memory growth. Its Reference Sliding Window Attention reportedly preserves full access to source images but retains only a moving window of generated text, reducing the linear KV-cache burden that usually forces page-by-page OCR. The released Transformers and SGLang paths support local NVIDIA-GPU inference, 32,768-token output, PDFs, streaming, and concurrent batches. HN welcomed the architecture for local workflows but questioned window size, novelty versus existing sliding attention, and whether it can advance neglected optical music recognition.

### Comment pulse

- Memory savings drive interest → commenters saw bounded generation context as a path to long local OCR without linearly growing VRAM or page-gluing pipelines.
- The architectural claim needs clarification → readers questioned whether major models already use sliding windows and whether a 128-unit local window preserves enough context.
- Optical music recognition remains a harder frontier → dense graphical grammar, incomplete notation formats, and scarce paired corpora frustrate reliable score transcription.

### LLM perspective

- **View:** Separating persistent visual reference from bounded text history is the core systems idea; output remains capped at 32,768 tokens.
- **Impact:** Local RAG and archive pipelines may process longer documents with steadier memory use and less page-boundary stitching.
- **Watch next:** Publish memory scaling, throughput, long-document accuracy, cross-page coherence, window-size ablations, and comparisons with chunked OCR and sliding attention.
