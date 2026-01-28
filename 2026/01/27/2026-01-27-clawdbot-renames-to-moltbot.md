# Clawdbot Renames to Moltbot

- Score: 140 | [HN](https://news.ycombinator.com/item?id=46783863) | Link: https://github.com/moltbot/moltbot/commit/6d16a658e5ebe6ce15856565a47090d5b9d5dfb6

## TL;DR

Clawdbot has been renamed to Moltbot, with compatibility layers to keep old installs working. Commenters suspect Anthropic quietly pushed for the change to protect its Claude trademark, citing how aggressively trademarks must be enforced. Most of the thread, though, fixates on the project’s security posture: Shodan-visible deployments, agents with full filesystem and network access, and users wiring it to email, chat, and wallets. People report isolating it in VMs/containers, but many foresee a headline-making prompt-injection or supply-chain exploit.

## Comment pulse

- Moltbot instances already show up on Shodan via favicon hashes → exposed VPS deployments plus capabilities make targets, especially when connected to crypto wallets.  
- Anthropic likely pushed for rename to protect the Claude mark → trademark holders must enforce or risk dilution; Kellogg sued “Leggo Egg Roll” food truck.  
- Broad file/network access terrifies users → many run Moltbot in VMs/containers and restrict credentials—counterpoint: others think model alignment limits damage but seek reproducible exploit examples.

## LLM perspective

- View: Rename is minor; the real story is normalization of running semi-autonomous agents with root-like powers on personal data.  
- Impact: Non-expert users, small startups, and crypto-heavy setups face disproportionate risk; security professionals gain demand for hardening and incident response.  
- Watch next: concrete mitigations like default sandboxing, capability-based tooling, skill-store vetting, plus the first large-scale prompt-injection or skill-supply-chain breach.
