# What I learned selling 2,500 MIDI recorders: Hardware is not so hard

- Score: 385 | [HN](https://news.ycombinator.com/item?id=48966713) | Link: https://chipweinberger.com/articles/20260719-hardware-is-not-so-hard

- TL;DR  
  A solo software engineer built Jamcorder, a simple MIDI recorder for digital pianos, sold 2,500 units, and found that—at this scale—hardware was smoother than the 200k‑LOC software stack. By aggressively simplifying the design (25‑component PCB, minimal features, pre‑certified ESP32 module, easy assembly), keeping margins high, and tightly managing manufacturing and QA, he avoided common hardware pitfalls. HN commenters largely agree this works for niche, low‑complexity products but argue it underplays how hard scaling and compliance are.

- Comment pulse  
  Hardware seems “easy” here → ultra‑simple design, pre‑certified RF module, low volumes; avoids most regulatory, reliability, and supply‑chain edge cases—counterpoint: this is an outlier compared to many Kickstarters.  
  Real hardness → designing complex, multi‑board products at scale; forecasting demand; cash‑intensive tooling and inventory; failures or delays can sink a small hardware company.  
  Niche success proof → multiple users report Jamcorder as “flawless” and exactly filling a need, validating the focused, simple‑hardware/high‑value approach.

- LLM perspective  
  View: For indie builders, ruthlessly scoping hardware complexity and feature set can make “hard” hardware tractable and profitable.  
  Impact: Encourages software folks to attempt tightly‑scoped devices, especially where off‑the‑shelf modules and high margins are viable.  
  Watch next: Detailed follow‑ups on molding, anti‑counterfeit, and certifications will clarify which parts stay easy as volumes and complexity grow.
