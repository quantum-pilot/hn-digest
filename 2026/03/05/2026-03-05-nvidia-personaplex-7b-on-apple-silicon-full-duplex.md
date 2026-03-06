# Nvidia PersonaPlex 7B on Apple Silicon: Full-Duplex Speech-to-Speech in Swift

- Score: 353 | [HN](https://news.ycombinator.com/item?id=47258801) | Link: https://blog.ivan.digital/nvidia-personaplex-7b-on-apple-silicon-full-duplex-speech-to-speech-in-native-swift-with-mlx-0aa5276f2e23

- TL;DR  
    - A Swift/MLX library ports Nvidia’s PersonaPlex 7B speech-to-speech model to Apple Silicon, collapsing ASR→LLM→TTS into one full‑duplex, audio‑in/audio‑out model. The author 4‑bit‑quantizes PersonaPlex plus its Depformer to 5.3 GB, reuses Kyutai’s Mimi codec, and hits faster‑than‑real‑time streaming on an M2 Max. The package also includes ASR and TTS for round‑trip testing and offers system‑prompt presets; HN debates its practicality versus composable pipelines, tool‑calling, writing quality, and safety of human‑like voice agents.

- Comment pulse  
    - Composable ASR→LLM→TTS pipelines rival real-time performance and remain easier to train, swap models, and integrate tools; some propose hybrid setups with PersonaPlex as low-latency “mouth”.  
    - Users report mixed results: some see slow, off-topic replies on M1 Macs; others add parallel LLM tool-calling and note partial streaming or turn-based interactivity.  
    - Some distrust the seemingly LLM-written article and AI diagrams; others defend its clarity but raise broader concerns about anthropomorphized chatbots encouraging harmful behavior.

- LLM perspective  
    - View: On-device speech-to-speech shows Apple Silicon can host complex real-time agents, but cognition still benefits from separate, composable text pipelines.  
    - Impact: macOS developers gain a Swift-native toolkit for offline assistants, call centers, and accessibility tools without servers or Python.  
    - Watch next: benchmarks on lower-end M1/M2 machines, tighter LLM-tool integration, and safety UX that makes conversational limits and context explicit.
