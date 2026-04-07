# An open-source 240-antenna array to bounce signals off the Moon

- Score: 243 | [HN](https://news.ycombinator.com/item?id=47656622) | Link: https://moonrf.com/

### TL;DR
MoonRF is an open-source, C‑band software-defined phased-array project aimed at making Earth-Moon-Earth (EME) and advanced RF experiments accessible. It offers a $49–99 4‑antenna SDR tile (QuadRF), a 72‑antenna “Mini” array, and a 240‑antenna, ~1.5 kW “Moon” array designed for moon-bounce, RF imaging, and radio astronomy. HN commenters praise the serious engineering and low price-per-aperture, debate whether EME is more marketing than necessity, and scrutinize both the open-source claims and the “AI/agentic” branding.

---

### Comment pulse
- Open-source status questioned → skeptics dislike calling it open before shipping; others link to active GitHub and licenses — counterpoint: hardware/schematics availability and timing still matter.  
- Engineering and architecture lauded → creative Pi 5 MIPI “camera/display as SDR I/O” hack impresses, but some prefer standard PCIe/USB and doubt the “Agentic Transceiver” AI workflow claims.  
- Usefulness vs alternatives → phased array seen as overkill for slow-moving Moon compared to cheaper dishes; others note far higher power than Starlink and strong educational/experimental value.

---

### LLM perspective
- View: If documentation stays strong, this becomes a reference platform for serious hobbyist/academic RF, not just a novelty EME toy.  
- Impact: Lowers the barrier for learning phased arrays, radio astronomy, and high-speed SDR pipelines, especially for universities and clubs.  
- Watch next: Release of full hardware files, reproducible moon-bounce demos, and ports to non–Raspberry Pi SBCs with cleaner high-speed interfaces.
