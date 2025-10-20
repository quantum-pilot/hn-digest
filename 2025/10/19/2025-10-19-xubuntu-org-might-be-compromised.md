# Xubuntu.org Might Be Compromised

- Score: 305 | [HN](https://news.ycombinator.com/item?id=45634367) | Link: https://old.reddit.com/r/Ubuntu/comments/1oa4549/xubuntuorg_might_be_compromised/

- TL;DR
    - Xubuntu.org’s downloads page appears compromised: the torrent link served a ZIP with a Windows EXE that “clips” clipboard crypto addresses to attacker wallets. Maintainers disabled downloads and called it a hosting “slip‑up,” which users criticized as minimizing risk. Official ISOs from mirrors and signed SHA256SUMS still validate; the issue seems limited to the torrent link. Discussion centers on verification practices (HTTPS vs checksums vs GPG), on-chain tracing of attacker wallets, typosquatted distro sites, and ideas for centralized trust validation.
    - Content unavailable; summarizing from title/comments.

- Comment pulse
    - Torrent link served a ZIP with a Windows EXE that swaps clipboard crypto addresses to attacker wallets → classic clipper malware targeting Bitcoin, Ethereum, etc.
    - Checksums alone aren’t protection if site is compromised → verify GPG-signed hashes and keys from independent sources — counterpoint: HTTPS already prevents in-transit tampering.
    - Maintainers disabled downloads and called it a hosting “slip‑up” → community perceives minimization; wants clear incident report, scope (torrent-only?), and rotation of credentials.

- LLM perspective
    - View: Treat distro sites as supply-chain targets; prefer direct mirrors, avoid torrent links until clarified; verify signatures with known keys.
    - Impact: Users moving to signed checks and key verification; projects tightening hosting, CI/CD, and release workflows; browser clipboard permissions scrutinized.
    - Watch next: Incident postmortem, asset list, key rotation; blacklist attacker wallets; demote typosquats; audit mirrors; re-enable torrents only with verified .torrent files.
