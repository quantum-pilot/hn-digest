# Firefox 153 available with support for Vulkan video decoding, JPEG-XL

- Score: 234 | [HN](https://news.ycombinator.com/item?id=48978835) | Link: https://www.phoronix.com/news/Firefox-153-Downloads

### TL;DR
Firefox 153 is the new Extended Support Release, notable for adding initial Vulkan Video hardware decoding on Linux, aiming to replace fragile VA‑API setups, especially on Nvidia and embedded GPUs. The release also improves PDFs, enables HDR video on Windows, and exposes experimental JPEG‑XL via Firefox Labs. HN commenters focus on Linux video acceleration reliability and power use, and note that Firefox’s now‑local translation features are becoming viable alternatives to Chrome’s integrated translator.

### Comment pulse
- Vulkan decoding on Linux seen as big win for Nvidia and flaky VA-API setups → more robust, sandboxed acceleration—counterpoint: Intel/AMD users may see little improvement.  
- Hardware video blocks meant to save power; some measure dGPU acceleration using more energy than CPU or iGPU due to high power states.  
- Firefox’s on-device page and selection translation now praised as good enough for daily use, balancing privacy with somewhat weaker quality than cloud services.  

### LLM perspective
- View: Vulkan Video makes browser media pipelines less vendor-specific, easing support across Nvidia, Intel, AMD, and quirky embedded GPUs.  
- Impact: Linux desktop users on Nvidia benefit most; enterprises gain from ESR stability plus standardized, testable acceleration and emerging JPEG-XL workflows.  
- Watch next: Watch for per-GPU power benchmarks, VA-API deprecation discussions, and JPEG-XL moving from Labs flag to default in mainstream builds.
