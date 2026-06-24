# Unlimited OCR: One-shot long-horizon parsing

- Score: 430 | [HN](https://news.ycombinator.com/item?id=48643426) | Link: https://github.com/baidu/Unlimited-OCR

## TL;DR
Unlimited OCR proposes “Reference Sliding Window Attention” (R‑SWA) to OCR arbitrarily long documents on fixed VRAM. The model keeps a full global view of the original page image, but only remembers a small sliding window of its *own* generated text. This caps KV cache growth while preserving document context, enabling streaming, one-pass parsing instead of page-chunk hacks. HN discusses extending this to long conversations, questions the tiny local window size, and contrasts strong text OCR with still-abysmal music OCR/OMR.

*Content unavailable; summarizing from title/comments.*

## Comment pulse
- R‑SWA decouples visual context from text history → unbounded OCR with bounded KV cache, promising for conversations too—counterpoint: a ~128-word local window seems uncomfortably small.
- Practitioners already slice big documents or images into chunks for OCR → avoids VRAM spikes and often beats whole-image OCR, though it loses true global context.
- Music OMR lags far behind OCR → rich notation, weak corpora and formats (MEI, MusicXML, etc.) make AI misread scores; niche tools like Soundslice are rare standouts.

## LLM perspective
- View: R‑SWA formalizes a streaming pattern: persistent input state plus aggressively pruned output state; likely reusable for code, logs, and dialogues.
- Impact: Makes serious local document and media understanding feasible on consumer GPUs, improving privacy-preserving RAG and assistive tools.
- Watch next: Standardized long-document benchmarks, open implementations, and integration of R‑SWA-like attention into mainstream LLM toolchains.
