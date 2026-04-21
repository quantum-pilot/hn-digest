# Claude Token Counter, now with model comparisons

- Score: 206 | [HN](https://news.ycombinator.com/item?id=47829178) | Link: https://simonwillison.net/2026/Apr/20/claude-token-counts/

- TL;DR  
  A new version of Simon Willison’s Claude Token Counter shows Anthropic’s Opus 4.7 tokenizer often inflates token counts versus 4.6—about 1.46× for its own system prompt, ~1.08× on a long PDF, and up to 3× on very high‑resolution images it can now accept. Because pricing per token stayed fixed, many users effectively see a 10–40% cost increase. Commenters debate fairness of token-based billing, speculate on more semantic tokenization, and share strategies for aggressive token management.

- Comment pulse  
  - Token-based pricing is misleading → different tokenizers and languages produce wildly different counts, so “$ per token” hides effective price gaps across models and locales.  
  - Anthropic may use more semantic tokens → finer pieces encode structure better but inflate length — counterpoint: evidence shows little performance gain from morphology‑aware tokenizers.  
  - Users feel price hike → same per‑token rate but higher counts; they split workloads across cheaper/local models and share token‑management tricks to stay within limits.

- LLM perspective  
  - View: Tokenization is becoming a hidden pricing lever; developers must treat tokenizer choice as part of model selection and budgeting.  
  - Impact: Multilingual and vision-heavy apps see biggest swings; effective costs now hinge on content language, formatting, and especially image resolution.  
  - Watch next: Open-source token analyzers, tokenizer reverse‑engineering, and higher‑level billing metrics beyond raw tokens (characters, bytes, or normalized “work units”).
