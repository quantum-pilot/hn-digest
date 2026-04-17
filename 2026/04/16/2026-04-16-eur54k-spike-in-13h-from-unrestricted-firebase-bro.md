# €54k spike in 13h from unrestricted Firebase browser key accessing Gemini APIs

- Score: 375 | [HN](https://news.ycombinator.com/item?id=47791871) | Link: https://discuss.ai.google.dev/t/unexpected-54k-billing-spike-in-13-hours-firebase-browser-key-without-api-restrictions-used-for-gemini-requests/140262

## TL;DR
A Firebase app added a small Gemini feature using a browser API key with no restrictions. Within 13 hours, automated abuse ran up over €54k of Gemini API charges before alerts landed; Google support called the usage “valid” and declined adjustment. A Google PM replied outlining new spend caps, prepaid billing, leak detection, and plans to disable unrestricted keys. Hacker News focused less on the specific bug and more on systemic cloud-billing traps, weak safeguards, and trust in AI platforms.

---

## Comment pulse
- Lack of true hard caps → developers can be hit with life‑altering surprise bills; alerts are delayed and budgets are not enforced — counterpoint: real‑time caps are technically hard at hyperscale.  
- Similar horror stories → budget alerts arrive hours late even with “best practice” kill switches; platforms resist features that cut revenue and shift all risk to customers.  
- Gemini keys as secrets → years of “API keys aren’t secrets” messaging plus many leaked keys on GitHub; LLM billing makes this confusion extremely expensive and feels like a deliberate anti‑feature.

---

## LLM perspective
- View: Treat AI API keys as production credentials; never ship them to browsers, demos, or talks without strict scoping and rotation.  
- Impact: Small teams and hobbyists are disproportionately exposed; they lack legal leverage and ops tooling to absorb billing shocks.  
- Watch next: Whether clouds add real, instant hard caps and fraud write‑off policies for AI usage, or keep relying on DIY safeguards and PR damage control.
