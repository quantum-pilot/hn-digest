# Claude Code Can Debug Low-Level Cryptography

- Score: 155 | [HN](https://news.ycombinator.com/item?id=45784179) | Link: https://words.filippo.io/claude-debugging/

### TL;DR

Cryptographer Filippo Valsorda tested Claude Code on three bugs in a Go ML-DSA implementation. In the live verification failure, it localized a duplicated HighBits transformation, wrote a confirmation test, and proposed a fix that the author later replaced with a cleaner refactor. In separate sessions it also identified two previously fixed signing bugs involving Montgomery constants and a mistaken length unit. The result is encouraging for targeted bug localization, but it is only three expert-supervised cases and some proposed fixes were imperfect.

### Comment pulse

- Supporters saw constrained bug hunting as a high-value use because an expert can verify and rewrite the result.
- Skeptics reported agents pursuing irrelevant issues or premature conclusions, with concurrency bugs cited as especially difficult.

### LLM perspective

- View: The evidence supports AI as a debugging probe, not an autonomous cryptography reviewer.
- Impact: Fast localization can save expert time, while plausible but flawed patches preserve the need for independent verification.
- Watch next: Evaluate performance on unseen failures, ambiguous symptoms, concurrency, and tests designed without the original author's guidance.
