# GPT-5o-mini hallucinates medical residency applicant grades

- Score: 185 | [HN](https://news.ycombinator.com/item?id=45581029) | Link: https://www.thalamusgme.com/blogs/cortex-core-clerkship-grades-and-transcript-normalization

- TL;DR
    - Thalamus’ Cortex tool parses medical school transcripts with OCR/NLP to normalize core clerkship grades. This season, programs flagged occasional inaccuracies—sometimes reading passes as fails. Thalamus says official PDFs/MSPEs are always available, outputs don’t drive filtering/scoring, and reviewers should verify; reported errors were corrected quickly. HN debates whether this is “hallucination” or OCR misread, warns about deploying LLMs in high‑stakes decisions, notes transcripts’ messy formats, and suggests safer workflows: abstention/uncertainty flags, screenshots of source text, structured data entry, or APIs instead of brittle PDF extraction.

- Comment pulse
    - LLMs in high‑stakes extraction misfire → publicize failures to counter “it’s fixed now”; vendor responded, but risk persists — counterpoint: nothing new; errors are inherent.
    - Transcripts are structurally nasty → multi‑column, nested tables, per‑school formats break OCR; mitigations: VLM‑assisted table repair, HTML over Markdown inputs, ensemble/consensus checks.
    - Manual verification undermines utility → users won’t recheck; better: show source snippets/screenshots, collect grades as structured fields, or require APIs; procurement–user incentives misalign.

- LLM perspective
    - View: Treat extraction as classification with abstain: per-field confidence thresholds, highlight deltas versus official PDFs, and forbid negative-grade auto-population.
    - Impact: Require program-level QA metrics: false-fail rate, human override rate, and time saved, reported by school and clerkship.
    - Watch next: Publish benchmark set of de-identified transcripts; run bake-offs across OCR/VLM stacks; announce timeline for structured-grade ingestion via ERAS.
