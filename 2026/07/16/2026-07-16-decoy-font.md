# Decoy Font

- Score: 359 | [HN](https://news.ycombinator.com/item?id=48936584) | Link: https://www.mixfont.com/experiments/decoy-font

### TL;DR

Decoy Font is a downloadable TTF that overlays two signals in each glyph: sharp outlines form a decoy, while blurred low-frequency mass carries the intended letter. Up close, viewers and vision models tend to read the outlines; from farther away, while squinting, or after downsizing, the hidden message emerges. Screenshots reportedly fooled several frontier models, but the author calls it a deterrent, not a guarantee. Asking models to seek another message or applying simple low-pass processing can reveal it, making this optical camouflage rather than encryption.

### Comment pulse

- Prompt context changes performance → models often returned only the outline text until told a second message existed, after which some decoded both.
- Scale selects the channel → downsizing acts as a low-pass filter, suppressing outlines and exposing the blurred message to humans and models.
- Utility divided commenters → some saw little security value — counterpoint: others proposed camera evasion, image-only messaging, art, or recognition benchmarks.

### LLM perspective

- **View:** The font exploits preprocessing assumptions, not intelligence limits; resolution, prompting, and frequency decomposition determine which message wins.
- **Impact:** It can delay naive OCR or scraping, but treating it as privacy protection risks exposing supposedly hidden text.
- **Watch next:** Benchmark multiple resolutions, compression levels, prompts, OCR engines, languages, accessibility tools, and automated dual-frequency detection.
