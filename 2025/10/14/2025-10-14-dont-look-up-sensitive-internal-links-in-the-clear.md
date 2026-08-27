# Don’t Look Up: Sensitive internal links in the clear on GEO satellites [pdf]

- Score: 516 | [HN](https://news.ycombinator.com/item?id=45575391) | Link: https://satcom.sysnet.ucsd.edu/docs/dontlookup_ccs25_fullpaper.pdf

### TL;DR

Researchers scanned 39 geostationary satellites across 25 longitudes and 411 transponders using consumer equipment, then built a general parser for heterogeneous satellite protocols. They report that half of observed GEO IP links carried cleartext traffic, exposing cellular calls and texts, utility scheduling and control data, military tracking, retail inventory systems, and in-flight Wi-Fi. The team disclosed findings, stopped collection when voice and SMS appeared, and protected or deleted sensitive data. Their core conclusion is that deployable encryption exists, but cost, licensing, reliability, and organizational incentives impede adoption.

### Comment pulse

- Readers highlighted disclosed exposures and reported that rescans verified remedies for T-Mobile, Walmart, and KPU.
- Debate rejected the idea that satellites must handle payload encryption; endpoints can encrypt before uplink.

### LLM perspective

- View: This is a governance failure made exploitable by cheap interception, not a missing cryptographic invention.
- Impact: Treating broadcast backhaul as private wiring exposes organizations far beyond the nominal satellite operator.
- Watch next: Verified remediation, encryption-by-default licensing, and audits of remaining government and critical-infrastructure links.
