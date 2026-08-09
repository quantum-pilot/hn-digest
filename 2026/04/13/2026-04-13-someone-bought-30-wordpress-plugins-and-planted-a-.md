# Someone Bought 30 WordPress Plugins and Planted a Backdoor in All of Them

- Score: 617 | [HN](https://news.ycombinator.com/item?id=47755629) | Link: https://anchor.host/someone-bought-30-wordpress-plugins-and-planted-a-backdoor-in-all-of-them/

### TL;DR

After a six-figure acquisition of the Essential Plugin portfolio, the buyer’s first WordPress SVN commit allegedly inserted a remote-deserialization backdoor across 30-plus plugins. It remained dormant eight months, then downloaded code that injected Googlebot-only SEO spam into `wp-config.php`, resolving its changing command server through an Ethereum contract. WordPress.org closed 31 plugins and force-disabled the loader, but did not remove existing configuration-file infections. The investigator found affected plugins on 22 client sites. Discussion framed this as a governance failure around ownership transfers, inherited trust, and automatic updates.

### Comment pulse

- Attackers can buy trusted dependencies or bribe insiders, making governance and provenance as important as finding implementation vulnerabilities.
- Lockfiles and fewer dependencies reduce exposure. — counterpoint: freezing updates also preserves known vulnerabilities and shifts review burden to users.
- Commenters want signed releases, visible ownership-transfer history, new-maintainer warnings, and independent package labels.

### LLM perspective

- **View:** Maintainer identity changes should be treated like high-risk code changes, not routine metadata.
- **Impact:** Site operators must inspect persisted files; removing or disabling the plugin may leave payloads active.
- **Watch next:** WordPress transfer controls, forced-cleanup tooling, affected-install counts, and defenses against blockchain-resolved command servers.
