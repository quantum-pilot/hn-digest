# That's not how email works

- Score: 218 | [HN](https://news.ycombinator.com/item?id=46799304) | Link: https://danq.me/2026/01/28/hsbc-dont-understand-email/

## TL;DR
HSBC mailed the author a physical letter claiming their emails were “returned undelivered,” even though those emails were arriving fine. Root cause: HSBC uses tracking pixels in statement emails, and when the pixel isn’t loaded—because the user blocks remote images for privacy—they wrongly infer the email failed. Worse, the pixels are served over plain HTTP, leaking metadata on shared networks and enabling possible content injection. The author argues this is both technically incompetent and emblematic of surveillance capitalism, and suggests simpler, privacy‑respecting alternatives.

---

## Comment pulse
- Other banks do this too → NAB, BoA, Citi: block tracking or invalidate email → get snail mail threats or forced paper statements instead.  
- Bank tech is brittle legacy plumbing → HTTP pixels, inconsistent formats, broken UIs persist because nobody wants to touch risky old systems. — counterpoint: some see HTTP risk here as marginal.  
- Organizational dysfunction → leaders demand “prove customers read it,” overvalue open rates, ignore warnings that tracking is unreliable at individual level.

---

## LLM perspective
- View: Treat “email opened” as a coarse campaign metric only; never as a per-customer truth or control-flow trigger.  
- Impact: Banks, insurers, and gov agencies must decouple regulatory communications from marketing-style telemetry and respect image-blocking as normal.  
- Watch next: Email client defaults on remote images, privacy regulation on tracking pixels, and any banking guidance explicitly banning HTTP resources in customer comms.
