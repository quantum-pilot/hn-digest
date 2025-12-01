# "Boobs check" – Technique to verify if sites behind CDN are hosted in Iran

- Score: 155 | [HN](https://news.ycombinator.com/item?id=46100323) | Link: https://twitter.com/hkashfi/status/1995109785679573167

- TL;DR  
“Boobs check” is a network trick for guessing whether a site hidden behind a CDN is actually hosted inside Iran. It relies on Iran’s filtering infrastructure inspecting unencrypted origin traffic and treating requests containing banned keywords differently when they leave the National Information Network. If a CDN talks to its origin over plain HTTP (e.g., Cloudflare Flexible), URL paths leak, enabling this side‑channel; properly configured TLS breaks it. HN discussion focuses on Cloudflare’s weak defaults, Iranian TLS interception, and sanction‑driven interest in location.  
*Content unavailable; summarizing from title/comments.*

- Comment pulse  
  - Technique works only when CDN terminates TLS and forwards to origin over HTTP, letting Iranian proxies read URLs; end‑to‑end TLS or custom cert defeats it.  
  - Iran’s National Information Network terminates TLS via state CA or HTTP, enabling inspection; commenters call Cloudflare an “encryption remover” — counterpoint: careful setups avoid this.  
  - Motivations include avoiding sanctioned business ties, flagging propaganda outlets, and supporting protests; some doubt the need for such geolocation beyond niche compliance or activism.

- LLM perspective  
  - View: Technique illustrates how censorship infrastructure and sloppy CDN TLS settings create unintended side‑channels that leak server geography.  
  - Impact: Impacts Iranian hosts, CDNs, compliance teams, and activists who rely on location knowledge for sanctions, boycotts, or information‑control analysis.  
  - Watch next: Watch for CDNs deprecating insecure “flexible” HTTPS modes and for more rigorous audits of state‑level TLS interception practices.
