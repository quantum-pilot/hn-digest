# We need a federation of forges

- Score: 507 | [HN](https://news.ycombinator.com/item?id=47948603) | Link: https://blog.tangled.org/federation/

### TL;DR
- Tangled argues that while git is decentralized, collaboration has re-centralized onto GitHub-like forges, creating a fragile monoculture. It proposes “knots” (git servers) whose issues, PRs and social activity federate via the AT Protocol, letting you self-host code yet interact across servers as if on one site. HN likes the technical elegance and early UX, but debates Mastodon-style governance pitfalls, VC funding and whether richer, self-contained VCS (e.g., Fossil) might be a better direction.

### Comment pulse
- Mastodon repeat? → Skeptics expect defederation drama and low signal; others explain ATProto’s PDS/AppView model avoids “instances” and enables global discovery instead.  
- Hands-on users → Tangled already replaces GitHub for some: familiar social graph, unified login, static hosting, Nix-based CI, and separable self-hosted git “knots”.  
- Sustainability and alternatives → VC backing prompts rug-pull fears; some prefer co-ops or richer offline-first VCS like Fossil over adding another federated layer.  

### LLM perspective
- View: Federated forges over ATProto trade Mastodon-style fragmentation for shared data layer, but depend on AT/Bluesky ecosystem maturing.  
- Impact: Most relevant to OSS maintainers worried about GitHub lock-in, self-hosters, and tool builders leveraging open social graphs.  
- Watch next: Track Tangled's self-hosting docs, export/migration tools, governance/monetization plans, and interop with ForgeFed or richer-repo systems like Fossil.
