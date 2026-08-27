# Gemini 2.5 Computer Use model

- Score: 417 | [HN](https://news.ycombinator.com/item?id=45507936) | Link: https://blog.google/technology/google-deepmind/gemini-computer-use-model/

### TL;DR

Google released Gemini 2.5 Computer Use in public preview through AI Studio and Vertex AI. An agent loop sends the model a task, screenshot, recent actions, and URL; the model returns clicks, typing, or other function calls, the client executes them, and the updated state returns for another step. Google says it leads several browser and mobile-control benchmarks at lower latency, though supplied results mix self-reported and third-party evaluations. It is browser-focused, not optimized for desktop control, and includes confirmation and per-step safety mechanisms.

### Comment pulse

- Demo users found login and website interaction impressive but still observed elementary visual interpretation failures.
- A reported CAPTCHA success came from Browserbase's solver, not the model itself.

### LLM perspective

- View: The release packages visual browsing into an API loop, while reliability remains task- and harness-dependent.
- Impact: UI agents can automate systems without APIs but inherit ambiguity, prompt injection, and destructive-action risk.
- Watch next: Independent evaluations should measure completion, recovery, latency, and safety on changing real interfaces.
