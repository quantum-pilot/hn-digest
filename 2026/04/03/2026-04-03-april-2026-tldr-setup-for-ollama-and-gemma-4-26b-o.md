# April 2026 TLDR Setup for Ollama and Gemma 4 26B on a Mac mini

- Score: 290 | [HN](https://news.ycombinator.com/item?id=47624731) | Link: https://gist.github.com/greenstevester/fc49b4e60a4fef9effc79066c1033ae5

### TL;DR

Despite the 26B headline, the guide ultimately recommends Gemma 4’s default 8B quantization on a 24GB Apple Silicon Mac mini: it occupies about 9.6GB, while the 26B build reportedly uses roughly 17GB and triggers swapping under concurrency. It walks through installing Ollama, launching at login, preloading the model every five minutes, keeping it resident, and using the local API. Commenters warn launch-day runtimes and quantizations can break tool calls, and generally do not view local models as Claude replacements.

### Comment pulse

- Early failures may reflect immature inference engines or quantizations, so update both and retest before blaming Gemma.
- Local models offer privacy and offline utility, but most commenters find them weaker than Claude for complex coding.
- Prospective hardware buyers should trial hosted versions first; cold starts, latency, and reliability can erase self-hosting’s appeal.

### LLM perspective

- **View:** The recipe is practical, but its model naming and persistence advice need careful verification.
- **Impact:** Developers gain private local inference; production users inherit update, memory, and reliability work.
- **Watch next:** Stable tool calling across Ollama, llama.cpp, and quantizations, plus measured throughput under concurrent agent workloads.
