# 10 Years of Let's Encrypt

- Score: 411 | [HN](https://news.ycombinator.com/item?id=46208962) | Link: https://letsencrypt.org/2025/12/09/10-years

TL;DR
- Let’s Encrypt celebrates ten years since its first public certificate, having scaled from millions to tens of millions of daily issuances and pushing HTTPS usage to ~80–95% of web traffic. The post highlights milestones (ACME automation, wildcard, IP and short-lived certs), huge infrastructure upgrades, and crucial partners like IdenTrust and early sponsors. Hacker News commenters recall the painful, expensive pre-LE TLS ecosystem, praise its “boring default” status, and debate remaining issues like CA centralization and hard-to-automate internal/IoT use cases.

Comment pulse
- Let's Encrypt made HTTPS the boring default → people recall EV-certificate status games fading; almost no end-users notice or question LE issuance.  
- Pre-LE TLS was costly and manual → anecdotes of $30k wildcard quotes and hand-deployed GoDaddy certs; ACME automation erased most operational pain.  
- CA centralization worries persist → needing a trusted CA gates web features — counterpoint: this predates LE and mirrors existing DNS and PKI dependencies.  

LLM perspective
- View: Let's Encrypt shows how nonprofit, automated infrastructure can change defaults more than new crypto primitives.  
- Impact: Operators of anything with HTTPS must now embrace automation; manual certificate handling will break under 45‑day lifetimes.  
- Watch next: Tooling for internal/IoT ACME, browser policies on shorter lifetimes, and funding models to keep nonprofit CAs sustainable.
