# JSON-LD Explained for Personal Websites

- Score: 141 | [HN](https://news.ycombinator.com/item?id=48621517) | Link: https://hawksley.dev/blog/json-ld-explained-for-personal-websites/

### TL;DR

JSON-LD embeds a Schema.org graph in a non-executable script so crawlers can identify a personal site’s entities and relationships. The guide recommends stable URL-fragment IDs linking WebSite, WebPage, Person, ProfilePage, SoftwareApplication, BreadcrumbList, CollectionPage, Blog, and BlogPosting nodes; at minimum, describe the site, profile page, and person on the homepage. Reused IDs let crawlers merge facts across pages, though single-page scrapers need local context. HN found the implementation practical but questioned whether richer search displays justify duplicated metadata when Google increasingly answers directly; supporters argued widespread annotation enables competing discovery tools.

### Comment pulse

- SEO value is contested → skeptics say structured data feeds answer boxes that displace source visits — counterpoint: advocates see richer results and alternative-search infrastructure.
- Duplication is acceptable but fragile → metadata repeats visible content like titles, so generators and validation must prevent facts drifting across representations.
- Business data has concrete consumers → addresses, hours, phones, and menus can populate map platforms even when generic personal-site ranking gains remain uncertain.

### LLM perspective

- **View:** JSON-LD is an interoperability layer, not visible content; its payoff depends entirely on trustworthy consumers and consistent maintenance.
- **Impact:** Stable entity IDs may improve disambiguation across social profiles, posts, and projects, especially for common names and fragmented archives.
- **Watch next:** Measure rich-result eligibility and referral changes; lint schemas against rendered content, test merged graphs, and minimize personal-location disclosure.
