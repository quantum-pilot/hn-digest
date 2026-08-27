# Trick users and bypass warnings – Modern SVG Clickjacking attacks

- Score: 320 | [HN](https://news.ycombinator.com/item?id=46155085) | Link: https://lyra.horse/blog/2025/12/svg-clickjacking/

### TL;DR

The researcher shows how SVG filters applied to cross-origin frames can inspect selected pixels, compose logic gates, and alter displayed output without extracting raw pixel data into JavaScript. That enables interactive, multi-step clickjacking interfaces that react to a target's state, hide real prompts, and solicit user actions. A Google Docs demonstration earned a $3,133.70 bounty. A rough Chromium-only proof of concept even encodes observed data into a QR code for user-assisted exfiltration, although scaling, color profiles, framing protections, and user cooperation constrain attacks.

### Comment pulse

- Discussion disputed whether iframe controls solve the problem, noting some applications require framing and injection scenarios may differ.
- Commenters admired the SVG adder while debating whether disabling SVG or CSS would be proportionate.

### LLM perspective

- View: The novelty is state-aware visual computation, which makes long clickjacking sequences more convincing.
- Impact: Browser defenses must consider rendered pixels as attacker-controlled signals, not merely passive presentation.
- Watch next: Vendor mitigations that preserve legitimate SVG filters and framing without exposing cross-origin state.
