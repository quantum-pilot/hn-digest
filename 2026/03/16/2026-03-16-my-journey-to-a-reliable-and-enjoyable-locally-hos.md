# My Journey to a reliable and enjoyable locally hosted voice assistant (2025)

- Score: 303 | [HN](https://news.ycombinator.com/item?id=47398534) | Link: https://community.home-assistant.io/t/my-journey-to-a-reliable-and-enjoyable-locally-hosted-voice-assistant/944860

### TL;DR
A Home Assistant user describes replacing Google/Nest speakers with a fully local voice stack: HA Assist + llama.cpp on a GPU box, Parakeet V2 for speech-to-text, and Kokoro/Piper for speech output. They benchmark multiple GPUs and GGUF models (GPT-OSS:20B, Unsloth Qwen variants), showing that quantization, context size, and prompt design strongly affect tool use and reliability. Extra HA automations handle music, weather, unclear commands, and custom wake words; later updates add camera understanding via Frigate and a vision LLM. HN comments focus on TTS prosody, wake-word pain, and whether talking to assistants is even desirable.

---

### Comment pulse
- TTS quality is a major bottleneck → read-speech-trained voices sound unnatural conversationally; folks suggest XTTS, mlx-audio with Qwen/Chatterbox, and better conversational datasets.  
- Wake-word reliability dominates UX → HA devices miss activations vs Echo; proposals include better mic arrays, claps/buttons, or presence-based triggers—counterpoint: many commands need only a chime, not speech.  
- Attitudes to voice are split → some see phones as “failure” compared to ambient control; others use assistants only for timers, driving, or quick reminders.

---

### LLM perspective
- View: Local assistants are practical but still tinker-heavy: model choice, quantization, prompts, and HA glue code matter more than raw FLOPs.  
- Impact: Power users gain a replicable architecture; vendors can mine this for sane defaults on prompts, tools, and wake-words.  
- Watch next: Standardized home-assistant evals (latency, tool use, misfires), robust open wake-word models, and TTS/ASR tuned for noisy, conversational households.
