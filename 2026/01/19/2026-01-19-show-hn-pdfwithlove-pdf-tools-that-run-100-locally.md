# Show HN: Pdfwithlove – PDF tools that run 100% locally (no uploads, no back end)

- Score: 171 | [HN](https://news.ycombinator.com/item?id=46675231) | Link: https://pdfwithlove.netlify.app

### TL;DR

Pdfwithlove presents a free browser-only suite for merging, splitting, editing, compressing, signing, watermarking, and converting PDFs, claiming WebAssembly keeps documents in memory without uploads, tracking, a file database, or usage limits. Its pitch is privacy versus cloud services, especially for sensitive documents. HN noted a crowded field of nearly identical client-side PDF tools and challenged the product’s testing: one commenter reported broken Word conversion, while the author called it unfinished. Discussion also highlighted difficult scan compression, forms support, and absent source code.

### Comment pulse

- Saturation → commenters list many recent browser PDF suites and similar interfaces — counterpoint: PDF demand and format complexity still create useful niches.
- Quality gap → users report editing quirks and failed Office conversion; the author says LLM assistance accelerated development and testing will continue.
- Hard cases → image-heavy scans need aggressive resampling, while editable forms are complex, inconsistent, and easy to corrupt.

### LLM perspective

- View: Local execution improves privacy architecture, but it does not establish correctness, security, or document fidelity.
- Impact: Sensitive-document users gain convenience only if conversions preserve content and browser memory handling matches privacy claims.
- Watch next: Add public compatibility fixtures, end-to-end tests, browser profiling, form support, and precise source-code disclosure.
