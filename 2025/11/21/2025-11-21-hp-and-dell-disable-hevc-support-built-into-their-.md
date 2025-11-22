# HP and Dell disable HEVC support built into their laptops' CPUs

- Score: 214 | [HN](https://news.ycombinator.com/item?id=46002989) | Link: https://arstechnica.com/gadgets/2025/11/hp-and-dell-disable-hevc-support-built-into-their-laptops-cpus/

### TL;DR
HP and Dell are shipping many new business laptops with HEVC/H.265 hardware decoding deliberately disabled in drivers/codec packages, even though the CPUs fully support it. They appear to be dodging rising per-device HEVC royalties, instead pushing customers to buy third‑party or Microsoft Store codecs. The result: choppy browser video, broken 4K streaming, and heavier CPU load in conferencing apps. Commenters split blame between OEM penny‑pinching and a dysfunctional HEVC patent regime, arguing this will accelerate adoption of AV1/VP9.

---

### Comment pulse
- OEMs saved maybe 4–24 cents per unit but shipped $800 “Pro” laptops with worse Teams and video than older models—counterpoint: cost hikes may keep rising.  
- Critics decry patent-pool double-dipping across Intel/AMD, OEMs, and apps; defenders note royalties hit whoever finally enables HEVC for end users.  
- Technically, hardware blocks still work; OEM graphics drivers and missing system codecs disable them. Intel’s generic drivers, Linux, or $1 HEVC extensions restore acceleration.  

---

### LLM perspective
- View: Codec licensing now directly degrades baseline PC functionality; expect more silent feature removals tied to royalty-bearing standards.  
- Impact: IT buyers must scrutinize codec support like CPU or RAM, especially for fleets relying on video conferencing and 4K content.  
- Watch next: Monitor OEM specs, Microsoft’s codec bundling, and whether major streamers/browsers more aggressively prioritize AV1 over HEVC on PCs.
