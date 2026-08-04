# Inflect-Micro-v2: complete voice in 9.36M parameters

- Score: 198 | [HN](https://news.ycombinator.com/item?id=49053375) | Link: https://huggingface.co/owensong/Inflect-Micro-v2

### TL;DR

Inflect-Micro-v2 is an independently built, Apache-2.0, open-weight English text-to-waveform model with 9,356,513 parameters, 37.53 MB FP32 weights, an integrated 24 kHz decoder, deterministic seeds, and punctuation-aware long-text chunking. Its published four-thread CPU test produced audio at 6.28× real time; reported evidence includes 66.2% blind community preference, 4.395 predicted naturalness, and 3.99% two-ASR word error. Hacker News listeners were impressed by its size-to-quality ratio, while flagging odd inflections, one fixed male voice, no speech recognition or cloning, and uncertain microcontroller feasibility.

### Comment pulse

- Complete describes the inference path, not every speech task → the package performs TTS only; it includes normalization, phonemization, synthesis, and waveform decoding.
- Tiny weights unlock local assistants → one user replaced an older ONNX voice, while another combines STT/TTS with Home Assistant and a local LLM.
- Naturalness remains uneven → listeners said it avoids a robotic sound — counterpoint: prosody and inflections can still feel strange.

### LLM perspective

- **View:** A compact full-stack model can outperform a larger component-only model operationally by reducing memory, dependencies, latency, and deployment friction.
- **Impact:** Offline products gain privacy and resilience, particularly embedded assistants, accessibility tools, kiosks, and low-cost edge devices.
- **Watch next:** Benchmark ONNX on microcontrollers, collect formal MOS, and test adaptation across voices, languages, names, and long passages.
