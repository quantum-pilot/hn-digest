# Redis array: short story of a long development process

- Score: 213 | [HN](https://news.ycombinator.com/item?id=48009172) | Link: https://antirez.com/news/164

### TL;DR
Redis creator antirez describes designing and implementing a new sparse-friendly Array type and ARGREP regex search, using GPT‑5.x as a constant collaborator. He spent a month co-writing a detailed spec, then iteratively auto-coded, redesigned the hierarchy, optimized the TRE regex library, and stress-tested everything, while personally reviewing every line. He argues LLMs don’t replace deep systems expertise but act as a safety net and force multiplier, enabling more ambitious data structures without compromising correctness or portability.

---

### Comment pulse
- Antirez is an outlier; his 4‑month AI-assisted effort shouldn’t justify CEOs forcing full agent workflows—counterpoint: shows skilled experts can multiply impact with coding agents.  
- Several describe spec-first, multi-AI “adversarial” design and code review; resembles Google-style processes, but AI compresses critique cycles while humans still own polish.  
- Some worry about reviewing a monolithic 22k-line PR; others clarify core is ~5k LOC and Redis historically evolves via large, founder-led changes.  

---

### LLM perspective
- View: AI lets senior engineers tackle riskier designs—deeper hierarchies, regex engine tuning—without compromising quality, if specs and reviews stay rigorous.  
- Impact: Databases and infra can ship richer data structures faster, while core maintainers’ judgment, not raw coding hours, becomes the bottleneck.  
- Watch next: Watch adoption of Redis arrays, ARGREP, TRE tweaks in production; compare memory and latency against hashes, lists, external search systems.
