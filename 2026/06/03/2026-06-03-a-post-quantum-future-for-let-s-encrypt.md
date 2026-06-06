# A Post-Quantum Future for Let's Encrypt

- Score: 213 | [HN](https://news.ycombinator.com/item?id=48385114) | Link: https://letsencrypt.org/2026/06/03/pq-certs

## TL;DR

Let’s Encrypt plans to adopt Merkle Tree Certificates (MTCs) as its main path to post‑quantum‑safe authentication. Conventional post‑quantum signatures (like ML‑DSA) would bloat TLS handshakes to >10 KB and break or slow many real‑world connections. MTCs batch certificates into Merkle trees and let browsers cache signed “landmarks,” keeping handshakes small while making certificate transparency intrinsic. Let’s Encrypt aims for MTC staging in 2026 and production in 2027; meanwhile, servers should already enable hybrid post‑quantum key exchange.

## Comment pulse

- Quantum risk is debated: some see PQ as cheap insurance against “store-now, decrypt-later”; others argue symmetric ciphers like AES remain safe even with quantum.  
- MTCs praised for efficiency and transparency, but skeptics fear untested designs replacing mature tooling, and suggest layering old+new—counterpoint: extra complexity may outweigh gains.  
- Downsides raised: servers and clients must handle landmark syncing; non‑browser tools may fall back to large standalone certs, blunting MTC size wins in many environments.  

## LLM perspective

- View: Moving signature bulk out of the handshake mirrors web caching: background sync plus compact proofs instead of heavyweight crypto.  
- Impact: ACME clients, TLS libraries, and non‑browser tools must be updated or risk degraded performance via oversized standalone certificates.  
- Watch next: MTC standardization progress, browser landmark-distribution designs, and measurements of handshake failures on flaky or air‑gapped networks.
