# Gentoo bugzilla closed due AI bot scraper overload

- Score: 151 | [HN](https://news.ycombinator.com/item?id=49221864) | Link: https://social.treehouse.systems/@mgorny/117058483039362779

### TL;DR

A Gentoo contributor temporarily took Bugzilla offline after suspected LLM scrapers made it unusable, spreading requests across thousands of IPv4 addresses without a blockable pattern. Related maintainers described IPv6 prefix rotation and residential-proxy traffic where each source looks ordinary, defeating simple rate limits. Gentoo may restrict more access to logged-in users. HN discussion centered on an attribution and incentive failure: delegated scraping hides responsibility, while authentication, proof-of-work, micropayments, or CDN defenses all impose cost and friction on legitimate users of public infrastructure.

### Comment pulse

- Distributed residential proxies make per-IP blocking ineffective; each device behaves normally while aggregate traffic overwhelms volunteer infrastructure.
- Authentication and proof-of-work preserve servers — counterpoint: both exclude low-power devices, casual readers, archives, and automation.
- Micropayments could price abusive volume, but international payment friction and transaction fees can cost more than the requested content.

### LLM perspective

- **View:** An open bug tracker’s public-good value has become an uncompensated operational liability.
- **Impact:** Contributors lose productive time; users face outages or gates; scrapers may still obtain data through delegated networks.
- **Watch next:** Reopening terms, logged-in access, scraper identification, cacheable mirrors, dataset-sharing norms, and upstream accountability.
