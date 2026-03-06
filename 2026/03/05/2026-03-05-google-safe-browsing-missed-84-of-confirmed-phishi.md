# Google Safe Browsing missed 84% of confirmed phishing sites

- Score: 264 | [HN](https://news.ycombinator.com/item?id=47262347) | Link: https://www.norn-labs.com/blog/huginn-report-feb-2026

### TL;DR
Norn Labs’ Huginn system tracked 254 human-confirmed phishing sites in February 2026 and found Google Safe Browsing (GSB) had not yet flagged 84% of them at discovery time. Many attacks lived on large, “trusted” platforms (Weebly, Vercel, GitHub, IPFS, even Google Docs/Forms/Sites), which can’t simply be domain-blocked. Their Muninn browser extension combines a low-noise automatic scan with a very conservative screenshot-based deep scan. Case studies show multi-stage, anti-bot, brand-perfect phishing, underscoring how reactive URL blocklists miss short-lived, evasive campaigns.

---

### Comment pulse
- Methodology skepticism → tiny, hand-reviewed dataset and marketing framing raise concerns; deep scan flags every benign sample as suspicious—counterpoint: author explains manual confirmation bottleneck and timing focus.  
- Blocklists vs power → some distrust centralized blocklists as censorship tools; others argue phishing lists are objective abuse, and browser vendors can restrict whatever they host.  
- User experience and gaps → people dislike unskippable Safe Browsing download prompts and note phishing campaigns abusing Gmail/Google services, reinforcing that protection is incomplete today.

---

### LLM perspective
- View: Vendor study, but the emphasis on fast, evasive, platform-hosted phishing reflects well-known pain points in current defenses.  
- Impact: Pressures browser makers and infrastructure providers to augment URL lists with content, behavior, and visual similarity analysis.  
- Watch next: Independent, larger-scale benchmarks of phishing detectors and transparency from Google and others about time-to-detection on fresh attacks.
