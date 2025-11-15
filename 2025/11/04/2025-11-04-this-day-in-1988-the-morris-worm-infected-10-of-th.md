# This week in 1988, Robert Morris unleashed his eponymous worm

- Score: 436 | [HN](https://news.ycombinator.com/item?id=45812024) | Link: https://www.tomshardware.com/tech-industry/cyber-security/on-this-day-in-1988-the-morris-worm-slithered-out-and-sparked-a-new-era-in-cybersecurity-10-percent-of-the-internet-was-infected-within-24-hours

- TL;DR
    - In November 1988, Robert Tappan Morris released a self-replicating worm exploiting sendmail and finger flaws on BSD Unix, overwhelming thousands of NSFNET hosts, forcing shutdowns and costly cleanups, and leading to a landmark CFAA conviction. The article frames it as a measurement experiment gone wrong; HN commenters dispute the “10% of the Internet” figure as a guess and stress the severe operational disruption. Others surface primary postmortems and note Morris’s later MIT role teaching distributed systems.

- Comment pulse
    - “10% infected” is dubious → contemporaries recall it as a guess from ~60k hosts; UUCP inflated counts — counterpoint: article cites ~6,000 of ~60,000 systems.
    - Impact was massive, not harmless → mail relays shut, 56 kbps links clogged, NSF collaboration stalled; aftermath built outage procedures and eroded default trust.
    - Primary sources and legacy → CACM “With Microscope and Tweezers” and RFC 1135; IBM’s 1987 Christmas Tree EXEC; Morris later taught MIT 6.824.

- LLM perspective
    - View: Self-replication plus tiny bugs still explodes; modern vectors are CI/CD pipelines, npm registries, and SaaS integrations.
    - Impact: Operators need kill switches, segmentation, strict egress, and staged rollouts; legal exposure remains even for “research” code.
    - Watch next: Agentic-AI worm exercises, supply-chain blast-radius benchmarks, mandatory out-of-band comms during incidents.
