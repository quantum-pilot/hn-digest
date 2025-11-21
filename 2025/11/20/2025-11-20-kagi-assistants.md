# Kagi Assistants

- Score: 112 | [HN](https://news.ycombinator.com/item?id=45997294) | Link: https://blog.kagi.com/kagi-assistants

## TL;DR
Kagi is launching two “research assistants” on top of its search engine: Quick Assistant (fast, concise answers, all plans) and Research Assistant (slower, deep multi-step investigations, Ultimate tier). They act as “deep search” agents, running parallel queries, calling tools (code, Wolfram, news, etc.), and always citing and ranking sources instead of emitting long, opaque reports. Kagi benchmarked extremely well on SimpleQA but intentionally stopped optimizing, arguing that chasing public benchmarks causes overfitting, ethical compromises, and enshrines dataset authors’ biases.

---

## Comment pulse
- Kagi as LLM backend → Cleaner, less spammy results than Google/Bing, so models hallucinate less. — counterpoint: “just rank Wikipedia” helps only narrow fact queries.
- Hallucination handling → Example where Gemini invents a 2025 conference, but Kagi correctly declines to answer, suggesting safer prompt handling and grounding.
- UX and scope → Users like browser “? / !quick / !research” shortcuts, but some are unsure how Quick/Research differ from existing Kagi model picker.

---

## LLM perspective
- View: Best assistants will be “search-native” agents that orchestrate multiple tools, not just bigger static chat models.
- Impact: High-signal search backends become critical infrastructure for any serious AI assistant or agent framework.
- Watch next: Independent benchmarks of “deep search” agents, Kagi integration into editors/IDEs, and whether Google cleans up results to stay attractive as an AI backend.
