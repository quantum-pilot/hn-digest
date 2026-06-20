# There are no instances in ATProto

- Score: 319 | [HN](https://news.ycombinator.com/item?id=48599515) | Link: https://overreacted.io/there-are-no-instances-in-atproto/

### TL;DR
Abramov explains that ATProto (used by Bluesky) doesn’t have “instances” like Mastodon. In Mastodon, each instance tightly couples hosting, identity, and app, then federates with others; your username and data effectively live inside one fiefdom. ATProto instead separates hosting from apps, like blogs + RSS readers: you can move your data to another host and use many different clients, all aggregating from the same “atmosphere” of user data. HN debates whether this analogy, tone, and real-world centralization gloss over moderation and relay/AppView dependencies.

---

### Comment pulse
- Critique: “no instances” is a semantic dodge → downplays ActivityPub’s tradeoffs, relays, and migrations; tone comes off as Mastodon-hostile and needlessly divisive.  
- Defense: post usefully reframes “instance-brain” → many people wrongly equate decentralization with counting servers instead of separating hosting, identity, and apps.  
- Practical worry: ATProto is decentralized on paper but centralized in practice → Bluesky runs main app + hosting; moderation and powerful relays risk recreating oligopolies.

---

### LLM perspective
- View: The key idea is architectural: user identity lives at portable data hosts; apps become interchangeable views, not sovereign silos.  
- Impact: If adopted, this favors small hosts, experimental clients, and independent moderation services over monolithic “one-site-rules-all” platforms.  
- Watch next: Growth of non-Bluesky hosts/appviews, real-world host switching, and whether independent moderation lists and relays stay cheap and plural.
