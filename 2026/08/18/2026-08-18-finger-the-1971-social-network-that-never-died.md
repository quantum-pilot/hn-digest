# Finger: the 1971 social network that never died

- Score: 325 | [HN](https://news.ycombinator.com/item?id=49342472) | Link: https://en.andros.dev/blog/54572bc7/finger-the-1971-social-network-that-never-died/

### TL;DR

Finger began at Stanford in 1971 as a human-readable way to see who was logged in, then evolved into network presence and text profiles served from `.plan` and `.project` files. Its protocol is almost irreducibly simple: send a username over TCP port 79 and receive plain text. The article traces famous uses, including John Carmack’s development journal and CMU’s connected soda machine, explains its security-driven decline, and surveys modern hosts, clients, directories, and self-hosting options sustaining a small revival.

### Comment pulse

- Nostalgia centered on Finger’s role within a broader Unix social toolkit and on its unexpectedly permissive early-internet security environment.
- Readers debated whether modern discovery, HTTPS, and privacy layers would improve Finger or simply erase the value of its minimalism.
- Current client builders highlighted the protocol’s missing discovery layer and efforts to make active hosts easier to explore.

### LLM perspective

- View: The strongest historical claim is continuity of a social pattern, not equivalence to modern social networks.
- Impact: Port 79’s simplicity is appealing, but public deployments still require deliberate privacy and daemon hardening.
- Watch next: The revival is intentionally niche; richer discovery creates tension with Finger’s defining restraint.
