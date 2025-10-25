# Roc Camera

- Score: 519 | [HN](https://news.ycombinator.com/item?id=45690251) | Link: https://roc.camera/

- TL;DR
  - Roc Camera is a $399 Raspberry Pi 4–based, 16MP IMX519 device that records attested sensor data and ships ZK proofs so photos can be verified via an SDK. It promises tamper-resistance and ‘real’ capture; batch 2 ships in 2–3 weeks. HN liked the entrepreneurial effort but argued authenticity isn’t the core problem—photography’s cultural value is. Many panned the hardware (slow boot, no sleep, tiny sensor, export missing). Others questioned ZK versus C2PA, analog-hole limits, and potential lock‑down; some defended attestations for chain‑of‑custody contexts.

- Comment pulse
  - Authenticity isn’t the problem → Photos are commodified; audiences don’t care about provenance. Focus on personal joy; some avoid cameras over surveillance vibes.
  - Hardware misses basics → RPi lacks instant-on/sleep; tiny IMX519. Prefer 1-inch sensors, low-power SoCs; OneInchEye/Alice cited — counterpoint: tuned Buildroot RPi can boot fast.
  - ZK proofs questioned → C2PA favored; scant tech detail; analog hole persists; lock‑down feared — counterpoint: attestations can coexist with user firmware and aid chain‑of‑custody.

- LLM perspective
  - View: Verifiable capture is niche: journalism, legal evidence, scientific logging—not consumer social sharing.
  - Impact: Success likely depends on interoperability with C2PA and open SDKs, plus better sensors and fast, low‑power hardware.
  - Watch next: Publish proofs/specs, third‑party audits, anti‑analog tactics (depth/GPS/time), boot/sleep benchmarks, sample RAWs, export UX, and court admissibility tests.
