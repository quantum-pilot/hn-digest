# Investigating a Forged PDF

- Score: 282 | [HN](https://news.ycombinator.com/item?id=45381010) | Link: https://mjg59.dreamwidth.org/73317.html

### TL;DR

After a rental-deposit dispute, Matthew Garrett received a lease copy containing an addendum absent from his signed copy, despite both displaying the same RightSignature certificate checksums. He traced the discrepancy through PDF timestamps and IDs, Acrobat edit tags, renamed fonts—including a signature font added only after signing—and finally RightSignature's downloadable original base PDF, whose hash matched the certificate and lacked the addendum. A screenshare then exposed separate draft and completed records. Garrett says this strongly resembles post-signing forgery, while acknowledging his motive and liability analysis is inference.

### Comment pulse

- Readers urged reports to licensing, police, and fraud authorities, while Garrett said he would contact regulators and consult counsel.
- Commenters stressed that courts may need testimony from the signing provider or an expert, not merely technically persuasive metadata.

### LLM perspective

- View: Layered independent artifacts make a stronger provenance case than mutable PDF metadata alone.
- Impact: Signers need durable original access; platforms risk enabling deception when certificate pages survive document modification.
- Watch next: RightSignature's attestation, regulator response, expert preservation, agency explanation, and any civil or criminal proceeding.
