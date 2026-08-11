# Nvidia PersonaPlex 7B on Apple Silicon: Full-Duplex Speech-to-Speech in Swift

- Score: 353 | [HN](https://news.ycombinator.com/item?id=47258801) | Link: https://blog.ivan.digital/nvidia-personaplex-7b-on-apple-silicon-full-duplex-speech-to-speech-in-native-swift-with-mlx-0aa5276f2e23

### TL;DR

An open-source Swift/MLX port runs Nvidia’s 7-billion-parameter PersonaPlex speech-to-speech model locally on Apple Silicon, using about 5.3 GB after 4-bit quantization. On an M2 Max, generation averages 68 milliseconds per 80-millisecond frame, aided by batched prefills, fewer synchronization barriers, bulk audio extraction, and optional Metal compilation. The architecture jointly models text and two audio streams to support natural overlap and turn-taking. HN welcomed the engineering but corrected the pitch: this port currently accepts WAV input and streams generated chunks; live, interactive full-duplex conversation is not implemented.

### Comment pulse

- Full-duplex speech offers backchannels and natural turn-taking — counterpoint: modular ASR→LLM→TTS pipelines are easier to improve, scale, and equip with tools.
- A parallel “brain” could handle tools while PersonaPlex fills latency, but coordinating overrides before the fast model hallucinates remains unsolved.
- Reported M2 Max speed did not generalize: one M1 Max tester saw ten-second, unrelated replies, highlighting hardware and prompting sensitivity.

### LLM perspective

- **View:** This release proves efficient local inference mechanics, not yet a production voice-agent experience.
- **Impact:** Apple developers gain reusable Swift components; users still need live capture, orchestration, evaluation, and safety layers.
- **Watch next:** Microphone duplex, interruption handling, tool arbitration, broader hardware benchmarks, semantic accuracy, and voice-quality tests.
