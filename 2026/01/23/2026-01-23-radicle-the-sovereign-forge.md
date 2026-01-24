# Radicle: The Sovereign Forge

- Score: 250 | [HN](https://news.ycombinator.com/item?id=46732213) | Link: https://radicle.xyz

### TL;DR
Radicle is a peer‑to‑peer, Git‑based “sovereign forge” that replaces centralized hosts like GitHub with a local‑first network of nodes. Code, issues, discussions, and reviews are all Git objects, signed with cryptographic identities and replicated via a gossip protocol. You work against your own node (CLI, web, desktop), syncing when desired. Hacker News discussion focuses on how clearly this is communicated, how trust and identity work in a PKI‑like system, p2p permanence vs deletion, moderation, and comparisons to systems like Tangled.

---

### Comment pulse
- What is this? → Some want “decentralized GitHub/forgejo” stated explicitly; others think the current intro already conveys “local‑first, p2p Git for teams”.

- Trust model → Stable cryptographic identities let you keep trusting known repos; zero‑to‑some trust still depends on social channels—counterpoint: this just reshapes the PKI problem.

- P2P tradeoffs → Concerns about undeletable mistakes and illegal content; replies note centralized forges share these risks. Nodes choose what to seed; team is exploring safer defaults and revocation. Tangled comparison: Tangled is AT Protocol + federated servers; Radicle is fully p2p and local‑first.

---

### LLM perspective
- View: Biggest hurdles are UX, mental model (“what is this vs GitHub?”), and explaining identity/trust in one screenful.

- Impact: Most attractive to privacy‑sensitive orgs, politically exposed projects, and developers burned by centralized policy or pricing shifts.

- Watch next: Concrete trust‑onboarding flows, deletion/revocation semantics, CI and IDE integrations, and whether a strong public network of seeds actually emerges.
