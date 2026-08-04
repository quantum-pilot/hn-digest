# Kimi K2.7-Code: open-source coding model with better token efficiency

- Score: 453 | [HN](https://news.ycombinator.com/item?id=48502347) | Link: https://huggingface.co/moonshotai/Kimi-K2.7-Code

### TL;DR

Moonshot’s Kimi K2.7 Code is a 1-trillion-parameter mixture-of-experts coding agent activating 32 billion parameters per token, with 256K context, vision, native INT4 quantization, and a modified MIT license. Moonshot reports stronger long-horizon coding and tool use than K2.6 while using about 30% fewer thinking tokens; its published scores usually trail GPT-5.5 and Claude Opus 4.8. Hacker News users found it capable on bounded and even large refactoring tasks, but said Claude remains better at intent, planning, debugging, and first-pass reliability, making real cost highly workflow-dependent.

### Comment pulse

- Real-world results impressed → a 177KB OpenSSL patch rebase reportedly succeeded from sparse instructions for an estimated $5–10.

- Per-token price misleads → weaker models need more precision and retries — counterpoint: bounded coding often reaches similar quality for less.

- Modified MIT terms drew cautious approval → attribution in product interfaces seemed reasonable, though commenters found the user-interface definition vague.

### LLM perspective

- **View:** K2.7 narrows the commodity-coding gap; agent harness quality increasingly determines whether benchmark gains reach developers.

- **Impact:** Open weights and standard API compatibility widen provider choice, but 1T-parameter hosting remains infrastructure-intensive.

- **Watch next:** Compare independent task success, total tokens, wall-clock time, retry count, test integrity, and quantized deployment cost.
