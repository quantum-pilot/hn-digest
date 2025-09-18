# What is a color space?

- Score: 265 | [HN](https://news.ycombinator.com/item?id=45013154) | Link: https://www.makingsoftware.com/chapters/color-spaces-models-and-gamuts

- TL;DR
  Primer on digital color: how device-independent spaces (CIE XYZ/Lab, Oklab) relate to device spaces (sRGB, display gamuts), why gamut limits and perceptual uniformity matter, and how profiles convert between them. HN adds the messy reality: printers need ICC LUTs per paper yet still miss vivid colors like purples; soft proofing previews losses. HDR complicates pipelines and capture; displays beat print contrast by orders of magnitude. Tools like colour-science and high-bit-depth workflows help, but transforms aren’t perfectly reversible.

- Comment pulse
  - Printing needs ICC profiles with big LUTs per paper; tiny gamut vs displays makes purples hard; soft proofing maps device-independent color to preview losses.
  - HDR pipelines are messy: input/processing/output mismatches, OSs often capture SDR; displays reach 10+ stops, prints ~5—counterpoint: soft-proof setups approximate target viewing conditions.
  - Perceptual spaces matter: Oklab eases uniform edits; CIE-XYZ separates luminance/chroma; Colour Science tools convert spectra to RGB; many transforms lose information.

- LLM perspective
  - View: Color pipelines juggle device dependence, gamut mapping, and perception; profiles and HDR make correctness context-specific, not absolute.
  - Impact: Developers of imaging, web, and print tools must expose profiles, soft proofing, and HDR-aware paths; defaults should minimize surprises.
  - Watch next: Standardized HDR-in-web pipelines, OS-level HDR capture APIs, better gamut-mapping presets, and broader adoption of Oklab/OKLCH in editors and CSS.
