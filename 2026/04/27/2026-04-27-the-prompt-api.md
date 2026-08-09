# The Prompt API

- Score: 253 | [HN](https://news.ycombinator.com/item?id=47917026) | Link: https://developer.chrome.com/docs/ai/prompt-api

### TL;DR

Chrome’s experimental Prompt API exposes on-device Gemini Nano to web pages and extensions for text generation, image and audio understanding, structured JSON, streaming, and stateful sessions. It runs offline after a shared initial model download and keeps prompts local, but currently supports only qualifying desktop hardware, requires 22 GB free storage, and excludes mobile. Hacker News envisioned tone filters and local search, while practitioners praised free private inference but warned that first-use downloads, small slow models, and browser-specific implementations undermine a seamless web API.

### Comment pulse

- A de-snarkifier could preserve facts while neutralizing hostility — counterpoint: personalized rewriting fragments shared conversations and may behave unpredictably.
- One deployed local-search use confirms privacy and zero inference cost, but model-download latency makes first use rough.
- Commenters want cross-platform model discovery selecting local or remote backends rather than APIs tied to vendor-promoted models.

### LLM perspective

- **View:** The strongest abstraction is capability negotiation, not a permanent contract with one bundled model.
- **Impact:** Sites can add private AI without servers, accounts, API keys, or native installation.
- **Watch next:** Standardization across browsers, mobile support, model upgrades, download UX, context limits, and real-device latency.
