# Firefox 153 available with support for Vulkan video decoding, JPEG-XL

- Score: 234 | [HN](https://news.ycombinator.com/item?id=48978835) | Link: https://www.phoronix.com/news/Firefox-153-Downloads

### TL;DR

Firefox 153 is the new Extended Support Release and adds initial Vulkan Video decoding, giving Linux users a cross-vendor alternative to VA-API—especially relevant to NVIDIA, whose drivers lack native VA-API support. The release also adds PDF improvements, Windows HDR playback, and opt-in JPEG-XL support through Firefox Labs. Hacker News welcomed another hardware-decoding path after fragile Linux setups, but questioned benefits for Intel and AMD, where VA-API already works well. Measured power use emerged as the key caveat: a discrete GPU can consume more than software or integrated decoding.

### Comment pulse

- Vulkan could stabilize NVIDIA acceleration → users describe Firefox’s VA-API path as fragile — counterpoint: Intel and AMD users may gain little.
- Hardware decoding optimizes energy, not necessarily speed → dedicated blocks usually save power, but waking a discrete GPU can reverse the result.
- Configuration remains part of correctness → backend selection, sandbox constraints, driver choice, performance states, and environment flags can determine whether acceleration helps.

### LLM perspective

- **View:** Portable APIs reduce fragmentation, but measurements must show whether each driver-device combination improves playback.
- **Impact:** NVIDIA Linux users gain a first-party route beyond compatibility layers; ESR organizations get the feature on a stability-focused baseline.
- **Watch next:** Benchmark CPU load, total-system power, battery life, dropped frames, codec coverage, sandbox behavior, and automatic backend selection.
