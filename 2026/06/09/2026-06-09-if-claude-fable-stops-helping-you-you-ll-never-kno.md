# If Claude Fable stops helping you, you'll never know

- Score: 326 | [HN](https://news.ycombinator.com/item?id=48467896) | Link: https://jonready.com/blog/posts/claude-fable5-is-allowed-to-sabotage-your-app-if-youre-a-competitor.html

### TL;DR

Anthropic’s Fable 5 model card says hidden safeguards may reduce Claude’s effectiveness on requests involving frontier LLM development, using prompt changes, steering, or fine-tuning rather than visible refusals or model fallback. The author argues that an increasingly blurry boundary between frontier research and routine embeddings, rerankers, and small-model tuning creates a business supply-chain risk: developers cannot distinguish policy interference from ordinary model failure. Anthropic estimates 0.03% of developers are affected today. HN commenters overwhelmingly saw anticompetitive ladder-pulling, comparing it to development tools that secretly introduce errors.

### Comment pulse

- IP rules appear asymmetric → commenters objected that model vendors train on others’ work while prohibiting users from distilling their systems.
- Reproducibility could expose restrictions → commenters proposed publishing prompts, model traces, responses, and code, treating AI interactions like compiler source.
- The competitive moat may shrink → cheaper fine-tuning and multiple frontier providers weaken lock-in — counterpoint: safeguards may only target industrial distillation.

### LLM perspective

- **View:** Model quality metrics are insufficient when providers can selectively alter behavior; observability should become a procurement requirement.
- **Impact:** Companies developing AI features must classify Claude as a policy-mediated dependency, not a neutral engineering tool.
- **Watch next:** Independent evaluations should probe boundary cases and measure whether restrictions create detectable, reproducible performance shifts.
