# Granite 4.1: IBM's 8B Model Matching 32B MoE

- Score: 273 | [HN](https://news.ycombinator.com/item?id=47960507) | Link: https://firethering.com/granite-4-1-ibm-open-source-model-family/

### TL;DR  
Granite 4.1 is IBM’s new open-source family of 3B/8B/30B dense LLMs where the 8B model matches or beats IBM’s prior 32B MoE and rivals larger open models on chat, math, coding, and tools. Gains come from a huge, carefully staged training set, strict LLM-judged data filtering, and multi-step RL that fixes RLHF-induced regressions, plus staged extension to 512K context without wrecking short-range performance. Apache-2.0-licensed with FP8 variants, Granite runs easily via Ollama/vLLM; HN users find the 8B strong locally but still lean on Qwen/Gemma for heavy coding.

---

### Comment pulse
- Early testers: 8B Granite runs fast on commodity GPUs and benefits from fresh training data, but Qwen 3.6 35B still wins for serious coding.  
- Some argue 8B is overkill for autocomplete, preferring ~1B models or Qwen-Coder-Next; others want Gemma 4-style tool-use capability in similarly compact models.  
- Community also flags Granite-Vision 4.1-4B as a promising mini vision model, and trades tips on Claude-like local UIs (Jan, LM Studio, llama.cpp—counterpoint: OpenWebUI feels unstable).

---

### LLM perspective
- View: Training-pipeline engineering and data curation now yield better returns than just scaling parameter counts or adding MoE complexity.  
- Impact: Enterprises gain clean mid-size models deployable on modest hardware for RAG, tools, and code, easing dependence on closed APIs.  
- Watch next: Third-party evals versus Gemma/Qwen, 512K-context workloads, and whether the 4B vision model holds up for document extraction.
