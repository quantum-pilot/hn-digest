# Replace IBM Quantum back end with /dev/urandom

- Score: 331 | [HN](https://news.ycombinator.com/item?id=47897647) | Link: https://github.com/yuvadm/quantumslop/blob/25ad2e76ae58baa96f6219742459407db9dd17f5/URANDOM_DEMO.md

## TL;DR
A Bitcoin-sponsored “largest quantum ECC attack” contest awarded 1 BTC to a 17‑bit elliptic-curve key recovery claimed to use IBM Quantum hardware. Yuval Adam shows that swapping the IBM backend for `/dev/urandom`—pure uniform randomness—while leaving all other code intact reproduces the same success rates, including the prize‑winning run. The extraction logic simply tests many random candidate keys until one verifies, which is overwhelmingly likely with the chosen parameters. This indicts the contest’s validation and benchmark design, not quantum computing itself.

---

## Comment pulse
- Small-instance Shor benchmarks are flawed → noisy quantum hardware behaves like RNG, and verification alone can “succeed for the wrong reason” on tiny keys.  
- Contest vetting criticized → winner appears to lack quantum background; code looks “vibe coded,” reinforcing that organizers didn’t enforce proof of genuine quantum advantage.  
- Some ask if quantum runs were faster than random search → others reply that 17‑bit ECC is trivial classically, so any “speedup” is meaningless.

---

## LLM perspective
- View: This is a textbook case of missing classical baselines and controls when claiming quantum advantage, especially on toy cryptographic problems.  
- Impact: Quantum contests, industry demos, and reviewers must demand side‑by‑side classical benchmarks and ablation tests like “replace device with RNG.”  
- Watch next: Better metrics (advantage vs best classical), stricter challenge rules (size, noise models), and independent audits of high‑profile “quantum breakthrough” claims.
