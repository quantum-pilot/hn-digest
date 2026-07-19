# Regressive JPEGs

- Score: 649 | [HN](https://news.ycombinator.com/item?id=48954851) | Link: https://maurycyz.com/projects/bad_jpeg/

## TL;DR
The post explains how progressive JPEGs encode images in multiple “scans,” starting with low-frequency (blurry) data and refining detail later. By concatenating scans from many same-sized images—while stripping start/end markers—you can make later scans overwrite earlier ones, so a single JPEG “plays” a sequence as it loads. Decoder scan limits force a DC-only (very low-res) trick to reach ~90 frames. It’s mostly a fun hack: timing depends on network speed, so it’s unsuitable for real video.

---

## Comment pulse
- Similar tricks exist with PNG and GIF → servers stream partial images or use multipart/x-mixed-replace, approximating live video without JavaScript.  
- Potential steganography / filter evasion → early frames for humans, final frame for AI or scanners—counterpoint: classic steganography is simpler and more robust.  
- Possible legit use → progress visualization or webcams using controlled chunked responses, though some sites ban such tricks due to abuse concerns.

---

## LLM perspective
- View: Multi-scan formats leak surprising “dynamic” behavior when transport and decoder behavior are exploited creatively.  
- Impact: Content filters, AI vision models, and security tools may misinterpret such files, missing earlier or hidden frames.  
- Watch next: Benchmarks of scanner/AV behavior on multi-scan JPEGs; browser limits; standardized animated JPEG-like formats vs. these ad-hoc hacks.
