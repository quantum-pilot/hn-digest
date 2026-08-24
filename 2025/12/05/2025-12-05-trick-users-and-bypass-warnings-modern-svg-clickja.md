# Trick users and bypass warnings – Modern SVG Clickjacking attacks

- Score: 320 | [HN](https://news.ycombinator.com/item?id=46155085) | Link: https://lyra.horse/blog/2025/12/svg-clickjacking/

### TL;DR

SVG filters can visually transform cross-origin frames, sample their pixels internally and combine those signals into logic, enabling adaptive clickjacking far beyond a hidden button. The researcher demonstrates disguising sensitive text as a CAPTCHA, hiding validation messages, detecting interface state and guiding victims through multi-step interactions. A Google Docs proof earned a $3,133.70 bounty. Filters cannot directly export sampled data, but can render a QR code encoding it for a user to scan. Attacks still require framing or suitable injection, precise visuals and user participation.

### Comment pulse

- Some readers blamed overpowered CSS and SVG — counterpoint: many primitives are decades old, and the issue is cross-origin rendering or framing policy.
- X-Frame-Options blocks many cases, but applications needing embedding remain exposed; strict CSP with HTML injection can also leave a path.
- Readers admired the SVG adder while noting functional completeness lacks the storage and random access required to establish Turing completeness.

### LLM perspective

- View: This converts browser rendering into a constrained decision engine, making human-mediated data leakage and long interaction chains practical.
- Impact: Framable applications must treat visual filtering as active cross-origin capability, not harmless presentation.
- Watch next: Browser mitigations, Google’s patch details, frame-ancestor deployment and reliable detection under scaling, color profiles and accessibility settings.
