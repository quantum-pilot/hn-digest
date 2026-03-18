# GPT‑5.4 Mini and Nano

- Score: 203 | [HN](https://news.ycombinator.com/item?id=47415441) | Link: https://openai.com/index/introducing-gpt-5-4-mini-and-nano

- TL;DR  
  OpenAI’s GPT‑5.4 mini and nano shrink much of GPT‑5.4’s capability into cheaper, faster models aimed at coding, subagents, and computer-use tasks. Mini runs over 2× faster than GPT‑5 mini while approaching 5.4’s scores on SWE‑Bench Pro and OSWorld; nano targets ultra‑low‑cost classification and simple coding helpers. APIs expose long context, tool use, and multimodal input at $0.75M/$4.50M (mini) and $0.20M/$1.25M (nano). HN readers praise speed and pricing but debate agent reliability, rising “cheap tier” costs, and evaluation-by-vibes.

- Comment pulse  
  - Raw tests show mini/nano output 180–200 tokens/s and undercut Claude/Gemini prices, but engineers stress ttft, prompt ingestion speed, and thinking level matter more.  
  - Several report GPT‑5.x agents as slow, context‑fragile, and poor at following instructions; Claude, Gemini, or fine‑tuned Qwen feel snappier and more dependable.  
  - Many see small models as where practical progress happens, yet note rising “mini” prices and gaps vs open SOTA—counterpoint: constrained automation tasks already benefit substantially.

- LLM perspective  
  - View: Signals a design era of planner–executor stacks, with frontier models delegating most work to fast, specialized subagents.  
  - Impact: Cost-sensitive dev tools, RPA pipelines, and realtime voice/chat UIs can upgrade intelligence without sacrificing latency budgets.  
  - Watch next: Independent eval suites on multi-agent workflows, latency-per-task metrics, and direct mini/nano comparisons versus Claude Haiku and Gemini Flash.
