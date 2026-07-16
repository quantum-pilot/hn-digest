# Mysteries of Telegram Data Centers (2022)

- Score: 238 | [HN](https://news.ycombinator.com/item?id=48920475) | Link: https://dev.moe/en/3025

### TL;DR
The article explains how Telegram ties each account to one of five data centers (DC1–DC5), including why DC5 often fails for Chinese users. Assignments are fixed at registration from phone country code; popular bots misclassify DC2 users as DC4 because Telegram’s web CDN shares domains. Accurate methods instead inspect MTProto migration errors or where profile photos/files live. Testing suggests DC2 is used, while DC3 was deprecated and its users silently moved to DC1. HN comments add anecdotes about outages, concerns over FSB involvement in infrastructure, and debate about Telegram’s region‑bound architecture.

---

### Comment pulse
- Telegram infra may be covertly managed by an operator also serving Russia’s FSB → raises trust, privacy, and jurisdiction concerns beyond mere DC placement.  
- Regional users treat specific DCs as memes: Chinese communities complain about unstable DC5; Russian‑speaking tech groups similarly joke about “dc2 down” during outages.  
- Critics call per‑region DC mapping technical debt; defenders say it’s just a tiny country‑code table. — counterpoint: even tiny bespoke rules complicate long‑term maintenance.  

---

### LLM perspective
- Telegram’s opaque DC behavior shows how closed protocols force the community to reverse‑engineer basics like routing and failover.  
- Network‑sensitive users, activists, and regulators gain a clearer mental model for outage patterns and potential jurisdiction or surveillance exposure.  
- Watch for Telegram clarifying DC policies, user‑migration rules, or open‑sourcing more infra details amid growing scrutiny over FSB links.
