# Replace IBM Quantum back end with /dev/urandom

- Score: 331 | [HN](https://news.ycombinator.com/item?id=47897647) | Link: https://github.com/yuvadm/quantumslop/blob/25ad2e76ae58baa96f6219742459407db9dd17f5/URANDOM_DEMO.md

### TL;DR

A 59-line patch replaces an IBM quantum processor with `/dev/urandom` in a prize-winning elliptic-curve key-recovery submission while leaving its circuit-building and extraction pipeline intact. Random data still recovers small keys and the flagship 17-bit key in two of five trials because 20,000 uniform candidates plus a classical verifier have a 26.43% theoretical chance of finding the answer. The result challenges the claimed quantum contribution, not quantum computing. Hacker News blamed tiny benchmarks, noisy circuits, and weak prize validation, while noting that outperforming random sampling could still demonstrate real signal.

### Comment pulse

- Small ECDLP cases are poor quantum benchmarks because random samples can succeed quickly, especially when deep noisy circuits already resemble randomness.
- Project Eleven’s 1 BTC award exposed inadequate validation; replacing the backend should have been an elementary control experiment.
- The demonstration proves this recovery was classical — counterpoint: statistically faster-than-random hardware results could still indicate genuine quantum contribution.

### LLM perspective

- **View:** A verifier confirms candidate correctness, not the mechanism that produced it; attribution requires controlled baselines.
- **Impact:** Quantum prize organizers need preregistered metrics and null models before treating tiny-key recovery as cryptanalytic progress.
- **Watch next:** Repeated hardware-versus-random trials, confidence intervals, larger curves, shot-efficiency comparisons, and the prize sponsor’s response.
