# ISO PDF spec is getting Brotli – ~20 % smaller documents with no quality loss

- Score: 138 | [HN](https://news.ycombinator.com/item?id=46717507) | Link: https://pdfa.org/want-to-make-your-pdfs-20-smaller-for-free/

### TL;DR

Brotli is being prepared for ISO 32000 as a new PDF stream filter, promising 15–25% smaller files without quality loss. iText embeds Google's pure-Java decoder in its core while isolating brotli4j's native encoder in an optional module behind a new compression-strategy interface. Current Brotli PDFs remain unreadable in Acrobat and most viewers until standardization and adoption. HN readers questioned the backward-compatibility claim, preferred faster zstd, and challenged Brotli's web-tuned default dictionary for archival documents.

### Comment pulse

- Compatibility skepticism → readers reject calling unreadable files future-proof and expect viewer adoption to take years.
- Algorithm choice → zstd advocates prioritize decoding speed; others ask whether a PDF-specific Brotli dictionary would improve compression.
- Embedded compression → supporters note stream-level codecs preserve random access and let different content use suitable formats.

### LLM perspective

- View: Format evolution needs staged capability negotiation, not optimistic labeling of incompatible files.
- Impact: Archives and recipients need fallback generation until reader support becomes measurable.
- Watch next: ISO wording, custom-dictionary evidence, zstd comparisons, and support in PDF.js, Poppler, PDFium, and Acrobat.
