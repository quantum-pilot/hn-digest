# Molly: An Improved Signal App

- Score: 200 | [HN](https://news.ycombinator.com/item?id=46080916) | Link: https://molly.im/

### TL;DR

Molly is an independent Android fork of Signal offering a fully open-source build, encrypted local database, multi-device pairing, automatic locking, RAM shredding, Tor and SOCKS support, Material You theming, and optional UnifiedPush notifications without Google services. Commenters valued F-Droid availability and user control, but emphasized that modifying an encrypted messenger expands the code and maintainers users must trust. One user reported losing registration and unusable backups, while others distinguished Molly's standard and FOSS notification variants.

### Comment pulse

- Removing Google dependencies serves stricter threat models → UnifiedPush avoids Firebase timing metadata at a possible reliability cost.
- Forks restore client choice → counterpoint: protocol changes and third-party code can weaken compatibility or security guarantees.
- Reliability is part of privacy tooling → failed registration or backups can strand users despite stronger local protections.

### LLM perspective

- View: Molly offers meaningful autonomy, but its security value depends on maintenance quality as much as added controls.
- Impact: De-Googled Android users gain a practical Signal client while accepting extra update and recovery risk.
- Watch next: Audit release cadence, upstream patch lag, reproducible builds, backup recovery, and UnifiedPush reliability.
