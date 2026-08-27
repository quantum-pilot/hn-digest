# Why I chose Lua for this blog

- Score: 150 | [HN](https://news.ycombinator.com/item?id=45452261) | Link: https://andregarzia.com/2025/03/why-i-choose-lua-for-this-blog.html

### TL;DR

Andre Garzia replaced a friction-heavy Racket static generator with a deliberately small dynamic blog written in Lua. The site uses CGI, one process per request, SQLite, Mustache templates, and a limited set of LuaRocks, alongside small hand-built libraries for features such as Micropub and IndieAuth. He chose Lua for its slow evolution, C89 bootstrap, small language surface, and easy native integration, accepting lower theoretical throughput and fewer libraries in exchange for understanding the whole system and maintaining it for decades.

### Comment pulse

- Readers celebrated homemade blog engines as low-stakes learning projects, while warning that custom web-facing code still carries security risk.
- Alternatives included static generation, Python, Fennel, Pandoc, and redbean; cross-platform LuaRocks maintenance drew concern.

### LLM perspective

- View: Longevity comes from limiting moving parts more than choosing the ecosystem with the most capabilities.
- Impact: A comprehensible personal stack can preserve content and motivation when dependency churn would otherwise end maintenance.
- Watch next: Security review, backup portability, Lua version upgrades, and dependency availability will test the longevity claim.
