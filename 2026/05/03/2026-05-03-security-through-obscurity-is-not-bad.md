# Security through obscurity is not bad

- Score: 109 | [HN](https://news.ycombinator.com/item?id=47997486) | Link: https://mobeigi.com/blog/security/security-through-obscurity-is-not-bad/

### TL;DR
The article argues that “security through obscurity is bad” is an oversimplified mantra: relying *only* on obscurity is dangerous, but using it as one layer in defense‑in‑depth is valuable. Examples include non‑default WordPress table prefixes thwarting mass SQL‑injection bots, stripped debug symbols slowing CS:GO cheat development, and heavy JavaScript obfuscation in reCAPTCHA, Netflix DRM, and Riot Vanguard. AI and tools can pierce obscurity, but the author’s own $300 LLM CTF experiment shows that making attacks slower and costlier is still a practical deterrent.

---

### Comment pulse
- Obscurity as concealment → Useful like camouflage alongside real “cover” (robust controls), but fails quickly against well‑resourced or automated adversaries.
- Cost vs payload → Best “security” is collecting less sensitive data; then even a successful breach yields little—counterpoint: operational needs often push in the opposite direction.
- Risk of overconfidence → Obscurity can hide design flaws, mislead teams into thinking they’re safe, and add complexity; must be clearly labeled as a minor, brittle layer.

---

### LLM perspective
- View: Treat obscurity as friction engineering: raise marginal attack cost without counting it as a primary control or assurance mechanism.
- Impact: Most value is against commodity botnets and spray‑and‑pray scanners, not focused nation‑states or insider threats.
- Watch next: Quantified studies of AI‑assisted de‑obfuscation costs vs typical bug‑bounty payouts or ransomware returns.
