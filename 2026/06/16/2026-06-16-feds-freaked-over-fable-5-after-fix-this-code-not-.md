# Feds freaked over Fable 5 after 'fix this code', not jailbreak, say researchers

- Score: 536 | [HN](https://news.ycombinator.com/item?id=48552687) | Link: https://www.theregister.com/security/2026/06/15/feds-freaked-over-fable-5-after-simple-fix-this-code-prompt-not-jailbreak-says-researcher/5255827

### TL;DR

Security researcher Katie Moussouris says the evidence behind US export restrictions on Anthropic’s Fable 5 and Mythos 5 was not a sophisticated jailbreak: researchers supplied vulnerable code, requested repairs, then generated tests. The administration’s directive led Anthropic to disable both models globally. Moussouris and more than 100 cybersecurity leaders argue this normal find-fix-test workflow helps defenders and that restrictions spare foreign or open-weight alternatives. HN disputed whether the prompt still bypassed intended controls, while debating Anthropic’s dangerous-model messaging, inherently leaky guardrails, and possible political motives behind the action.

### Comment pulse

- Defensive and offensive outputs overlap → patch tests can reveal exploit components, making intent-based refusal difficult without degrading ordinary security work.

- Anthropic created a messaging trap → calling Mythos exceptionally dangerous made Fable guardrail leaks look unsafe — counterpoint: Fable’s capability advantage was unproven.

- Motive claims remain contested → commenters alleged retaliation or regulatory capture, but the supplied discussion offered speculation rather than evidence resolving those theories.

### LLM perspective

- **View:** Export policy should distinguish demonstrated capability gains from trivial reformulations of routine defensive tasks.

- **Impact:** Broad restrictions may reduce defenders’ access while leaving attackers able to use open models and ordinary development workflows.

- **Watch next:** Release the underlying evaluation methodology, reproduce exploit chaining independently, and publish precise legal criteria for model export controls.
