# Apple is about to make Hide My Email useless

- Score: 357 | [HN](https://news.ycombinator.com/item?id=48559935) | Link: https://arseniyshestakov.com/2026/06/16/apple-is-about-to-make-hide-my-email-useless/

- TL;DR  
    - Apple will move all Sign in with Apple and iCloud+ Hide My Email addresses onto @private.icloud.com, separating them from normal @icloud.com inboxes. That makes it trivial for sites to block Apple’s relay domain without impacting ordinary iCloud mail, weakening plausible deniability and making Hide My Email resemble disposable-address services. The author urges users to pre-generate @icloud.com aliases while possible. HN debates how harmful this is and shares DIY aliasing strategies using custom domains, catch‑alls, and forwarding services.

- Comment pulse  
    - Concern: change degrades hassle‑free privacy → services can blanket‑block @private.icloud.com, forcing users to pre‑mint aliases or run custom-domain relays—counterpoint: only sketchy sites will bother.  
    - Practical limits: sometimes you must use hostile apps (parking, telcos); blocking your relay means no service access despite privacy‑preserving intent.  
    - Alternatives: own domain + catch‑all or SimpleLogin‑style services give per‑site aliases, but add admin overhead, SPF/DMARC complications, weaker anonymity, and account‑recovery hassles.

- LLM perspective  
    - View: Centralizing relays on a distinct domain simplifies anti‑abuse for sites but predictably invites crude blocking that harms privacy‑minded users.  
    - Impact: Heavy Hide My Email users, journalists, activists lose plausible deniability; casual users may notice only when important services reject them.  
    - Watch next: Track which major platforms block @private.icloud.com and whether Apple offers enterprise‑friendly alternatives or policy nudges discouraging blanket bans.
