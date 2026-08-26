# LWN is currently under the heaviest scraper attack seen yet

- Score: 140 | [HN](https://news.ycombinator.com/item?id=46651887) | Link: https://social.kernel.org/notice/B2JlhcxNTfI8oDVoyO

### TL;DR

LWN’s Jonathan Corbet says tens of thousands of addresses are creating its worst scraper-driven DDoS, degrading responsiveness and threatening the site’s preference for frictionless reader access. HN commenters struggled to explain the economics and attribution: possibilities ranged from careless one-off agents and small AI firms to aggressive commercial crawlers using residential proxies. Operators of niche sites reported similar overloads and login walls. Discussion also linked scraping to license evasion, while warning that anti-bot JavaScript can damage search indexing and automated tests.

### Comment pulse

- Polite crawling is an engineering choice → operators said agents often omit delays, backoff, APIs, and robots.txt compliance.
- Attribution remains uncertain → counterpoint: reports blamed small or Chinese firms, generic user agents, residential proxies, and individual agent users.
- Defenses impose collateral costs → login walls and JavaScript traps protect infrastructure but obstruct readers, search engines, and testing tools.

### LLM perspective

- View: Cheap agent-generated crawlers turn individual negligence into aggregate infrastructure pressure, even without a coordinated attacker.
- Impact: Independent publishers may retreat behind authentication, weakening the open web for humans and well-behaved machines.
- Watch next: Measure request duplication, robots.txt compliance, crawler identity, proxy-provider accountability, and whether standardized agent throttling emerges.
