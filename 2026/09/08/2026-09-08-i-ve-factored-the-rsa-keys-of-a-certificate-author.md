# I've factored the RSA keys of a Certificate Authority from the 90s

- Score: 498 | [HN](https://news.ycombinator.com/item?id=49604637) | Link: https://mcpherrin.ca/2026/09/07/rsa.html

### TL;DR

Matthew McPherrin extracted historical browser trust roots and factored two 512-bit E-Certify RSA certificate keys from Netscape 4.51 using CADO-NFS on a Ryzen 9 5950X, taking 32 and 29 hours. Reconstructing the private keys let him issue certificates accepted by a deliberately time-shifted Netscape VM through a custom legacy TLS server. The exercise exposes how export-era constraints produced weak trust anchors, but it does not compromise modern PKI or establish practical attacks against 1024- or 2048-bit RSA. Commenters supplied historical context and debated future decryption risks.

### Comment pulse

- A former Netscape certificate manager said export-grade weakness was known and government-required, while root slots also faced commercial pressure.
- Retrocomputing users valued legacy TLS support—counterpoint: deploying custom cryptography requires strong isolation and careful review.
- Commenters worried about harvested ciphertext, but offered no evidence that this 512-bit result translates directly to current key sizes.

### LLM perspective

- View: This is a successful archaeological demonstration of obsolete trust, not a break of contemporary RSA deployments.
- Impact: Preserved software becomes testable evidence of how policy and commercial choices shaped early web security.
- Watch next: Inventory surviving weak roots, document compute precisely, isolate demonstrations, and accelerate migration from still-deployed legacy keys.
