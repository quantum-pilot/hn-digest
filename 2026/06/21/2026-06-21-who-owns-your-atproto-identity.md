# Who owns your ATProto identity?

- Score: 160 | [HN](https://news.ycombinator.com/item?id=48619140) | Link: https://kevinak.se/blog/who-actually-owns-your-atproto-identity-hint-its-probably-not-you

- TL;DR  
ATProto’s promise of portable, decentralized identity hides a critical trade-off: most users let their Personal Data Server host both signing and rotation keys, so operators can cryptographically impersonate them or delete identities across every ATProto app, not just Bluesky. The author argues this is worse than traditional platform lock-in and mostly invisible to users. Commenters debate how serious the risk is, compare it to GitHub and DNS, and stress that self-hosting or user-held keys must be easier and more common.

- Comment pulse  
  - Risk is overblown → users already trust hosts like GitHub; bigger threat is account takeover. — counterpoint: GitHub never holds signing keys; ATProto PDS does.  
  - PDS like domain/DNS hosting → someone controls routing to your identity. — counterpoint: DNS operators can’t impersonate you without private keys; PDS operators can.  
  - Portability exists → self-hosting a PDS is cheap Docker-on-RPi work. — counterpoint: Bluesky usually holds DIDs’ keys; moving or self-hosting remains rare and UI-fragile.

- LLM perspective  
  - View: Centralizing signing keys in third-party PDSs recreates platform trust problems that decentralization was meant to reduce.  
  - Impact: High-risk users, maintainers, and orgs should treat ATProto PDS choice like picking a bank or CA, not casual hosting.  
  - Watch next: Client-side key storage, hardware-key support, and default backup rotation keys could shift real control from operators to users.
