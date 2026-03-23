# Cloudflare flags archive.today as "C&C/Botnet"; no longer resolves via 1.1.1.2

- Score: 363 | [HN](https://news.ycombinator.com/item?id=47474255) | Link: https://radar.cloudflare.com/domains/domain/archive.today

### TL;DR
Cloudflare’s malware-filtering resolver 1.1.1.2 now classifies archive.today and related domains as “Command & Control/Botnet” and “DNS tunneling,” returning 0.0.0.0 with a “censored” note. HN commenters tie this to archive.today’s disputed JavaScript-based DDoS behavior against a critic’s blog and broader worries over paywall circumvention and copyright. Discussion splits between seeing the block as legitimate security hygiene on a security-focused DNS variant and as infrastructure-level censorship hampering a widely used, free web archiving tool.

### Comment pulse
- Cloudflare malware DNS blocking archive.today is appropriate → injected JS mass-queries a target blog, resembling command-and-control abuse — counterpoint: only optional 1.1.1.2 users are affected.  
- Block reflects wider pressure on archive.today → FBI subpoenas and dubious CSAM-based complaints push infrastructure providers to treat it as risky, regardless of user utility.  
- Ethics of outing the operator divide users → some call investigations doxxing that endangers a free archive; others say anonymity is untenable amid alleged attacks.  

### LLM perspective
- View: Centralized DNS filtering blurs malware protection and content governance; criteria like “C&C/Botnet” risk being stretched to policy disputes.  
- Impact: Heavy users of archive.today behind managed resolvers may lose access silently, nudging archivists and journalists toward more decentralized mirroring.  
- Watch next: Whether other DNS or browser vendors follow this classification, and if Cloudflare documents criteria or an appeal process.
