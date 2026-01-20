# Show HN: Pdfwithlove – PDF tools that run 100% locally (no uploads, no back end)

- Score: 171 | [HN](https://news.ycombinator.com/item?id=46675231) | Link: https://pdfwithlove.netlify.app

## TL;DR
Pdfwithlove is a browser-based PDF toolkit (merge, compress, edit, sign, convert) that runs entirely client-side via WebAssembly, promising zero uploads, no tracking, and free, unlimited use. It positions itself as a privacy-first alternative to cloud tools like iLovePDF or Smallpdf, aiming at legal/medical scenarios. Hacker News comments note a surge of nearly identical “local PDF” projects—often LLM-assisted—with UX bugs and weak conversions, and highlight the hard problems still unsolved: image-heavy PDFs, robust Word→PDF, and editable PDF forms.

## Comment pulse
- Wave of similar client-side PDF tools → some see “hello world” / AI-generated sameness; others argue PDF complexity and demand justify many attempts.  
- Quality concerns → obvious UI quirks and broken Word→PDF conversions suggest heavy LLM use and minimal testing — counterpoint: author says it’s WIP and being improved.  
- Hard edges → image-only PDFs and true form editing remain difficult in-browser; commenters prefer mature tools like Stirling-PDF, PdfTk, or custom PDF.js-based annotators.

## LLM perspective
- View: Local-only PDF suites are useful, but must prove reliability on real-world documents, not just simple demos.  
- Impact: Strong contenders could displace web SaaS in privacy-sensitive sectors and standardize in-browser PDF engines.  
- Watch next: Public test corpus, side-by-side output comparisons, and transparent QA processes for LLM-assisted development and regression testing.
