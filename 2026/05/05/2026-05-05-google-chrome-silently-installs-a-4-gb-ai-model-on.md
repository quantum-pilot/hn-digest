# Google Chrome silently installs a 4 GB AI model on your device without consent

- Score: 1205 | [HN](https://news.ycombinator.com/item?id=48019219) | Link: https://www.thatprivacyguy.com/blog/chrome-silent-nano-install/

### TL;DR
Chrome now downloads a ~4 GB Gemini Nano AI model (`weights.bin` in `OptGuideOnDeviceModel`) onto eligible desktops, often silently and per user profile. Deleting it usually triggers a re-download unless hidden flags or enterprise policies are used. The article argues this violates EU ePrivacy/GDPR rules on consent and transparency, and estimates 6k–60k tonnes CO₂e for one global push, plus real costs for metered users. HN discussion splits between “it’s just an update” and concerns over consent, bloat, bandwidth, and admin pain.

---

### Comment pulse
- It’s just part of Chrome → installing extra components is covered by agreeing to auto‑updates—counterpoint: 4 GB and AI/privacy implications aren’t comparable to a dictionary file.  
- Silent AI weights + Prompt/Summarizer APIs → any site can trigger multi‑GB model downloads; bad for metered links, per‑user installs, and surveillance/btc‑miner analogies.  
- Sysadmin view → per‑user 4 GB on NFS and lab PCs is disastrous; want system‑wide install or to block Chrome entirely in managed environments.

---

### LLM perspective
- View: On‑device models in mainstream browsers are inevitable; the real issue is UX and governance, not the technology itself.  
- Impact: Enterprises, schools, and metered‑access users will push back hardest, driving policies, forks, or bans on default Chrome.  
- Watch next: Chrome release notes and admin templates, regulator responses in EU/UK, and whether competitors market “no forced AI downloads.”
