# Video Game Blurs (and how the best one works)

- Score: 277 | [HN](https://news.ycombinator.com/item?id=45114498) | Link: https://blog.frost.kiwi/dual-kawase/

TL;DR
Walkthrough of real-time blur methods in WebGL, from box and Gaussian to Dual Kawase. It explains kernels, UV sampling, texture taps, performance costs, edge handling, and artifacts from increasing sample distance. Dual Kawase achieves wide-radius, bloom-friendly blur by iteratively downsampling and upsampling with small kernels, leveraging bilinear filtering to minimize bandwidth—ideal for UI and mobile. HN praised the interactive demos; flagged proper Gaussian weighting via integration for small sigmas; debated bokeh DOF vs Gaussian, with the author noting Kawase still wins at high resolutions.

Comment pulse
- Gaussian weights need integral over pixel area → erf-based coefficients avoid bias at small radii.
- Modern GPUs enable bokeh DOF looks more natural → disk-shaped aperture better matches human vision — counterpoint: DK remains efficient, especially on mobile and 4K.
- Compute-shader blur without textures sought → shared-memory pipeline avoids DRAM, but Kawase’s odd sample positions fight subgroup intrinsics limited to even lanes.

LLM perspective
- View: Dual Kawase is a smart bandwidth hack: pyramid passes trade taps for resolution, exploiting bilinear hardware.
- Impact: Best-fit for bloom, frosted glass, and GUIs on mobile/VR; full-frame Gaussian remains expensive at 4K+.
- Watch next: Benchmark DK vs separable Gaussian and compute-shader variants; test cache sensitivity, subgroup tricks, and HDR precision on iOS/Android.
