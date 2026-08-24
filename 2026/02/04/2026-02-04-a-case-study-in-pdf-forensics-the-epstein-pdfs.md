# A case study in PDF forensics: The Epstein PDFs

- Score: 237 | [HN](https://news.ycombinator.com/item?id=46886440) | Link: https://pdfa.org/a-case-study-in-pdf-forensics-the-epstein-pdfs/

### TL;DR

PDF Association researchers sampled the Justice Department’s first seven Epstein release datasets, examining file structure rather than document content. They found 4,085 mostly valid PDFs, correctly applied image-level redactions with no recoverable text in the sampled EFTA files, low-resolution bitmap conversion, weak OCR, incremental updates, and largely stripped metadata. Yet orphaned objects and comments exposed processing details, underscoring sanitization risk. Commenters focused on apparently simulated scans, preservation as files changed, stylometric privacy, and independently rerunning OCR; motives for scan-like rendering remained speculative.

### Comment pulse

- Forensics needs multiple tools → one pdfinfo ignored catalog version overrides, proving parser assumptions can produce false conclusions.
- Sanitization mostly worked → pixel redactions and metadata stripping held — counterpoint: orphaned objects and comments still leaked processing details.
- Scan simulation invites questions → identical skew suggests digital rendering, but commenters offered mundane signing workflows and unsupported concealment theories.

### LLM perspective

- View: Strong redaction outcomes and messy PDF internals coexist; neither establishes anything about the documents’ substantive contents.
- Impact: Archivists and investigators need revision-aware tooling, preserved originals, independent OCR, and caution distinguishing leakage from evidentiary significance.
- Watch next: Broader sampling, Dataset 8 analysis, archive diffs, comment-object review, OCR comparisons, and verified explanations for synthetic scan artifacts.
