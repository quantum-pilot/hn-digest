# Tor browser removing various Firefox AI features

- Score: 324 | [HN](https://news.ycombinator.com/item?id=45605842) | Link: https://blog.torproject.org/new-alpha-release-tor-browser-150a4/

### TL;DR

Tor Browser 15.0a4 removes Firefox AI integrations because the project considers hosted machine-learning systems unauditable for its security and privacy goals and does not want inclusion to imply endorsement. The release candidate also strips additional Firefox branding and services, renames the meek transport, improves themes and CJK rendering, updates security components, delegates web-content WebAssembly restrictions to NoScript, and preserves URL protocols on desktop. Tor asks users to test before a planned stable release, while warning people needing strong anonymity to remain on the stable channel.

### Comment pulse

- Supporters favored excluding AI from browser chrome, particularly for users facing nation-state threats and difficult-to-audit attack surfaces.
- Others found Firefox’s optional sidebar useful for explanations and translation, arguing such functionality belongs in removable extensions.
- Commenters noted the sidebar is off by default or provider-dependent, complicating claims that every integration is equally intrusive.

### LLM perspective

- View: Removing optional convenience features is consistent with Tor’s narrower threat model and reproducibility burden.
- Impact: Each upstream Firefox integration creates continuing audit and rebase work even when disabled by default.
- Watch next: Test that feature removal, NoScript WebAssembly controls, and branding changes preserve anonymity and ordinary site compatibility.
