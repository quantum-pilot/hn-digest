# The AV2 Video Standard Has Released (Final v1.0 Specification)

- Score: 337 | [HN](https://news.ycombinator.com/item?id=48340910) | Link: https://av2.aomedia.org

### TL;DR
AV2, AOMedia’s successor to AV1, has shipped its 1.0 spec and reference encoder/decoder (AVM). It promises roughly 20–30% bitrate savings versus AV1 plus important features like native multi‑stream support (for VR, multi‑angle sports, alpha/overlay streams) and better handling of screen/AR content. Hacker News discussion is excited but skeptical about near‑term practicality: software encoders are currently extremely slow, specialized hardware may not be common until late decade, and looming patent and “royalty‑free” risks remain unresolved.

---

### Comment pulse
- Adoption timeline → Reference encoder runs ~1 fps; many expect usable hardware decode/encode and common AV2 streaming only around 2028–2030 — counterpoint: production encoders historically get much faster.
- Legal risk vs alternatives → AV-family “royalty‑free” status seen as fragile, with AV1 lawsuits brewing; others argue HEVC-style patents are clearly worse and AV1 suits are slow and unproven.
- AV2 spinoffs and AI codecs → Interest in AV2-powered AVIF evolution and neural codecs; feasibility hinges on NPUs, standard APIs, and battery/power versus fixed-function silicon.

---

### LLM perspective
- View: AV2 looks like a long-horizon, infrastructure codec: great for giants (YouTube, Netflix, VR platforms), marginal for small producers short term.
- Impact: Hardware vendors, browser engines, and CDNs will determine whether AV2 becomes ubiquitous or stays a niche “premium efficiency” option.
- Watch next: Performance of non-reference encoders, first shipping hardware decoders, AVIF/AV2 tooling, and outcomes of early AV1 patent litigation.
