# Show HN: WalletWallet – create Apple passes from anything

- Score: 254 | [HN](https://news.ycombinator.com/item?id=46345745) | Link: https://walletwallet.alen.ro/

### TL;DR

*The supplied product page is brief, and its privacy implementation cannot be verified from the input.* WalletWallet claims to create free Apple Wallet passes in a browser without signup or installation. Users scan or upload a QR code, or enter barcode data manually, then choose titles, labels, values, format, and color before downloading a standard .pkpass. Commenters liked the one-off browser workflow but requested source code, questioned where cryptographic signing occurs, and noted that “processed locally” may not cover pass generation if a hosted certificate signs the file.

### Comment pulse

- Loyalty-card users want visible membership numbers alongside barcodes and fewer dedicated card-management applications.
- Barcode scanning is mature without generative AI; commenters challenged framing manual entry as the safer alternative.

### LLM perspective

- View: Convenience is clear, but the page's privacy promise needs an auditable signing explanation.
- Impact: Barcode and membership data may be sensitive even when the interface appears client-side.
- Watch next: Publish source, document certificate boundaries, expose network behavior, and test camera, barcode, and pass compatibility.
