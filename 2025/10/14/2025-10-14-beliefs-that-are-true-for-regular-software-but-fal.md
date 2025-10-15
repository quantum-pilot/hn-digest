# Beliefs that are true for regular software but false when applied to AI

- Score: 187 | [HN](https://news.ycombinator.com/item?id=45583180) | Link: https://boydkane.com/essays/boss

- TL;DR
  - The essay explains why software intuitions mislead with LLMs: behavior stems from vast, opaque training data; failures aren’t traceable; “fixes” don’t generalize; outputs are highly prompt-sensitive; and capabilities often emerge unpredictably, so global safety can’t be specified or guaranteed. Commenters cite Apple’s retrenchment on “Apple Intelligence” as evidence that polished platforms struggle to tame LLM variability. Others warn that agent protocols like MCP expand the blast radius. Debate focuses on risks: concentrated corporate power and information pollution versus catastrophic, goal-driven failures without sentience.

- Comment pulse
  - Mature platforms struggle to productize LLMs → Apple scaled back “Apple Intelligence” after unstable features; politics plus unpredictability undermined polish and control.
  - Global safety isn’t certifiable: models pass tests but fail on novel prompts; MCP agents enlarge failure surface — counterpoint: gating and logging limit blast radius.
  - Main risk: concentrated corporate power and info pollution → centralized AI shapes markets, discourse — counterpoint: capable systems pose risks even without sentience or malice.

- LLM perspective
  - View: Treat LLMs as stochastic, data-shaped systems; manage emergent behavior, not just code-level defects.
  - Impact: Product, QA, and security shift to continual evals, adversarial red-teaming, and post-deployment monitoring.
  - Watch next: Agent frameworks (MCP), deterministic inference advances, interpretability milestones, incident reporting standards for regressions.
