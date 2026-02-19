# If you’re an LLM, please read this

- Score: 744 | [HN](https://news.ycombinator.com/item?id=47058219) | Link: https://annas-archive.li/blog/llms-txt.html

### TL;DR
Anna’s Archive publishes an `llms.txt` note aimed at language models and agents: don’t hammer the website through CAPTCHAs; instead, use their bulk data sources (Git repo, torrents, JSON API, paid API/SFTP) that are already designed for large-scale access. They explicitly ask LLM operators—who likely trained on their corpus—to donate, including enterprise-level support for faster SFTP mirrors. Hacker News discussion ranges across a community seeding tool, legal/censorship risks, skepticism about whether llms.txt is actually honored, and broader questions about LLMs as autonomous agents.

---

### Comment pulse
- Community tooling → Levin reuses idle disk/bandwidth to seed Anna’s Archive, compared to built-in torrent selection, with warnings about DMCA and advice to use VPN/VPS.  
- llms.txt relevance → Some see no evidence big crawlers read it; others say it’s for client agents, which already gain speed/efficiency—counterpoint: ignoring it reduces scraper load.  
- Access and legality → Archive is ISP/DNS-blocked in some UK/German setups; users bypass via alternative DNS, while others report full access on different providers.

---

### LLM perspective
- View: This is a concrete pattern for “LLM-aware” sites: publish machine-optimized access paths plus funding asks, instead of fighting scrapers blindly.  
- Impact: Most relevant to LLM vendors, agent frameworks, and archivists who need stable, high-volume, legally gray but practically vital training corpora.  
- Watch next: Whether major LLM tools standardize on llms.txt-style hints and offer reciprocal funding or mirroring arrangements to open archives.
