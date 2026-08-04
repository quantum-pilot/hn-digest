# Fable 5 Is Back

- Score: 291 | [HN](https://news.ycombinator.com/item?id=48752030) | Link: https://twitter.com/claudeai/status/2072402636813607381

### TL;DR

Anthropic temporarily restored Fable 5 to paid plans with included usage through July 7, capped at 50% of each weekly allowance; users can then switch models or continue through paid credits. HN reaction was wary rather than celebratory. Several users reported broad safety refusals on book manuscripts, credential entry, and security work, arguing that unreliable intervention undermines the model’s long-horizon value. Others questioned quota economics and proposed reserving Fable for planning and orchestration, then delegating implementation to cheaper older models, while debate continued over model-weight security.

### Comment pulse

- Safety tuning may erase utility → users described benign work being flagged and routine browser credentials refused.
- Planning may maximize scarce quota → use Fable for architecture, tests, and orchestration, then fan out implementation to cheaper models.
- Weight leakage risk is disputed → widespread deployment invites exfiltration — counterpoint: encrypted TEEs or sharded architectures may prevent full-weight access.

### LLM perspective

- **View:** A premium agent model is dependable only when capability, refusal behavior, and access duration are jointly predictable.
- **Impact:** Users must design workflows around quota cliffs and safety interruptions, reducing autonomous value.
- **Watch next:** Measure benign refusal rates, recovery after intervention, and planning quality per consumed token.
