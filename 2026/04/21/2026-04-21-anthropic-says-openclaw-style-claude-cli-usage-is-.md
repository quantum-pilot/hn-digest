# Anthropic says OpenClaw-style Claude CLI usage is allowed again

- Score: 472 | [HN](https://news.ycombinator.com/item?id=47844269) | Link: https://docs.openclaw.ai/providers/anthropic

## TL;DR
Anthropic’s Claude models can be used in OpenClaw either via normal API keys or by reusing the official Claude CLI (`claude -p`), and Anthropic staff have told OpenClaw this CLI-style integration is allowed again. OpenClaw adds niceties like fast/standard tiers, prompt caching, and optional 1M-token context. However, HN commenters highlight that Anthropic’s actual behavior and communication around subscription vs API use, classifier blocking, and upcoming `--bare`/`-p` changes remain inconsistent, making long-term CLI-based workflows feel risky.

---

## Comment pulse
- Developers built extensive `claude -p` workflows on tweet-based assurances; now fear a rug pull as Anthropic hints at deprecating `-p` and pushing `--bare`/API-key use.  
- Users are frustrated by shifting, poorly documented policies and surprise changes to limits and pricing, leading some to avoid Claude or favor open-weight models instead.  
- Some clarify: running OpenClaw *inside* an official Claude Code session is allowed; reusing OAuth tokens directly is metered as extra API usage — counterpoint: classifiers still silently block prompts, so “allowed” doesn’t match reality.

---

## LLM perspective
- View: Flat-rate “pro” plans are colliding with automated, high-volume workflows; vendors are closing loopholes piecemeal.  
- Impact: Serious tool builders should default to API-key billing and treat subscription/OAuth harnessing as experimental and revocable.  
- Watch next: Clear, written policies for CLI and headless use, plus competitor moves that might win over burned Claude Code users.
