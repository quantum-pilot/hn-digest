# Flux 3 X Mimic: The Next Generation of Video-Action Models

- Score: 308 | [HN](https://news.ycombinator.com/item?id=49033127) | Link: https://bfl.ai/blog/flux-3-mimic

### TL;DR
FLUX 3 is Black Forest Labs’ multimodal “world model” trained mainly via video prediction, then reused as the backbone for FLUX‑mimic, a video‑action model controlling real robots. Actions are decoded from intermediate video features, unifying generative modeling and representation learning (Self‑Flow), yielding better manipulation, fewer demos, and natural recovery from failures. Deployed with mimic robotics at Audi, the system runs end‑to‑end in ~100 ms and reportedly beats prior vision‑language‑action models, though HN notes strong prior art in similar approaches.

---

### Comment pulse
- Novel path but not entirely new → using video models as world models for robots echoes Nvidia, Waymo, Luma, Runway—counterpoint: integrating this deeply into a product is still rare.  
- Dexterous behavior impressed viewers → retries on fine manipulation feel new, yet Google’s VLA and GeneralistAI demos show comparable or better capabilities.  
- Writing style drew jokes → “less disentangled representations” sounded LLM‑ish, prompting meta‑discussion about over-attributing awkward phrasing to AI authorship.

---

### LLM perspective
- View: Treating high-capacity video generators as reusable physical world models is becoming the default architecture for manipulation and control.  
- Impact: Lowers data and engineering cost for factory robots; benefits integrators, OEMs, and GPU vendors, threatens hand‑engineered automation vendors.  
- Watch next: Independent benchmarks versus OpenVLA/Generalist, open‑weight variants for research, and evidence on long‑term reliability and safety in production.
