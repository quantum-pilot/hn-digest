# Elevated errors on Claude.ai, API, Claude Code

- Score: 241 | [HN](https://news.ycombinator.com/item?id=47779730) | Link: https://claudestatus.com/

## TL;DR
An unofficial community status dashboard shows frequent incidents across Claude.ai, the API, Claude Code, and specific models (notably Sonnet/Opus 4.6) through April 2026, mostly around login/auth and elevated error rates, with ~92–94% 30‑day uptime. The live feed lists repeated outages and auth failures while the official status reports short, resolved “elevated errors” episodes. Hacker News users report daily 500s at US–EU overlap hours, complain about account/billing/support chaos and brittle tooling, and float surge pricing and model fallbacks to tame peak-load failures.

## Comment pulse
- Peak 500s recur daily near 14:30–16:00 UTC → overlapping US/EU demand overloads Claude Code — counterpoint: explicit errors beat silent quality degradation.  
- Core models impress, everything around them feels broken → confusing accounts, billing issues, blocked org moves, flaky desktop wrapper, MCP auth limits, and nonresponsive support.  
- Users propose surge pricing and tier tweaks → throttle peak usage, favor cheaper models, and possibly auto-fallback to partner LLMs instead of outright outages.  

## LLM perspective
- View: Anthropic’s rapid feature rollout outpaces reliability engineering; authentication and capacity planning are recurring single points of failure.  
- Impact: Toolchains built on Claude Code inherit brownouts, forcing teams to add fallbacks or pause workflows during predictable peak windows.  
- Watch next: formal SLAs, revised pricing tiers, clearer capacity limits, and whether Anthropic offers multi-model redundancy or regional routing guarantees.
