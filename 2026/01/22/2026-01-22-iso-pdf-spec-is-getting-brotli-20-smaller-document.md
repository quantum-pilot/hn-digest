# ISO PDF spec is getting Brotli – ~20 % smaller documents with no quality loss

- Score: 138 | [HN](https://news.ycombinator.com/item?id=46717507) | Link: https://pdfa.org/want-to-make-your-pdfs-20-smaller-for-free/

## TL;DR
PDF has used Deflate since 1996; the PDF Association is now adding Brotli as an official `/BrotliDecode` filter, promising roughly 15–25% smaller files with no quality loss. iText implemented this by embedding Google’s Java decoder for reading and adding an optional Brotli-encoder module using a pluggable compression strategy interface. Today, Brotli PDFs won’t open in most viewers, so adoption is explicitly experimental and forward-looking—HN commenters question the backward-compatibility story and argue zstd or better tuning might be wiser.

## Comment pulse
- Brotli vs zstd → Many argue zstd is faster and more suitable for read-heavy formats; Brotli without a PDF-specific dictionary seems like an odd choice.  
- Compatibility concern → Marketing about “ahead of their time” files clashes with claims of strict backward-compatibility; people expect a decade-long lag before safe broad use.  
- Why compress inside PDF? → Internal compression allows per-stream algorithms and random access; filesystem/network compression is rare or tuned for different tradeoffs.

## LLM perspective
- View: Brotli-in-PDF is a realistic, incremental win, but the choice over zstd and dictionary design deserves more open benchmarking.  
- Impact: PDF SDKs and viewers must ship new filters; archives and governments will likely lag until compatibility is boringly universal.  
- Watch next: Results of PDF-specific dictionary experiments, comparative Brotli/zstd studies on real corpora, and adoption in Acrobat, pdf.js, Poppler, and PDFium.
