# Show HN: Needle: We Distilled Gemini Tool Calling into a 26M Model

- Score: 243 | [HN](https://news.ycombinator.com/item?id=48111896) | Link: https://github.com/cactus-compute/needle

### TL;DR

Needle is an open 26-million-parameter, INT4 function-calling model distilled from Gemini 3.1 for phones, watches, and other constrained devices. Its encoder-decoder Simple Attention Network was pretrained on 200B tokens and post-trained on 2B synthetic single-shot tool calls; Cactus reports a 14 MB footprint, 6,000-token/s prefill, and 1,200-token/s decoding. The repository includes weights, data generation, local testing, and one-command fine-tuning. It reportedly beats several 270M–600M rivals on this narrow task, while warning that broader conversational models retain more capacity. HN imagined natural-language CLIs and private agent swarms, and requested browser deployment.

### Comment pulse

- A 14 MB embedded parser could map natural-language CLI requests to deterministic flags, though per-tool bundling adds storage and compute.
- Privacy-focused developers saw tiny specialist models as components for local orchestrated agents rather than one general conversational model.
- Browser interest centered on ONNX or WebGPU and a hosted playground; authors said local setup is easy but public scaling remains unresolved.

### LLM perspective

- View: Needle treats tool choice as compact structured prediction, showing specialization can trade generality for dramatic size and latency reductions.
- Impact: Applications can interpret flexible commands locally, preserving privacy and offline operation on consumer hardware where general LLMs are impractical.
- Watch next: Independent accuracy, malformed-call, latency, energy, and multi-turn evaluations; ONNX/WebGPU exports; robustness after tool-specific fine-tuning.
