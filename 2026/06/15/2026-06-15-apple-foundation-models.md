# Apple Foundation Models

- Score: 461 | [HN](https://news.ycombinator.com/item?id=48536776) | Link: https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/apple-foundation-models

### TL;DR

Anthropic’s beta Swift package adapts Claude to Apple’s Foundation Models `LanguageModel` protocol, letting iOS, macOS, visionOS, and watchOS 27 apps use the same `LanguageModelSession` interface for Claude or Apple’s on-device model. It supports streaming, structured generation, tools, images, and framework-shaped errors; Claude requests go directly to Anthropic and require API billing, with a production proxy recommended to protect credentials. HN saw a provider abstraction that could commoditize models and simplify routing, but emphasized that Claude remains cloud-hosted, Gemini also integrates, and Apple may capture UX control or deepen platform lock-in.

### Comment pulse

- A common interface shifts power upward → applications can route among local and cloud providers while Apple owns the session, tool, and transcript abstractions.

- This is not local Claude → users hoping to run frontier coding models on Neural Engine hardware still face memory and performance limits.

- Device-wide defaults reduce duplication → Apple’s shared model avoids every app bundling weights — counterpoint: third-party providers preserve capability choice within Apple’s platform.

### LLM perspective

- **View:** Apple is defining the orchestration contract, making model selection swappable while retaining leverage over application architecture.

- **Impact:** Swift developers gain one integration surface; model vendors compete behind it on quality, privacy, latency, tools, and price.

- **Watch next:** Track OS 27 API changes, proxy patterns, provider parity, transcript portability, custom-model deduplication, and Apple’s commercial terms.
