# 15 years, one server, 8GB RAM and 500k users – how Webminal refuses to die

- Score: 275 | [HN](https://news.ycombinator.com/item?id=47570940) | Link: https://community.webminal.org/t/15-years-one-server-8gb-ram-and-500k-users-how-webminal-refuses-to-die/8803

### TL;DR

Webminal has served roughly 500,000 learners since 2011 from one modest CentOS server, originally with 8GB RAM and now reportedly 4GB. The free, owner-funded browser terminal survived a datacenter fire and other outages without ads, tracking, or venture capital. Its modernized interface still wraps a decidedly old stack—Python 2.7, Flask 0.12.5, Shellinabox, and MySQL—while User Mode Linux provides isolated root labs and eBPF powers an anonymized live command ticker. HN saw a compelling case for constrained, durable engineering.

### Comment pulse

- Concurrent users matter more than 500,000 lifetime accounts; the owner said the current machine actually has 4GB RAM.
- User Mode Linux was praised as an unusually good fit for safe, low-cost teaching sandboxes.
- Readers admired the old-web ethos — counterpoint: cloud-shell alternatives offer maintained environments without one volunteer carrying operational risk.

### LLM perspective

- **View:** The durable design is less about old software than matching narrow requirements and resisting needless complexity.
- **Impact:** A tiny service can deliver global educational value when isolation, recovery, and operating costs stay disciplined.
- **Watch next:** Python migration, backup resilience, concurrency limits, kernel isolation, sponsor fatigue, and another provider failure.
