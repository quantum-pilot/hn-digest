# Universal Claude.md – cut Claude output tokens

- Score: 446 | [HN](https://news.ycombinator.com/item?id=47581701) | Link: https://github.com/drona23/claude-token-efficient

### TL;DR

A drop-in `CLAUDE.md` tries to curb Claude’s sycophancy, repetition, formatting noise, unsolicited advice, guessing, redundant reads, and overengineering. Its tiny benchmark reduced measured output from 465 to 170 words, or 63%, across four scored prompts, but used no repeated runs or accuracy measure; the file also adds input tokens every turn, so only output-heavy persistent workflows may save overall. HN challenged the universal claim: output length may trade off against quality, and one commenter’s 30-task coding test found worse performance with the rules.

### Comment pulse

- Answer-first rules may seed confirmation bias in autoregressive generation unless hidden thinking already occurred.
- Several developers value previews because they expose misunderstandings early — counterpoint: high-volume automation benefits from terse, parseable responses.
- Stable handoff documents were proposed as a better place for durable reasoning than repeatedly carrying verbose conversational history.

### LLM perspective

- **View:** Optimize useful work per total token, not response brevity; output suppression can simply move cost into retries and corrections.
- **Impact:** The template suits repetitive batch tasks more than ambiguous implementation, architecture, or debugging sessions.
- **Watch next:** Controlled coding benchmarks, pass rates, retry counts, total input-plus-output cost, task complexity strata, and model-version drift.
