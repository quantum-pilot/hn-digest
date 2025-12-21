# Backing Up Spotify

- Score: 634 | [HN](https://news.ycombinator.com/item?id=46338339) | Link: https://annas-archive.li/blog/backing-up-spotify.html

### TL;DR
Anna’s Archive has scraped and packaged most of Spotify into a preservation dataset: metadata for ~256M tracks and ~186M unique ISRCs, plus 86M Ogg audio files (~300 TB) prioritized by popularity, covering an estimated 99.6% of actual listens. Data ships as torrents and queryable SQLite databases, enabling large‑scale analysis (genres, popularity, audio features) and “true shuffle” playlists. HN sees it as a milestone for cultural preservation and research, but debates legality, artist compensation, AI training, and platform censorship.

---

### Comment pulse
- Technical milestone / research bonanza → Massive, structured music+metadata corpus is ideal for classification, recommendation, and generative models—counterpoint: enabling more AI “slop” may further harm musicians.  
- Not What.CD, but dwarfs it in scale → What.CD prized quality, obscurities, and community; Spotify’s rip is licensed catalogs plus spam/AI junk, yet historically unparalleled in size.  
- Preservation vs access and censorship → Users note songs vanishing from platforms, ISP blocking of Anna’s Archive, and quiet de‑indexing of piracy‑adjacent repos by search engines.

---

### LLM perspective
- View: This is effectively “ImageNet for music,” but with real copyright landmines; quiet use is likely, public use is risky.  
- Impact: Musicologists, recommender‑system researchers, and open‑source ML projects gain a common reference corpus independent of Spotify’s changing APIs.  
- Watch next: Lawsuits, ISP blocking, and whether any reputable lab publishes results that clearly depend on this dataset.
