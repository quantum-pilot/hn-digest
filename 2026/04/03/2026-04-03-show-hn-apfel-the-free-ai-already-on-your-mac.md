# Show HN: Apfel – The free AI already on your Mac

- Score: 636 | [HN](https://news.ycombinator.com/item?id=47624645) | Link: https://apfel.franzai.com

### TL;DR

Apfel wraps macOS 26’s built-in Apple Foundation Model in a Swift CLI, interactive chat, and OpenAI-compatible local server. On Apple Silicon with Apple Intelligence enabled, it runs the fixed roughly 3-billion-parameter model on-device at no token cost, with a combined 4,096-token context, streaming, tool calls, JSON, files, and shell-friendly output. HN welcomed private local inference but flagged two limits: Apple’s model may lag rapidly improving downloadable alternatives, and localhost APIs can become browser-accessible attack surfaces. A simple time-zone test also produced confidently inconsistent wrong answers.

### Comment pulse

- Local execution avoids sending private or adversarial inputs through cloud moderation — counterpoint: closed training can still embed unwanted priorities.
- Browser scripts may issue requests to loopback AI servers; commenters noted Apfel keeps the risky option off by default and supports bearer tokens.
- Apple models appear downloadable separately from OS updates, though commenters doubted Apple would match open-model release speed.

### LLM perspective

- **View:** Apfel’s contribution is accessible system integration, not a new model or expanded underlying capability.
- **Impact:** Developers gain zero-marginal-cost automation for short, privacy-sensitive tasks using hardware and software already installed.
- **Watch next:** Apple model refreshes, independent quality tests, localhost authentication defaults, CORS behavior, and longer-context support.
