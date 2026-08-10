# Dithered QR Codes

- Score: 358 | [HN](https://news.ycombinator.com/item?id=49226742) | Link: https://www.andrewt.net/dithered-qr-codes/wtf/

### TL;DR

Decorative QR codes can hide a one-bit image around the data while retaining clear finder and alignment patterns. The technique subdivides each module into a 3×3 grid, reserves its center for encoded data, then applies Floyd–Steinberg error diffusion twice: first distributing the forced center-pixel error into neighbors, then dithering the full image. This reduces visible salt-and-pepper noise without altering many encoded bits. Commenters pointed to QArt as a fully valid alternative and warned that logos, long URLs, poor margins, printing, and low-end cameras rapidly consume scanning robustness.

### Comment pulse

- Error correction is a budget → aesthetic edits spend resilience intended for blur, damage, skew, and bad lighting.
- Diffusing forced pixels cleans the image → deliberately flipping modules yields little benefit while sharply hurting scans.
- Alternative encodings preserve validity → QArt embeds imagery by choosing the encoded representation instead of relying on damage recovery.

### LLM perspective

- **View:** The safest design optimizes the payload and dither before sacrificing encoded modules.
- **Impact:** Designers gain expressive codes, but physical deployments need larger margins and broader device testing.
- **Watch next:** Scan-rate benchmarks across printers, distances, lighting, damage, cameras, and QArt comparisons.
