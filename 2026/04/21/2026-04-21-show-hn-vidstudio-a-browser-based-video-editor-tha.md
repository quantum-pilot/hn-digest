# Show HN: VidStudio, a browser based video editor that doesn't upload your files

- Score: 234 | [HN](https://news.ycombinator.com/item?id=47847558) | Link: https://vidstudio.app/video-editor

### TL;DR
VidStudio is a browser-based video editor and toolkit (resize, trim, compress, audio, subtitles, thumbnails) that runs entirely client-side using FFmpeg compiled to WebAssembly and WebCodecs. Files never leave the device, so it feels like a native, private tool distributed via the web. HN commenters like the speed, presets (e.g., Discord size tiers), and “no upload” model, but raised concerns about FFmpeg’s LGPL compliance, some missing UX features, and codec/browser compatibility for phone videos.

---

### Comment pulse
- Licensing concern → Using FFmpeg (LGPL) in a closed-source WebAssembly app likely requires relinking options and source references—counterpoint: LGPL allows closed-source if obligations are met.  
- UX/performance → Encoding is impressively fast and persistent, but track reordering, transforms, and mixed aspect-ratio handling feel incomplete, especially in Firefox.  
- Local-in-browser model → People love “no account, no upload” tools and targeted presets, yet browser codec gaps (HEVC, odd audio) break some real-world phone videos.

---

### LLM perspective
- View: Strong proof-of-concept for serious, private, in-browser media tooling; correctness on licensing and codecs now matters more than adding features.  
- Impact: Casual editors, privacy-conscious users, and corporate environments gain a viable alternative to heavy native apps and opaque cloud tools.  
- Watch next: Clear LGPL/GPL compliance docs, broader codec coverage or fallback paths, progressive-web-app support, and a sustainable, non-predatory monetization model.
