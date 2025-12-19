# We pwned X, Vercel, Cursor, and Discord through a supply-chain attack

- Score: 508 | [HN](https://news.ycombinator.com/item?id=46317098) | Link: https://gist.github.com/hackermondev/5e2cdc32849405fff6b46957747a2d28

### TL;DR
A 16‑year‑old security researcher found a critical XSS in Mintlify, an AI docs SaaS used by Discord, X, Vercel, Cursor and others. Mintlify exposed internal endpoints that let any customer domain serve arbitrary static files from any other Mintlify project. By uploading an SVG with embedded JavaScript and loading it via a customer’s main domain, the attacker could run code as that site, enabling account takeover and API misuse. Discord rolled back Mintlify; total bounties were about $11k, which many see as underpaying for a severe supply‑chain risk.

---

### Comment pulse
- Impact is huge → one crafted SVG URL on a trusted domain could hijack sessions, apps, and payments; many feel $4k from Discord is insultingly low.  
- SVG scripting is a design landmine → many platforms now block or sanitize SVGs, or server‑render them; missing sanitization likely means you’re exposed.  
- Broader indictment of modern stacks → “vibe‑coded” AI/JS products, single‑domain fronting, and cheap bug bounties create systemic risk—counterpoint: XSS often has limited black‑market value.

---

### LLM perspective
- View: This is classic multi‑tenant SaaS isolation failure plus underrated SVG semantics, not something uniquely “AI‑era,” just amplified by reuse.  
- Impact: Any company embedding third‑party apps on primary domains should assume they share an origin and model threats accordingly.  
- Watch next: Expect more scrutiny of docs/SaaS vendors, stricter domain isolation, mandatory SVG sanitization, and better disclosed internal routing contracts.
