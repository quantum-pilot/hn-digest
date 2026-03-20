# macOS 26 breaks custom DNS settings including .internal

- Score: 309 | [HN](https://news.ycombinator.com/item?id=47440759) | Link: https://gist.github.com/adamamyl/81b78eced40feae50eae7c4f3bec1f5a

## TL;DR
macOS 26.3.1 appears to silently break a long‑standing feature where files under `/etc/resolver/` route specific domains (like `*.test` or `*.internal`) to a custom DNS server (e.g., local dnsmasq). On this release, mDNSResponder hijacks all non–IANA-root TLDs and answers via multicast DNS with “no such record,” never consulting the configured unicast nameserver, despite `scutil --dns` showing the resolver as active. This kills many local‑dev and private‑network DNS setups; the only robust workaround is editing `/etc/hosts`. HN discussion spans broader macOS 26 regressions, debates about Apple’s stability philosophy, alternatives like `*.localhost`, and distrust of LLM‑authored bug reports when factual slips appear.

---

## Comment pulse
- macOS papercuts → Users report macOS 26 as unusually breaking (DNS, brightness/XDR, mic indicator, removed APIs), pushing some toward Linux or containers—counterpoint: every OS has comparable regressions.
- Trust and LLMs → Commenters object to AI‑written bug reports, arguing undisclosed LLM use erodes credibility and forces reviewers to re‑validate every technical claim.
- Workarounds and alternatives → Suggestions include using `*.localhost` for browser‑only dev, `scutil`-based DNS config, or abandoning `/etc/resolver` entirely in favor of dedicated DNS servers.

---

## LLM perspective
- View: This change effectively deprecates a documented feature without notice, and conflicts with RFC guidance for special-use domains like `.test`.
- Impact: Local dev tooling, VPNs, and indie macOS utilities relying on custom TLDs face breakage, workarounds, or product degradation.
- Watch next: Whether Apple documents this, ships a 26.x fix, or offers a new sanctioned mechanism for private TLD resolution.
