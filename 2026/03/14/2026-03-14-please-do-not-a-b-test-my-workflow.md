# Please do not A/B test my workflow

- Score: 155 | [HN](https://news.ycombinator.com/item?id=47375682) | Link: https://backnotprop.com/blog/do-not-ab-test-my-workflow/

### TL;DR

A Claude Code user found plan mode suddenly returning context-free bullet lists because an Anthropic A/B test imposed a 40-line ceiling and discouraged prose. Paying $200 monthly for a professional tool, the author argues that core behavior should not change invisibly and asks for transparency, configurability, and opt-out controls. The responsible engineer said the experiment tested whether shorter plans reduced rate-limit hits with newer models; early results showed little benefit, so it ended. HN accepted experimentation’s value but saw undeclared workflow changes as destructive to reproducibility and trust.

### Comment pulse

- Test design matters more than testing itself → aggressive variants altered planning quality without giving professionals consent or recovery controls.
- Optimize exploration, not plan prose → commenters blamed unconditional multi-agent fan-out and repeated warm-context reading for greater token waste.
- Open source improves inspectability → counterpoint: it can still ship surprising behavior and lacks proprietary products’ large-scale experimentation data.

### LLM perspective

- **View:** Professional AI tools need behavior versioning because model nondeterminism already makes regressions difficult to diagnose.
- **Impact:** Users lose time and confidence; vendors need experiment disclosure, rollback switches, and stable channels.
- **Watch next:** Opt-out controls, experiment logs, plan-mode telemetry, and separate cost measurements for exploration versus final plans.
