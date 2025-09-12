# The MacBook has a sensor that knows the exact angle of the screen hinge

- Score: 1011 | [HN](https://news.ycombinator.com/item?id=45158968) | Link: https://twitter.com/samhenrigold/status/1964428927159382261

- TL;DR
  - MacBooks include a hinge-angle sensor to report exact lid position. Comments highlight Apple’s serialization/calibration tying the sensor to the logic board—seen as lock‑in—versus arguments about theft deterrence, sleep/security bypass prevention, and manufacturing integrity checks. The sensor enables features like Desk View keystone correction and nuanced sleep/auto‑lock behavior; it’s been present since ~2019. Many laptops have similar sensors and Linux can expose them; Apple doesn’t offer a public API. Some lament right‑to‑repair limits; others share playful repurposings.
  - Content unavailable; summarizing from title/comments.

- Comment pulse
  - Apple serializes the lid sensor → replacement needs Apple calibration; critics call it lock‑in — counterpoint: mitigates theft, sleep bypass, and enforces cryptographic manufacturing integrity.
  - Why the sensor exists → supports Desk View keystone, precise sleep/auto‑lock, “privacy ducking”; pre‑dates ultra‑wide cameras, so not exclusive to Desk View.
  - Not uniquely Apple → other laptops expose hinge angle via Linux IIO; main difference is Apple lacks a public API and restricts third‑party repairs.

- LLM perspective
  - View: Component serialization can enhance security yet harm repair; user‑authorized re‑pairing via Secure Enclave would balance both.
  - Impact: Independent repair shops and refurbishers lose capability; anti‑theft improves; OS features depend more on fine‑grained device telemetry.
  - Watch next: EU right‑to‑repair enforcement, Apple self‑service calibration expansion, standardized hinge‑angle APIs across platforms, and teardown verification of sensor pairing.
