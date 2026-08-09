# LinkedIn is searching your browser extensions

- Score: 1527 | [HN](https://news.ycombinator.com/item?id=47613981) | Link: https://browsergate.eu/

### TL;DR

Fairlinked alleges LinkedIn’s Chrome-site code probes over 6,000 browser extensions by testing known resources and DOM residue, then transmits encrypted results without disclosure. Because LinkedIn links visitors to identities and employers, the group says data can reveal sensitive traits, job searches, and competitors’ customer usage; it has filed DMA proceedings. LinkedIn responds that detection targets scraping and automation extensions, protects members and stability, never infers sensitive information, and follows a failed German injunction by the campaigner. HN agreed probing is invasive but sharply disputed motive, scope, and alarmist framing.

### Comment pulse

- Specific-ID probing may reflect browser API limits rather than arbitrary computer access — counterpoint: choosing sensitive extensions still creates serious privacy risk.
- Ad blockers may miss detection embedded in application code; changing browsers can stop some probing but not DOM-residue fingerprinting.
- LinkedIn says extension signals contextualize abnormal scraping — counterpoint: commenters preferred rate limits over inspecting users’ software environments.

### LLM perspective

- **View:** The observable technique and disputed purpose should be evaluated separately; neither side’s motive claims establish actual downstream use.
- **Impact:** Extension developers, job seekers, and enterprise customers face profiling risk even when detected attributes are only probabilistic.
- **Watch next:** Independent reproduction, published scan lists, LinkedIn disclosures, regulator findings, court records, and browser-level defenses against extension probing.
