# What's up with all those equals signs anyway?

- Score: 603 | [HN](https://news.ycombinator.com/item?id=46868759) | Link: https://lars.ingebrigtsen.no/2026/02/02/whats-up-with-all-those-equals-signs-anyway/

### TL;DR
Old leaked emails full of random “=” characters aren’t encryption, OCR junk, or secret codes; they’re fallout from a 1990s email encoding hack called quoted-printable. Email systems used “=CRLF” at line ends to split long lines and “=XX” hex sequences (e.g., “=C2=A0”) to represent non-ASCII characters. Whoever processed these archives stripped or converted line endings and then tried to “decode” by hand, mangling the continuation markers and character codes, so stray equals signs and missing letters show up in modern dumps.

---

### Comment pulse
- Lars’ credibility → Longtime Gnus author and email-parser expert; commenters recall him as a minor celebrity among Emacs users at the University of Oslo.  
- Naive parsing is dangerous → Hand-rolled quoted-printable decoding equals regex-parsing HTML: seems fine until edge cases quietly corrupt high‑stakes data.  
- Why line-length limits? → SMTP is line-based, built for tiny-memory mainframes; RFCs cap line length and encourage soft breaks, still shaping email formats today.

---

### LLM perspective
- View: This is a classic “leaky abstraction” story: transport encodings resurfacing decades later as visible garbage in public records.  
- Impact: Anyone building archives, FOIA tools, or court-document pipelines must treat legacy email as a binary protocol, not editable text.  
- Watch next: Robust, open-source email-normalization libraries and test suites for archives handling MIME, line endings, and character sets end-to-end.
