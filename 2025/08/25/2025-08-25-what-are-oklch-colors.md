# What are OKLCH colors?

- Score: 859 | [HN](https://news.ycombinator.com/item?id=45010876) | Link: https://jakub.kr/components/oklch-colors

### TL;DR

OKLCH represents color with lightness, chroma, and hue using the perceptually uniform OKLab space. Holding lightness and chroma while changing hue can produce palettes with more consistent perceived brightness than HSL, while changing lightness yields more predictable shades. It can express Display-P3 colors beyond sRGB, but also impossible colors that browsers must map into a device’s gamut. Modern browsers support it, with CSS fallbacks available. Gradients require care because circular hue interpolation may take colorful, unexpected, or out-of-gamut paths.

### Comment pulse

- Commenters recommended OKLab for many gradients because its straight interpolation avoids OKLCH’s long trips around the hue circle.
- Others stressed hue-dependent maximum chroma, display gamut limits, relative-color formulas, and visible hue shifts near gamut boundaries.

### LLM perspective

- View: OKLCH is an excellent authoring coordinate system, not a guarantee that every numerical operation produces a pleasing display result.
- Impact: Designers gain more systematic palettes, but must still inspect gamut mapping, gradients, and real screens.
- Watch next: Prefer explicit gamut checks and compare OKLCH, OKLab, and linear RGB interpolation for each visual goal.
