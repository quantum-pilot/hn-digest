# SSH certificates: the better SSH experience

- Score: 206 | [HN](https://news.ycombinator.com/item?id=47624811) | Link: https://jpmens.net/2026/04/03/ssh-certificates-the-better-ssh-experience/

### TL;DR
SSH normally relies on “trust on first use” (TOFU): you accept an unknown host key once, then hope it never changes, while manually sprinkling public keys into `authorized_keys`. This works for a few machines but scales poorly, breaks on host key rotation, and encourages bad habits (“just type yes”). The post shows how to set up an SSH certificate authority with OpenSSH: sign user and host keys, trust one CA on clients/servers, get short‑lived, policy‑rich certificates, no TOFU prompts, and centralized control. HN commenters mostly agree certs shine at scale but debate whether their complexity is justified for small setups where disciplined TOFU and static keys may suffice.

---

### Comment pulse
- TOFU is fine for a few stable hosts → you can out‑of‑band verify once and never rotate keys — counterpoint: in practice people YOLO “yes” and never verify.
- SSH certs are powerful but underused → folks repeatedly “rediscover” them; many even conflate plain keys with certificates and don’t realize time‑limited, role‑bound access exists.
- Organizations struggle more with TLS interception boxes than SSH → middleboxes like Zscaler/Umbrella break tooling and trust; at least SSH certs avoid X.509 complexity and CA sprawl.

---

### LLM perspective
- View: SSH certificates are low‑hanging fruit for serious infrastructures; most complexity is front‑loaded and automatable.
- Impact: Centralized SSH CA reduces lateral movement risk, key sprawl, and manual cleanup, while improving auditability and user experience.
- Watch next: Wider client support, opinionated tooling, and integration with SSO/OIDC to issue short‑lived SSH certs on login.
