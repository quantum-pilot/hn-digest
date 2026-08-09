# Fujifilm X RAW STUDIO webapp clone

- Score: 141 | [HN](https://news.ycombinator.com/item?id=47435081) | Link: https://github.com/eggricesoy/filmkit

### TL;DR

FilmKit is a beta, static web app that connects to Fujifilm cameras through WebUSB and PTP, letting the camera itself convert RAF files to JPEG. It manages on-camera and local presets, live previews, import/export, automatic preset detection, comparison, mobile use, and Linux access without installation. Reverse engineering combined existing projects with USB captures; a patch-based profile writer preserves unknown bytes. Only the X100VI is verified, and other models need compatibility captures. HN users welcomed the Linux/mobile option but reported both successful connections and model-specific profile failures.

### Comment pulse

- Camera-side conversion is the key distinction → FilmKit orchestrates Fujifilm’s processor rather than recreating proprietary color rendering in JavaScript.
- Compatibility remains the beta’s main risk → an X-T30 needed profile tweaks, while one GFX body was visible but could not connect.
- The workflow fills a real gap → users disliked Fujifilm’s native software and wanted fast recipe experimentation without a Windows installation.

### LLM perspective

- **View:** A client-only WebUSB design makes deployment simple, but browser and camera-protocol compatibility become the product boundary.
- **Impact:** Fujifilm owners gain preset management on Linux and Android while keeping image processing on trusted camera hardware.
- **Watch next:** Captures from older bodies, firmware-specific quirks, permission guidance, browser support, and a tested compatibility matrix.
