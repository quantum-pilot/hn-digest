# O(x)Caml in Space

- Score: 225 | [HN](https://news.ycombinator.com/item?id=48147058) | Link: https://gazagnaire.org/blog/2026-05-14-borealis.html

### TL;DR

Parsimoni’s Borealis, a pure-OCaml CCSDS stack, booted on a shared low-Earth-orbit payload on April 23. It treats file uplink/downlink as a delay-tolerant network, wrapping commands and telemetry in encrypted, authenticated, replay-resistant bundles; post-quantum over-the-air key rotation is planned. OxCaml stack-allocation annotations cut laptop-measured p99.9 dispatch latency from 29 ns to 9 ns and minor GCs from 394 to zero over 25.6 million packets. HN welcomed the typed, low-jitter design but challenged its novelty and debated protocol and language choices.

### Comment pulse

- Historical priority was corrected → GHGSat-D used OCaml in 2016, and its mostly OCaml payload stack reportedly now spans 16 satellites.
- CCSDS divides protocol opinion → critics prefer TLS-derived systems — counterpoint: spacecraft latency, legacy compatibility, and existing tooling make CCSDS difficult to replace.
- Language choice is sociotechnical → OCaml’s development model remains attractive, but hiring and training pressure pushes new components toward Rust.

### LLM perspective

- **View:** Layered assurance matters: types constrain logic, cryptographic envelopes survive hostile routing, and interop tests cover specification gaps.
- **Impact:** Hosted-payload tenants gain routing-path confidentiality, while the shared Linux kernel and unprotected master key remain critical dependencies.
- **Watch next:** Validate OTAR in orbit, benchmark flight hardware, fuzz malformed bundles, and demonstrate fleet updates, isolation, and attestation.
