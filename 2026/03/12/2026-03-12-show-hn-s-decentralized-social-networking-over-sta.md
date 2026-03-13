# Show HN: s@: decentralized social networking over static sites

- Score: 394 | [HN](https://news.ycombinator.com/item?id=47344548) | Link: http://satproto.org/

## TL;DR

`s@` is a decentralized social protocol where each user is just a static website. Your domain is your identity; posts live as encrypted JSON files on your site, and friends decrypt them in-browser using per-follower keys. There are no servers, relays, or global timelines—only mutual followers see each other, by design. HN readers like the elegance but question real-world usability: heavy crypto, fragile key storage in browser localStorage, and no clear path to mass, dopamine-driven network effects.

---

## Comment pulse

- Crypto-centric UX is too hard for normal users → people won’t manage X25519 keys; server-managed auth feels more realistic for friends/family—counterpoint: cultural shift + helpers may be acceptable.  
- Storing private keys in localStorage is unsafe → clearing browser nukes identity; users will rage-quit—counterpoint: export/download flow and 2FA/crypto-wallet norms partly mitigate.  
- Protocol seems more concept than Facebook rival → lacks built-in incentives and content velocity needed for network effects; best as experiment or niche small-group tool.

---

## LLM perspective

- View: Clever demonstration of “social over plain HTTPS files,” showing how far you can go without any dedicated backend.  
- Impact: Most useful to tinkerers, static-site owners, and protocol designers exploring ATProto/Fediverse-like models with maximal user data ownership.  
- Watch next: Robust key-backup tooling, multi-device support, `.well-known`-based discovery, and optional integration with existing identity providers.
