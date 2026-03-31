# 15 years, one server, 8GB RAM and 500k users – how Webminal refuses to die

- Score: 275 | [HN](https://news.ycombinator.com/item?id=47570940) | Link: https://community.webminal.org/t/15-years-one-server-8gb-ram-and-500k-users-how-webminal-refuses-to-die/8803

### TL;DR
Webminal is a 15‑year‑old, single‑server Linux training site that’s quietly onboarded ~500k users using an almost archival stack: CentOS, Python 2, Flask 0.12, Shellinabox, and User Mode Linux for fully isolated root labs. Two founders, collaborating for years only via shared screen sessions over SSH, have run it ad‑free and mostly at personal expense to serve students who can’t pay. HN commenters respond with nostalgia, highlight how limitations shaped its design, and argue over whether 8GB RAM is excessive or insufficient today.

### Comment pulse
- Old‑school internet idealism → creator funds Webminal himself, keeps it ad‑free; cost constraints drove SELinux hardening, filesystem quotas, and other careful multi‑tenant tricks.  
- Unusual collaboration and hosting → cofounders began on a home server, chatting via shared screen; later hopped between clouds, often powered by sponsorships and credits.  
- Tool choices and scale → UML admired as pragmatic “old” tech; some see 8GB as lavish—counterpoint: others note multi‑user teaching loads quickly exhaust it.

### LLM perspective
- View: Shows how tightly scoped goals plus proven tech can outperform elaborate microservices for education platforms and hobby projects.  
- Impact: Validates low‑cost Linux training for underserved students; may inspire similar single‑box labs in schools and community spaces.  
- Watch next: If sponsorship funds more RAM/UML instances, and how long Python 2 and Shellinabox remain viable before forced rewrites.
