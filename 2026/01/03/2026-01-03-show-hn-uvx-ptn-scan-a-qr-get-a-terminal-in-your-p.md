# Show HN: uvx ptn, scan a QR, get a terminal in your phone

- Score: 88 | [HN](https://news.ycombinator.com/item?id=46472772) | Link: https://github.com/lyehe/porterminal

- TL;DR  
  - Porterminal (ptn) is a quick web-based terminal that lets you run a command on your PC, scan a QR code, and control that shell from your phone via a Cloudflare tunnel. It focuses on mobile usability and persistent sessions, avoiding SSH or manual port forwarding. Hacker News discussion is enthusiastic but highlights security concerns around URL-only access, requests stronger auth options, and debates alternatives like Tailscale VPN or Termux+SSH for more traditional remote workflows.

- Comment pulse  
  - Security worries over URL-as-auth; commenters request one-time links and passwords; author notes tunnels are disposable and adds options for single-session and ephemeral passwords.  
  - Networking crowd prefers Tailscale or self-hosted WireGuard/Headscale, citing smaller attack surface and better reliability through firewalls than public tunneling services.  
  - Others say existing Termux+SSH setups are sufficient, but fans praise QR-based, zero-config ‘vibe coding’ from couch, commute, or waiting rooms.

- LLM perspective  
  - View: Novelty is low technically, but packaging tunnel, mobile UI, and persistence behind one command meaningfully lowers friction.  
  - Impact: Most useful for solo developers and tinkerers who need interactive access to home machines from phones without full VPN setup.  
  - Watch next: Worth adding audit logs, rate limiting, and clearer defaults around passwords/one-time URLs, plus benchmarks on latency and Cloudflare tunnel reliability.
