# New coding models and integrations

- Score: 205 | [HN](https://news.ycombinator.com/item?id=45601834) | Link: https://ollama.com/blog/coding-models

### TL;DR

Ollama added cloud access to GLM-4.6 and Qwen3-Coder-480B, while updating the locally runnable Qwen3-Coder-30B for faster, more reliable tool calling in its new engine. The 480B model can also run locally for users with more than 300GB of VRAM. Ollama documents connections through VS Code, Zed, Droid, Codex, Cline, Roo Code, and its cloud API, using the local Ollama endpoint as a common interface. The announcement demonstrates setup and a generated game, but provides no comparative benchmarks, pricing analysis, or reliability evaluation.

### Comment pulse

- Several commenters reported strong GLM-4.6 experiences, including coding and Lean work, but these were individual anecdotes.
- Local-model users noted newly merged experimental Vulkan support could broaden acceleration beyond officially supported GPU paths.
- A laptop user found local coding models slow and weak, illustrating how hardware and task scope shape practicality.

### LLM perspective

- View: The release’s main contribution is deployment choice and tool compatibility, not demonstrated model superiority.
- Impact: A shared endpoint lets developers switch between cloud and local models without replacing their editor workflow.
- Watch next: Compare latency, limits, tool-call accuracy, privacy boundaries, and total cost on representative coding tasks.
