# Keys Not Included: recovering the signing keys for US driver's license barcodes

- Score: 282 | [HN](https://news.ycombinator.com/item?id=49735930) | Link: https://ryan.science/blog/keys-not-included

### TL;DR

Ryan Fahey reverse-engineered how New York, Virginia, and North Carolina sign AAMVA PDF417 license data, then recovered their ECDSA public verification keys by comparing multiple signatures over reconstructed messages. This enables browser-side detection of altered barcode fields without exposing private signing keys; California already documents a different standards-based system. The protection remains incomplete because barcodes omit photos, so copied genuine data can authenticate on a counterfeit card. HN praised public verification while criticizing misleading “signing key” terminology and emphasizing front-to-back identity checks.

### Comment pulse

- Public keys should be published → verification depends on broad access, while disclosure provides no ability to create a valid state signature.
- Terminology matters → commenters objected that the recovered material is a public verification key, not the secret key that produced signatures.
- Barcode authenticity is not person authentication → valid signed text can be copied onto another card because the photo is absent and unsigned.

### LLM perspective

- View: Undocumented verification converted deployed cryptography into obscurity; recovering public keys restores only the checking function vendors should expose.
- Impact: Scanners can reject altered fields, but operators still need inspection or stronger credentials to bind data to the holder.
- Watch next: Vendor documentation, keys for remaining CBN states, revocation mechanisms, and wider adoption of photo-bearing mDL or NFC credentials.
