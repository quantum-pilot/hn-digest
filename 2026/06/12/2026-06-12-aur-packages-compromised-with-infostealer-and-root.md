# AUR packages compromised with Infostealer and Rootkit

- Score: 299 | [HN](https://news.ycombinator.com/item?id=48500447) | Link: https://discourse.ifin.network/t/400-aur-packages-compromised-with-infostealer-and-rootkit/577

### TL;DR

An attacker spoofed a trusted AUR maintainer, adopted more than 408 orphaned packages, and inserted preinstall scripts that fetched malicious NPM and Bun dependencies carrying an infostealer and eBPF rootkit. Arch maintainers believed all known malicious commits were removed by 17:30 UTC on June 12, but exposed systems may require credential rotation and reinstallation because rootkit presence destroys trust. Hacker News debated whether users should audit every PKGBUILD, arguing dependency chains make that unrealistic, and favored tighter adoption controls, ownership-change warnings, revocation data, and faster incident notices.

### Comment pulse

- Manual review is necessary but insufficient → PKGBUILDs expose obvious changes, while nested dependency payloads make complete human auditing impractical.

- Orphan adoption is the key weakness → attackers inherit package history and reputation; commenters proposed new submissions, aging purges, or ownership-change alerts.

- Incident communication split opinion → users wanted immediate blocking and warnings — counterpoint: AUR is volunteer-run Git infrastructure without install tracking.

### LLM perspective

- **View:** The failure is a trust-transition problem: reputation survived package ownership changes that should have reset scrutiny.

- **Impact:** Other registries face similar economics when low-friction publishing meets opaque transitive dependencies.

- **Watch next:** Verify the final package list, control changes, downstream dependency removals, forensic indicators, and confirmed victim count.
