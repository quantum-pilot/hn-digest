# The RAM shortage could last years

- Score: 166 | [HN](https://news.ycombinator.com/item?id=47822414) | Link: https://www.theverge.com/ai-artificial-intelligence/914672/the-ram-shortage-could-last-years

### TL;DR
Global DRAM production is far behind surging demand from AI data centers, especially for high‑bandwidth memory (HBM). Samsung, SK Hynix, and Micron are adding fabs, but most capacity won’t arrive until 2027–2028, leaving only ~60 percent of demand covered and possibly extending tight supply to 2030. Because new lines prioritize HBM over general-purpose DRAM, consumer devices—phones, laptops, VR headsets, gaming handhelds—face sustained price hikes. HN readers debate who bears the risk, whether this is a “shortage” or a new price level, and if software/AI optimizations can really offset demand.

---

### Comment pulse
- AI-driven HBM demand starves commodity DRAM → capacity is pre-allocated to data centers, with grid constraints delaying some builds—counterpoint: makers under-built specifically to avoid being stuck with overcapacity.  
- Multi‑year “shortage” = structurally higher prices → gamers are marginal, corporate AI demand is inelastic, and supply can’t ramp fast before 2028 despite high prices.  
- Hope: pricier RAM forces leaner software, local models, and quantization (TurboQuant, SpectralQuant, new architectures) → reality: optimizations free capacity, but exploding token/context use quickly reabsorbs it.

---

### LLM perspective
- View: This is an AI infrastructure bottleneck, not just a PC-parts story; HBM-first strategies structurally deprioritize consumer DRAM.  
- Impact: Cloud AI costs stay high; OEMs raise prices or cut RAM; small vendors and DIY builders lose the most flexibility.  
- Watch next: Actual fab ramp dates, big AI firms renegotiating memory contracts, and real-world adoption of aggressive KV-cache and architecture-level memory savings.
