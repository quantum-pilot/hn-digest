# Google Revisits JPEG XL in Chromium After Earlier Removal

- Score: 175 | [HN](https://news.ycombinator.com/item?id=46021179) | Link: https://windowsreport.com/google-revisits-jpeg-xl-in-chromium-after-earlier-removal/

### TL;DR
Google previously removed JPEG XL from Chrome, citing low interest, but is now reopening the door: a feature‑complete implementation has landed in Chromium review, including animation, and Google says it will ship once security, maintenance, and launch criteria are satisfied. Outside Chrome, JPEG XL is already used in PDFs, medical and camera workflows, and supported by Safari and Windows 11. HN discussion highlights Chrome’s Rust-only requirement, competition with AVIF/AV2, and the importance of long‑term support rather than another abandoned experiment.

---

### Comment pulse
- JPEG XL vs AVIF/AV2 → JXL encodes/decodes much faster; AVIF can beat it on quality at low bitrates; AV2 improves compression but raises compute costs.  
- Chrome’s condition → JPEG XL support is welcome only via a Rust implementation, driven by security and long‑term maintenance fears around huge C++ codec libraries.  
- Ecosystem signal → PDFs, medical imaging, cameras, Safari, and Windows 11 support show the format’s viability—counterpoint: Firefox’s continued absence slows true web ubiquity.

---

### LLM perspective
- View: Rust‑only codecs in major browsers will likely become the norm for complex media parsers and decoders.  
- Impact: CDNs, image hosts, and creative pipelines can standardize on JPEG XL once Chrome and Firefox meaningfully support it.  
- Watch next: jxl-rs performance, Chrome/Edge behind‑flags experiments, and whether Firefox aligns on Rust JPEG XL or doubles down on AVIF-only.
