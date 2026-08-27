# Show HN: uvx ptn, scan a QR, get a terminal in your phone

- Score: 88 | [HN](https://news.ycombinator.com/item?id=46472772) | Link: https://github.com/lyehe/porterminal

### TL;DR

Porterminal exposes a local terminal to a phone through a Cloudflare tunnel: run `uvx ptn`, scan a QR code, and reconnect to persistent, multi-tab shell sessions across Windows, macOS, or Linux. It avoids SSH and port forwarding, offers mobile controls, and supports optional per-session passwords. HN readers liked the convenience for asynchronous coding, but treated link-only authentication as the central risk; alternatives included Tailscale, Headscale, and WireGuard, while the author considered adding single-session URLs.

### Comment pulse

- Link-only access is fragile → anyone seeing the QR or URL gains a shell; a one-use session could narrow exposure.
- Private overlays reduce attack surface → readers favored Tailscale or Headscale, though WireGuard may encounter more blocked networks.
- Mobile terminals fit agent workflows → long-running coding tasks can be checked or corrected away from a desk.

### LLM perspective

- View: One-command access is compelling, but remotely exposed shells need secure defaults rather than optional hardening.
- Impact: Developers gain mobility while accepting Cloudflare availability and bearer-link risk.
- Watch next: Test one-use URLs, mandatory authentication, session revocation, and tunnel-failure recovery.
