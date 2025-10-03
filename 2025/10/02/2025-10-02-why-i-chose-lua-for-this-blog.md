# Why I chose Lua for this blog

- Score: 150 | [HN](https://news.ycombinator.com/item?id=45452261) | Link: https://andregarzia.com/2025/03/why-i-choose-lua-for-this-blog.html

- TL;DR
  - The author rebuilt their blog in Lua to avoid fast-moving JS/Ruby ecosystems and long-term dependency rot. Lua’s slow evolution, tiny runtime, C89 portability, and few dependencies let them keep the whole system in their head. The site is dynamic but simple: CGI per request, SQLite storage, Mustache templates, and hand-rolled IndieWeb pieces. HN reminisces about DIY engines, flags CGI security risks, debates static vs dynamic simplicity, and questions LuaRocks’ cross-platform friction—suggesting Python, Fennel, or redbean as alternatives.

- Comment pulse
  - Build-your-own blog is great learning → low-risk full-stack playground; DIY CGI on the public internet raises security risks — counterpoint: small scope can be manageable.
  - Prefer static generators → simple blogs can be pure HTML or pandoc with tiny scripts; dynamic engines often unnecessary; pandoc templating complicates inter-page linking.
  - Lua maintainability debated → fans like the small runtime; skeptics cite LuaRocks friction and cross-platform pain; alternatives suggested: Python, Fennel, redbean.

- LLM perspective
  - View: Small, slow-evolving stacks minimize dependency rot and cognitive load for personal sites better than fast-moving ecosystems.
  - Impact: Best fit for solo maintainers, long-lived archives, and low-traffic blogs; trade throughput for simplicity and resilience.
  - Watch next: Publish hardening steps, threat model, and benchmarks; test on ARM/Alpine; compare CGI Lua vs OpenResty or redbean for resource use.
