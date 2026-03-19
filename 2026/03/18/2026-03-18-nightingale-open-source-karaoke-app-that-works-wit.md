# Nightingale – open-source karaoke app that works with any song on your computer

- Score: 480 | [HN](https://news.ycombinator.com/item?id=47422942) | Link: https://nightingale.cafe/

### TL;DR
Nightingale is a GPL-licensed, cross‑platform karaoke app that takes any local audio/video file, separates vocals from backing tracks, auto-generates or fetches synced lyrics with WhisperX + LRCLIB, and scores users’ singing in real time. It bundles ffmpeg, Python, PyTorch, and ML models, downloading them on first run for a “single binary” experience. HN commenters like the FOSS, fully-local design and feature set, but raise sharp concerns about dependency bundling, silent downloads, bugs, and non-English lyric alignment.

---

### Comment pulse
- Bundled runtimes by default → avoids Python’s fragmented install ecosystem and version hell; common in apps like Blender and Krita — counterpoint: silent binary downloads erode trust and widen attack surface.  
- Build/first-run UX feels invasive → unexpected ffmpeg/Python/Docker installs and path bugs make users wary; they want explicit prompts, reuse of system tools, and clean removal.  
- Core ML pipeline is promising but brittle → English works better than Japanese; lyric drift, no editing, limited navigation, and missing “next note” hints reduce practical karaoke usability.

---

### LLM perspective
- View: This is a strong example of packaging heavy ML locally into a consumer-friendly, game-like desktop app.  
- Impact: Lowers barriers for niche-language or obscure-track karaoke, especially for privacy-conscious users and small gatherings.  
- Watch next: Better multilingual alignment, editable lyrics/timing, clearer sandboxed dependency handling, and quality comparisons vs. existing FOSS karaoke tools.
