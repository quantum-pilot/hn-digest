# Libre Barcode Project

- Score: 272 | [HN](https://news.ycombinator.com/item?id=48681949) | Link: https://graphicore.github.io/librebarcode/

### TL;DR

Libre Barcode provides fonts for rendering Code 39, Code 128, and EAN/UPC barcodes, optionally with human-readable text. Because Code 128 needs start, stop, checksum, and character-set decisions, the site includes an encoder that transforms plain input into the glyph sequence the font expects. HN liked the accessibility but warned that fonts can produce unreliable output through scaling or printer rasterization; native printer commands or correctly sized SVG/bitmaps are safer. Discussion also covered Code 39’s missing checksum, programmable font shapers, and configuration barcodes for scanners.

### Comment pulse

- Output geometry matters as much as encoding → barcode modules must align to printer resolution; arbitrary font scaling can blur or distort bars.
- Code 128’s hard part precedes drawing → encoders must choose character-set switches and calculate control characters before any font or SVG renders.
- Fonts are becoming programmable runtimes → HarfBuzz’s WASM shaper can support arbitrary logic, inspiring impractical but educational QR-in-font experiments.

### LLM perspective

- **View:** A barcode font is a presentation layer, not a full encoder; separating those roles prevents subtle validity failures.
- **Impact:** Designers gain portable typography, while logistics users still need scanner testing across printers, sizes, media, and lighting.
- **Watch next:** Publish scan-grade test vectors, minimum module sizes, checksum behavior, printer guidance, and automated verification across supported symbologies.
