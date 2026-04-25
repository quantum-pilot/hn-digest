# OpenAI releases GPT-5.5 and GPT-5.5 Pro in the API

- Score: 198 | [HN](https://news.ycombinator.com/item?id=47894000) | Link: https://developers.openai.com/api/docs/changelog

- TL;DR  
OpenAI’s API changelog introduces GPT‑5.5 and higher‑compute GPT‑5.5 Pro, positioned as new frontier models for complex professional work. GPT‑5.5 brings a 1M‑token context window, multimodal input, and deep integration with tools (web search, computer use, Skills, MCP), but only supports extended prompt caching and defaults reasoning effort to medium. Hacker News reactions are mixed: some report “lazy” behavior and weak real‑world benchmarks, others see state‑of‑the‑art coding performance and prefer it to Claude, while debating possible fanboy/astroturf dynamics.

- Comment pulse  
  - GPT‑5.5 feels “lazy”, delegating work back to users to save tokens — counterpoint: others say with Codex it's reliable and less hallucinatory.  
  - Benchmarks disagree: a WordPress plugin test rates GPT‑5.5 slow and poor value, while Gertlabs’ coding evals rank it top public model.  
  - Claude vs GPT‑5.5 debate: some suspect pro‑OpenAI astroturfing; others report Claude Opus hallucinations and weaker adherence to project instructions.

- LLM perspective  
  - View: For devs, behavior depends heavily on prompts and reasoning_effort; defaults may prioritize brevity, so explicit guidance is key.  
  - Impact: Largest benefits likely for long‑context, tool‑heavy agents using Responses API features like Skills, computer use, and extended caching.  
  - Watch next: Independent, task‑specific evals (coding, agents, chat UX) and pricing changes will determine whether teams migrate from 5.4 or competitors.
