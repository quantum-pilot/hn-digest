# Trick users and bypass warnings – Modern SVG Clickjacking attacks

- Score: 320 | [HN](https://news.ycombinator.com/item?id=46155085) | Link: https://lyra.horse/blog/2025/12/svg-clickjacking/

## TL;DR

The post introduces “SVG clickjacking”: abusing SVG filter effects applied to iframes (or any rendered page) to *read* pixels and run arbitrary logic entirely inside the rendering pipeline. By chaining `feTile`, `feComposite`, `feBlend`, `feColorMatrix`, etc., the attacker can detect UI states, build logic gates, and overlay highly convincing fake UI that tracks the real one—enabling multi‑step clickjacking and data exfiltration, including generating QR codes encoding stolen data. HN discussion centers on HTML/CSS complexity, mitigations (X‑Frame‑Options, CSP), and whether SVG/CSS are “too powerful.”

---

## Comment pulse

- HTML/CSS feels bewilderingly complex → labels toggle checkboxes, CSS `:has()` reacts to state, SVG filters chain visually. — counterpoint: most of this dates back decades, not “modern bloat.”

- Just set `X-Frame-Options` / `frame-ancestors` and be done → framing is required for apps like Docs; technique also works on non‑iframe targets under strict CSP.

- “Disable SVG/CSS for security” → some see them as overpowered attack surfaces. — counterpoint: practical exploitation is rare; iframes and misconfig, not CSS itself, are core risk.

---

## LLM perspective

- View: This weaponizes the graphics stack as a logic engine, bypassing usual script-centric mental models of web security.

- Impact: Browser vendors, large webapps with embedded UIs, and CSP/XFO best‑practice guides need to reassess assumptions about “safe” rendering.

- Watch next: Proposals to limit filters on cross-origin content, security reviews of SVG/CSS features, and tools that flag risky filter/iframe combinations.
