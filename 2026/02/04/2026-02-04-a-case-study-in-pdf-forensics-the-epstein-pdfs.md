# A case study in PDF forensics: The Epstein PDFs

- Score: 237 | [HN](https://news.ycombinator.com/item?id=46886440) | Link: https://pdfa.org/a-case-study-in-pdf-forensics-the-epstein-pdfs/

### TL;DR
The article forensically inspects the DOJ’s “Epstein Files Transparency Act” PDFs, showing they are mostly well-formed and that the EFTA datasets 01–07 are correctly, irreversibly redacted—contrary to viral claims based on older, separately released DOJ PDFs with flawed “black box” redactions. DOJ uses a pipeline that converts pages to low‑resolution bitmaps, strips most metadata, and adds Bates numbers via incremental updates, but leaves some comments and hidden Info dictionaries. OCR is poor, inviting community re‑OCR; HN commenters dive into fake scans, stylometry, and independent archiving/OCR.

---

### Comment pulse
- Simulated scans are easy → shared ImageMagick script adds skew/noise to born‑digital PDFs; commenters note agencies and individuals routinely “fake-scan” signed documents.  
- Stylometry can deanonymize → prior HN tool matched users by n‑grams; some doubt uniqueness across populations — counterpoint: empirical demos on HN were convincing.  
- Archiving and reanalysis matter → users track ZIPs temporarily disappearing, worry about re-redactions, and one is batch‑OCRing ~500k page images with olmocr‑2‑7b.

---

### LLM perspective
- View: Treat PDFs as executable-like artifacts: multiple layers, legacy quirks, and hidden structures that naive tools routinely misinterpret.  
- Impact: Any organization doing public disclosures needs standardized, testable redaction pipelines plus independent tool cross-checks before release.  
- Watch next: Open redaction/forensics test suites, better OCR re-processing of EFTA files, and policy updates distinguishing old flawed vs new robust DOJ workflows.
