# Speed up responses with fast mode

- Score: 98 | [HN](https://news.ycombinator.com/item?id=46926043) | Link: https://code.claude.com/docs/en/fast-mode

## TL;DR
Anthropic’s new “fast mode” for Claude Code runs the same Opus 4.6 model with a different API config that prioritizes latency over cost. It’s toggled with `/fast`, persists across sessions, and is ideal for interactive coding and debugging, not batch jobs. Pricing is significantly higher per token, always billed as extra usage and separate from subscription quotas, with distinct rate limits and automatic fallback to standard speed. HN discussion focuses on pricing, value vs competitors, and missing “slow/cheap” tiers.

## Comment pulse
- Fast mode is great, but a “slow mode” using spot/idle GPUs could cut costs for non-urgent jobs → better price discrimination — counterpoint: CPUs can already handle some slow work.
- Pricing feels like upselling urgent users; people will pay big premiums for faster tokens, and rivals will copy this monetization pattern quickly.
- Value questioned: modest speedup at much higher price vs alternatives like Gemini Pro; segmentation into “background vs human-in-loop” use is logical, but billing fairness is debatable.

## LLM perspective
- View: This formalizes QoS tiers for LLMs; latency becomes an explicit, billable dimension alongside context and quality.
- Impact: Teams must model human time vs token cost, budgeting separately for “interactive” vs “batch” usage.
- Watch next: Competitors’ speed tiers, true low-cost “slow modes,” and standardized, third-party latency/price benchmarks across providers.
