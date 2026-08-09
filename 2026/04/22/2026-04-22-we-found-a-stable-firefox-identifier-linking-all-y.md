# We found a stable Firefox identifier linking all your private Tor identities

- Score: 346 | [HN](https://news.ycombinator.com/item?id=47866697) | Link: https://fingerprint.com/blog/firefox-tor-indexeddb-privacy-vulnerability/

### TL;DR

Researchers found that Firefox Private Browsing and Tor Browser exposed a process-lifetime fingerprint through the unsorted order returned by `indexedDB.databases()`. Private database names were mapped to UUIDs in a global, cross-origin hash table; deterministic bucket iteration let unrelated sites creating the same names observe the same permutation, surviving closed private windows and Tor’s New Identity until full restart. Sixteen names offer 44 theoretical bits. Mozilla fixed CVE-2026-6770 in Firefox 150 and ESR 140.10. Hacker News recommended full Tor restarts and debated why benign browser capabilities become permissionless fingerprints.

### Comment pulse

- Site isolation did not prevent the leak because IndexedDB’s global bookkeeping sat outside the relevant per-origin boundary.
- A fingerprinting vendor disclosed the bug despite commercial incentives — counterpoint: the company says its products never exploit vulnerabilities.
- Prompting for every fingerprintable property could curb access but overwhelm users and disrupt ordinary layout, media, language, and storage features.

### LLM perspective

- **View:** Canonicalization is a privacy primitive: APIs should not expose internal order when order carries no intended meaning.
- **Impact:** Updated Firefox users regain isolation; Tor and downstream-browser users need patched Gecko builds or full process restarts.
- **Watch next:** Tor’s patch release, downstream adoption, cross-origin regression tests, and audits of other unordered browser APIs.
