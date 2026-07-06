# Claude Design System Prompt

- Score: 115 | [HN](https://news.ycombinator.com/item?id=48792399) | Link: https://github.com/Trystan-SA/claude-design-system-prompt

## TL;DR
The shared “Claude Design System Prompt” repo is likely not Anthropic’s real internal prompt but a recreation inspired by Claude Design’s behavior. Commenters note that Claude Design’s actual skills and prompt structure, easily inspectable via browser dev tools, don’t match the repo. Without demos or proof it works, many see it as “vibes” rather than a faithful reverse‑engineering. Discussion also touches on how to practically exploit Claude Design for complex SVG animations and on murky copyright around publishing LLM‑derived prompts.  
*Content unavailable; summarizing from title/comments.*

---

## Comment pulse
- Repo authenticity questioned → skill list and structure visibly differ from real Claude Design; no demos makes it hard to justify experimentation.  
- Reverse‑engineering is trivial → prompts/skills ship in frontend and network traffic; documenting the method could help Anthropic patch access—counterpoint: transparency aids research and reproducibility.  
- Real‑world use: animated SVGs → first define geometry, then map to SVG; export as `.svg.txt` to avoid sanitizers stripping animations and to inspect for exploits.

---

## LLM perspective
- View: Treat third‑party “system prompt” repos as speculative unless they demonstrate reproducible behavior matching the original product.  
- Impact: Developers risk building on unstable interfaces; researchers gain examples of how people try to reconstruct proprietary orchestration layers.  
- Watch next: Browser‑based prompt inspection tools, clearer IP policy on LLM prompts, and official design‑system APIs or templates from model providers.
