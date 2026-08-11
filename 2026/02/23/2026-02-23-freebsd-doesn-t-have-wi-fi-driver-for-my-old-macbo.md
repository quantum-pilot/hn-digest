# FreeBSD doesn't have Wi-Fi driver for my old MacBook. AI build one for me

- Score: 160 | [HN](https://news.ycombinator.com/item?id=47129361) | Link: https://vladimir.varank.in/notes/2026/02/freebsd-brcmfmac/

### TL;DR

After a direct AI-assisted Linux-to-FreeBSD port produced panics and sprawling shims, the author narrowed scope to one Broadcom BCM4350 PCI chip. Agents first derived and cross-checked an 11-chapter specification from Linux’s brcmfmac code, then implemented, tested, documented, and repeatedly debugged a native driver. It now scans and connects on 2.4/5 GHz with WPA/WPA2, but has known issues and is explicitly a study project. HN saw a notable prototype, while disputing claims that general hardware support or production-quality driver engineering is nearly solved.

### Comment pulse

- Specification-first iteration unlocked progress → fresh agents checked behavior against source before implementation.
- The prototype is not production evidence → the author neither wrote nor deeply reviewed its code — counterpoint: working hardware remains meaningful.
- Clean-room licensing is disputed → deriving a specification directly from open-source implementation may resemble license laundering.

### LLM perspective

- **View:** AI amplified project management more than autonomous engineering.
- **Impact:** Skilled operators can explore narrow ports faster, but maintainers inherit validation and licensing burdens.
- **Watch next:** Stress tests, power management, recovery behavior, code review, and upstream acceptance.
