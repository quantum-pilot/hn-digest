# VibeThinker: 3B param model that beats Opus 4.5 on reasoning with novel SFT+GRPO

- Score: 373 | [HN](https://news.ycombinator.com/item?id=48639240) | Link: https://arxiv.org/abs/2606.16140

- TL;DR  
  VibeThinker is a 3B-parameter reasoning-focused LLM trained with supervised fine-tuning plus GRPO that reportedly beats Claude Opus 4.5 on math and Python benchmarks. It generates long chains-of-thought for closed-world, verifiable tasks, but lacks tools, multi-turn memory, and broad knowledge. HN sees it as evidence that small, specialized models can rival frontier systems for narrow workloads and run on modest or ASIC hardware, while debating how much embedded world knowledge is still needed versus pure “reasoning modules.”

  *Content unavailable; summarizing from title/comments.*

- Comment pulse  
  - Reasoning-only tiny models vision → train small networks to think and browse for facts—counterpoint: token-prediction needs large corpora; reasoning emerges from broad data.  
  - Small but mighty models → VibeThinker excels at math/Python chain-of-thought, yet fails at conversation, open-ended research, or tool-using agent work.  
  - Hardware and specialization angle → 3B-domain models could fit single ASICs like Taalas, enabling fast local reasoning modules for developer tools and embedded systems.

- LLM perspective  
  - View: Treat VibeThinker as a pluggable reasoning engine behind agents that handle tools, browsing, and long-term context.  
  - Impact: Low-resource teams gain strong math/coding solvers running on desktops or edge chips instead of paid API calls.  
  - Watch next: Compare against Qwen, Llama 3.2, and Mistral SLMs on realistic multi-step coding and contest-math benchmarks, not just leaderboards.
