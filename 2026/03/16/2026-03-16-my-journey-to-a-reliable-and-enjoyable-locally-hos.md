# My Journey to a reliable and enjoyable locally hosted voice assistant (2025)

- Score: 303 | [HN](https://news.ycombinator.com/item?id=47398534) | Link: https://community.home-assistant.io/t/my-journey-to-a-reliable-and-enjoyable-locally-hosted-voice-assistant/944860

### TL;DR

A Home Assistant user replaced Nest Minis with a fully local stack built around llama.cpp, Parakeet speech recognition, Kokoro or Piper speech, custom intents, and several satellites. Higher-quality quantization fixed unreliable tool calls; detailed prompts forced concise weather and search behavior; a dedicated IoT network and streaming fixed audio stalls; and a custom “Hey Robot” wake word completed the setup. Tested GPUs produced cached responses in roughly 1–4 seconds. HN admired the result but argued that wake-word pickup and conversational prosody, not the LLM, remain the biggest everyday usability gaps.

### Comment pulse

- Cloud Gemini 2.5 Flash was cheaper and easier for some — counterpoint: local processing preserves privacy and survives external outages.
- Users suggested newer speech models, while one argued 80% of home commands need only an acknowledgment sound.
- Voice excels when hands or eyes are occupied; skeptics find speaking aloud slower or awkward for most tasks.

### LLM perspective

- **View:** Reliability comes from treating speech, routing, prompts, networking, and fallback automations as one product.
- **Impact:** Technical households can own their microphones and tune behavior, but setup remains enthusiast-grade.
- **Watch next:** Family-wide wake-word recall, false activations, idle power, model support, and blinded latency tests.
