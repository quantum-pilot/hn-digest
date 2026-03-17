# 'Pokémon Go' players unknowingly trained delivery robots with 30B images

- Score: 167 | [HN](https://news.ycombinator.com/item?id=47398479) | Link: https://www.popsci.com/technology/pokemon-go-delivery-robots-crowdsourcing/

### TL;DR
Niantic Spatial, the company behind Pokémon Go, has used more than 30 billion player-captured images to build a Visual Positioning System (VPS) that can localize devices to within centimeters by matching live camera views to a giant 3D map. That map, built from years of “Field Research” scans and AR gameplay, will now guide Coco Robotics’ sidewalk delivery robots where GPS is unreliable. HN readers see it as clever engineering but worry about opaque data repurposing, corporate control, and future surveillance uses.

---

### Comment pulse
- Scans feel awkward and under-rewarded → many players rarely do them; some even fake ground-only scans until Niantic started detecting and banning abusers.  
- Technically, this is large-scale structure-from-motion → colmap-style point clouds, hard part is fast city-scale feature matching and keeping maps fresh as streetscapes change.  
- Ethics split: some like the idea of a detailed world map; others want open data (e.g., OSM) and fear opaque reuse by corporations or law enforcement.

---

### LLM perspective
- View: This is the template for “fun app as sensor network” business models; similar dynamics exist for CAPTCHAs, dashcams, and smart doorbells.  
- Impact: Strong incentives to collect persistent, geolocated imagery will keep colliding with privacy norms, consent expectations, and urban anonymity.  
- Watch next: Clearer secondary-use disclosures, opt-outs, jurisdictional rules on sharing VPS-like datasets with governments, and benchmarks versus rival mapping stacks (Google, Apple, Mobileye).
