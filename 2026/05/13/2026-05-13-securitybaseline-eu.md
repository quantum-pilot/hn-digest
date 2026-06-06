# SecurityBaseline.eu

- Score: 222 | [HN](https://news.ycombinator.com/item?id=48118763) | Link: https://internetcleanup.foundation/2026/05/european-governments-3000-tracking-sites-1000-phpmyadmins-and-99pct-poorly-encrypted-email-introducing-securitybaseline-eu/

### TL;DR

SecurityBaseline.eu is a new EU-wide monitoring project that scans ~200k domains from 67k public bodies and visualizes 21 security/privacy metrics on daily-updated traffic‑light maps. Its first results are stark: 3,081 government sites set marketing/tracking cookies without valid consent, over 1,000 phpMyAdmin database consoles are exposed on the public internet, and only about 1% of governmental mail domains meet modern TLS guidelines (with the Netherlands and Denmark clear outliers). HN discussion focuses on legal barriers, methodology quality, and policy implications.

---

### Comment pulse

- Overcriminalized “hacking” laws chill EU security research → in Germany, even mild automated scanning can risk prosecution, so vulnerabilities persist unreported.  

- Metrics are useful but some inputs look wrong → in Hungary, many “government” sites are random or decommissioned, undermining trust in the public shaming approach.  

- Criteria choices shape the map → some readers see “red” for missing DNSSEC as overstated, and argue tracking big-cloud email hosting is at least as critical.

---

### LLM perspective

- View: Public, comparable, per‑region metrics strongly incentivize governments to adopt baseline security and privacy standards over time.  

- Impact: Procurement rules, gov IT vendors, and national CERTs will likely feel pressure to clean up exposed admin tools and upgrade mail/TLS.  

- Watch next: Independent validation of domain lists, expanded panels beyond phpMyAdmin, and whether EU policy picks up these baselines as formal minimum requirements.
