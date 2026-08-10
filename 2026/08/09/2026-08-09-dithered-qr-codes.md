# Dithered QR Codes

- Score: 358 | [HN](https://news.ycombinator.com/item?id=49226742) | Link: https://www.andrewt.net/dithered-qr-codes/wtf/

### TL;DR
This piece shows how to embed recognizable photos inside fully functional QR codes using error-diffusion dithering. The trick: shrink each QR data module to a single pixel in a 3×3 cell and use the surrounding 8 pixels to render a 1‑bit image. Because those center pixels are effectively random, the author runs a custom two-pass Floyd–Steinberg process that “pre-absorbs” their error into neighbors, greatly reducing visible noise. The article ends by stressing the trade-off between pretty codes and reliable scanning, which HN discusses alongside alternative image-QR techniques and concerns about overusing QR error correction.

---

### Comment pulse
- Alternative approach: Russ Cox’s QArt encodes images by choosing QR payloads that visually approximate a picture, preserving full error correction budget and validity.  
- Extensions: tools exist for color image QR codes, showing aesthetic capacity goes beyond monochrome dithering when readers control scanner environments.  
- Over-customization risk: logos, long URLs, and dense payloads already erode robustness; adding complex art may push many real-world codes into unscannable territory.

---

### LLM perspective
- View: Combine this dithering with automated scan-testing across devices to define safe aesthetic “budgets” for production use.  
- Impact: Designers, marketers, and signage creators gain more artistic freedom without blindly sacrificing scan reliability.  
- Watch next: Open libraries exposing these techniques, plus benchmarks comparing QArt-style encoding vs. dithering under print, glare, and motion.
