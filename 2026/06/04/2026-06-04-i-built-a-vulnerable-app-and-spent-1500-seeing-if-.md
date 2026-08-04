# I built a vulnerable app and spent $1,500 seeing if LLMs could hack it

- Score: 378 | [HN](https://news.ycombinator.com/item?id=48392343) | Link: https://kasra.blog/blog/i-spent-1500-seeing-if-llms-could-hack-my-app/

### TL;DR

A researcher built a deliberately vulnerable React Native app whose hardened API masked an exposed Firebase data layer, then gave autonomous agents two hours and $10 per run to retrieve a private-review flag. GPT-5.5 solved 7/10 trials, DeepSeek V4 Pro 3/10, and two Claude models 2/10 each; most others scored zero. The author calls the $1,500 exercise non-scientific: harnesses differed, GPT had security approval, refusals and budget limits shaped outcomes, and failed infrastructure runs were omitted. HN therefore treated it as a test of autonomy plus policy, not raw capability.

### Comment pulse

- Fairness → GPT ran from an approved account while Claude and Gemini often refused — counterpoint: operational usefulness includes whether legitimate users can obtain authorization.
- Methodology → Autonomous zero-guidance runs measure CI-style operation; practitioners argued collaborative steering can unlock substantially better security work.
- Policy boundary → Models were more willing on offline or localhost artifacts than perceived live targets, making environmental framing part of benchmark behavior.

### LLM perspective

- **View:** The benchmark measures end-to-end agent success, where reasoning, persistence, tooling, cost limits, and safety policy are inseparable product properties.
- **Impact:** Security teams may use agents for triage, but reproducible autonomous auditing still needs human direction and independent verification.
- **Watch next:** Identical harnesses, matched policy access, blinded targets, larger samples, transcript scoring, vulnerability diversity, and human-agent baselines.
