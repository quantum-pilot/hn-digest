# Anthropic takes legal action against OpenCode

- Score: 355 | [HN](https://news.ycombinator.com/item?id=47444748) | Link: https://github.com/anomalyco/opencode/pull/18186

### TL;DR
Anthropic asked the OpenCode project to remove all first‑party Claude Code integration, including bundled plugins and OAuth flows that let users pipe their cheap Claude Code subscriptions into a competing editor. OpenCode complied via a PR that deletes Anthropic-specific prompts, headers, UI hints, and the built‑in auth plugin, while still allowing use of Anthropic’s normal paid API like any other provider. HN discussion frames this as Anthropic enforcing ToS on a loss‑leader “all‑you‑can‑eat” plan versus hostility toward open tools and users.

---

### Comment pulse
- Side‑loading Claude Code into OpenCode violated explicit ToS → subscriptions are discounted for Anthropic’s own harness; third parties are supposed to use the per‑token API instead.  
- Critics: Anthropic nukes goodwill for PR loss, driven by subsidy pressure, telemetry/control, and fear of model distillation — counterpoint: this is standard “loss‑leader must stay first‑party” economics.  
- Debate on openness: some see no open‑source angle, just licensing and trademarks; others cite Dario’s anti‑open‑weights stance as evidence of a closed, moat‑protection strategy.

---

### LLM perspective
- View: This is classic product segmentation enforcement; the surprising part is how visible it is to developers.  
- Impact: Third‑party devtools lose “cheap Claude via subscription” hacks; heavy users face higher costs or migrate models.  
- Watch next: Whether Anthropic offers sanctioned partner integrations, adjusts pricing, or pursues similar actions against other unofficial harnesses.
