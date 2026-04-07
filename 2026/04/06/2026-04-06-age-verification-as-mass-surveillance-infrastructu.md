# Age verification as mass surveillance infrastructure

- Score: 289 | [HN](https://news.ycombinator.com/item?id=47659109) | Link: https://tboteproject.com/surveillancefindings/

### TL;DR
The piece documents how corporate crawlers from Meta, Microsoft/OpenAI, Google Cloud, Palo Alto (Cortex Xpanse), and Censys aggressively scrape an investigative site about age‑verification infrastructure, including full git history, document diffs, and login probes. The authors frame this as “surveillance of the investigators,” tied to firms lobbying for laws that push age‑verification into OS and infrastructure layers. They log all such access and threaten to publish detailed logs if contributors face retaliation. HN discussion questions the site’s credibility and explores privacy‑preserving age‑verification schemes.

---

### Comment pulse
- Site is likely LLM‑generated → huge volume in days, weak source linkage, “anomaly reports,” and the authors themselves mention bot writing—counterpoint: headline topic is still important.  
- Some see Thiel/Palantir et al. as obviously surveillance‑aligned → argue lack of airtight evidence here shouldn’t translate into giving them a pass.  
- Thread dives into cryptographic age proofs → ZK credentials, verifiable credentials, device flags; all have trade‑offs between anonymity, usability, and creating new surveillance chokepoints.

---

### LLM perspective
- View: Even if this project is messy and LLM‑heavy, its core concern—age checks becoming identity infrastructure—is directionally plausible.  
- Impact: Age‑verification mandates can turn OS vendors, browser makers, and ID-wallet providers into de facto global tracking and compliance gatekeepers.  
- Watch next: Concrete deployments of ZK age credentials, how major OSes implement “birthDate” fields, and whether legislators insist on auditable logs or privacy‑by‑design.
