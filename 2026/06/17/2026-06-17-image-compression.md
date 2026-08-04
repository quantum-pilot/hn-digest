# Image Compression

- Score: 153 | [HN](https://news.ycombinator.com/item?id=48522927) | Link: https://www.makingsoftware.com/chapters/image-compression

### TL;DR

The piece introduces image compression as the art of exploiting limits in human vision to reduce file size without visibly ruining an image. HN discussion broadened this into format tradeoffs: QOI favors a tiny specification and very fast lossless coding, JPEG XL combines lossy, lossless, HDR, and RAW-container use, while AVIF often beats older formats for compact delivery. Commenters stressed that adoption depends on browser, tooling, metadata, and computational support, not compression ratios alone; WebP may still win for lossless work.

### Comment pulse

- Simple codecs retain appeal → QOI’s one-page specification and roughly 300-line reference implementation deliver PNG-like lossless sizes with much faster coding.
- Feature leadership does not ensure adoption → JPEG XL’s metadata friction and JPEG 2000’s niche history show ecosystem support can outweigh technical breadth.
- Modern delivery choice remains workload-specific → commenters favor AVIF’s ratios, while others say WebP remains superior in lossless mode.

### LLM perspective

- **View:** Compression formats compete on deployment friction and decoding cost as much as visual quality or file size.
- **Impact:** Frontend teams can choose per asset class, retaining WebP for lossless images and testing AVIF or JPEG XL elsewhere.
- **Watch next:** Track default browser enablement, metadata interoperability, encode/decode benchmarks, and real-world quality at matched sizes.
