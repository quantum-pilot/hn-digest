# The local LLM ecosystem doesn’t need Ollama

- Score: 596 | [HN](https://news.ycombinator.com/item?id=47788385) | Link: https://sleepingrobots.com/dreams/stop-using-ollama/

### TL;DR

The author argues Ollama’s early one-command wrapper made llama.cpp accessible but no longer justifies using it. He alleges delayed attribution and MIT-license compliance, a slower and less compatible forked backend, misleading model names, a briefly closed-source GUI, redundant Modelfiles, limited quantizations, registry lock-in, and a privacy-blurring cloud pivot. He recommends llama.cpp directly or alternatives including LM Studio, Jan, Msty, koboldcpp, Ramalama, and llama-swap. Commenters agreed the history matters but stressed Ollama’s unmatched onboarding and model-management convenience.

### Comment pulse

- Ease remains Ollama’s defense: one command hides drivers and configuration that alternatives still expose.
- Readers valued the attribution history — counterpoint: permissive MIT obligations stop at retaining notices, not broader reciprocity.
- Power users cited stale backends and opaque storage; others find llama.cpp’s newer GUI and router much improved.

### LLM perspective

- Convenience is substantive engineering, but it does not excuse provenance, disclosure, or interoperability failures.
- A credible successor needs one-command installation, Hugging Face access, a catalog, an API, and transparent GGUF storage.
- Compare current versions on identical models: throughput, templates, tools, vision, context, and upgrade cadence.
