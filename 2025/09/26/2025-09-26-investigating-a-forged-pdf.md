# Investigating a Forged PDF

- Score: 282 | [HN](https://news.ycombinator.com/item?id=45381010) | Link: https://mjg59.dreamwidth.org/73317.html

- TL;DR
    - Matthew Garrett says a rental agency sent a “revised” lease PDF adding an addendum shifting security‑deposit liability to the landlord—after he’d signed. He forensically showed post‑signing tampering: differing PDF modification time/ID1, Acrobat “touchUp” edits and font renames affecting the e‑signature font, and, decisively, retrieving RightSignature’s base.pdf whose hash matched the certificate and lacked the addendum. A screenshare exposed a draft vs completed mismatch. HN urges criminal referrals, legal action, and stronger notarization/digital‑signature practices.

- Comment pulse
    - Treat as criminal fraud → report to CA e-crime, FBI IC3, SF financial crimes; pursue civil damages with contingency counsel; potential class risk.
    - Platform must attest → RightSignature, as the trusted third party, should testify which version is original; judges may ignore technical forensics.
    - Prevention → use digitally signed documents/invoices (Factur‑X/ZUGFeRD); keep multiple fully executed copies at signing — counterpoint: UX gaps in e-sign tools enable confusion.

- LLM perspective
    - View: Treat e-signed PDFs as code; verify cryptographic signatures, PDF IDs, timestamps, and fetch original assets (base PDFs) before negotiating.
    - Impact: Property managers and SaaS e-sign vendors face scrutiny; expect policy requiring verifiable audit trails and per-document public-key signatures.
    - Watch next: Vendor fixes exposing base files, notarization APIs, regulator or AG actions; any class filings or CFPB/AG landlord enforcement.
