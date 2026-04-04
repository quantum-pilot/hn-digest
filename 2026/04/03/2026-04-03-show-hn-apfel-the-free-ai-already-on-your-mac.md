# Show HN: Apfel – The free AI already on your Mac

- Score: 636 | [HN](https://news.ycombinator.com/item?id=47624645) | Link: https://apfel.franzai.com

**TL;DR**  
Apfel is a macOS tool that exposes Apple’s built‑in on‑device LLM (used by Siri/Apple Intelligence) as a CLI, interactive chat, and OpenAI‑compatible HTTP server. It’s free, runs entirely on Apple Silicon with a 4k token context, and includes shell-friendly helpers like natural-language → command, code explanation, and git summarization. HN discussion centers on privacy benefits of local models, concerns about Apple’s relatively small/older model and update cadence, and security pitfalls of exposing localhost AI APIs—plus some evidence the model’s reasoning is still shaky.

---

**Comment pulse**

- Local-only inference is appealing for privacy and ToS risk reduction → but cloud models with zero-retention policies and TEEs may be “private enough” for most users.  
- Apple’s ~3B model is roughly last‑year Qwen‑3‑4B quality → some prefer newer downloaded models; unclear if Apple will iterate quickly.  
- Localhost OpenAI servers widen the attack surface → browser JS can hit 127.0.0.1; Apfel’s default CORS=false and optional bearer auth are safer than many peers.

---

**LLM perspective**

- View: Bridging Apple’s hidden LLM to a standard OpenAI API meaningfully lowers effort for local-first tooling and experiments.  
- Impact: macOS developers gain a zero-cost baseline model; may reduce trivial calls to OpenAI/Anthropic for noncritical tasks.  
- Watch next: Independent evals vs Gemma/Qwen, Apple’s model refresh frequency, and secure-by-default patterns for localhost AI endpoints.
