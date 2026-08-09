# A cryptography engineer's perspective on quantum computing timelines

- Score: 300 | [HN](https://news.ycombinator.com/item?id=47662234) | Link: https://words.filippo.io/crqc-timeline/

### TL;DR

Cryptography engineer Filippo Valsorda says recent algorithm and error-correction papers, plus expert warnings, changed his quantum-risk assessment: organizations should finish migrating asymmetric cryptography by 2029 rather than wait for certainty. He urges ML-KEM key exchange now, pure ML-DSA-44 authentication rather than complex hybrids, warnings for classical key exchange, and retirement of new non-post-quantum schemes. Symmetric 128-bit encryption remains adequate. HN skeptics accepted the risk framing but disputed skipping hybrid signatures and questioned whether authentication is as urgent as protecting recorded traffic.

### Comment pulse

- Key exchange is the immediate priority because recorded traffic can be decrypted later; signatures generally lack that retrospective exposure.
- The author argues rotation lead times make authentication urgent too, especially timestamps, identities, and ecosystems that could be forged or stranded.
- Pure ML-DSA simplifies migration — counterpoint: hybrids hedge against undiscovered classical flaws in newer post-quantum algorithms.

### LLM perspective

- **View:** Migration deadlines should follow credible worst-case risk, not median hardware forecasts.
- **Impact:** Protocol owners face larger signatures, downgrade hazards, compatibility breaks, and obsolete attestation roots.
- **Watch next:** Independent review of new resource estimates, 2029 roadmaps, and production evidence for ML-DSA interoperability.
