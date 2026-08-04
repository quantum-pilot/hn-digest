# Regressive JPEGs

- Score: 649 | [HN](https://news.ycombinator.com/item?id=48954851) | Link: https://maurycyz.com/projects/bad_jpeg/

### TL;DR

Progressive JPEG sends coarse data first, then refines an image through ordered scans. Because each scan declares its spectral range, the author concatenates compatible images after stripping structural markers, making later scans replace what browsers already rendered. Decoder limits and JPEG rules prevent efficient detailed animation, but one DC-only scan per frame produces blocky 1/16-resolution frames and about 90-frame playback across browsers. The result is a standards-compliant pseudo-video whose speed follows network delivery because JPEG lacks frame timing, making it clever, fragile, and mostly recreational.

### Comment pulse

- Timed server chunks can approximate playback → commenters noted delivery pacing can override ordinary network timing, although the file itself still carries no timestamps.
- Novel format abuse creates analysis gaps → commenters proposed first-frame versus final-frame messages for filters or AI — counterpoint: ordinary steganography may work better.
- Practical alternatives already exist → APNG, animated GIF, Motion JPEG, and multipart replacement provide timing or streaming without exploiting progressive scans.

### LLM perspective

- **View:** The hack exploits disagreement between an image’s final state and the transient states users or automated systems observe.
- **Impact:** Content scanners, caches, screenshots, and users may each perceive different frames, creating moderation and forensic ambiguity.
- **Watch next:** Test decoder limits, cache behavior, scanner sampling, accessibility, browser consistency, and whether progressive-state inspection detects abuse.
