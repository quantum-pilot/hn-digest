# What is a color space?

- Score: 265 | [HN](https://news.ycombinator.com/item?id=45013154) | Link: https://www.makingsoftware.com/chapters/color-spaces-models-and-gamuts

### TL;DR

Digital color translates wavelengths and human perception into reproducible device values. A color space defines primaries, a white point, and a transfer function, giving RGB numbers specific meaning and bounding a gamut; a color model such as RGB, HSL, or OKLCH arranges those colors for manipulation. The article traces sRGB, CIE XYZ, Display P3, perceptual uniformity, interpolation, gamut mapping, gamma, bit depth, additive screens, subtractive printing, and ICC-based color management. Consistency ultimately requires conversion among content, application, operating-system, and display spaces.

### Comment pulse

- Readers praised the overview while adding printer profiles, paper-dependent lookup tables, soft proofing, HDR, ambient light, and color blindness.
- Practitioners emphasized that color-space conversion can lose information and that printed gamuts are often far smaller than modern displays.

### LLM perspective

- View: “RGB” alone is incomplete; identical channel values only identify a color once space, profile, and viewing pipeline are known.
- Impact: Ignoring color management produces unpredictable output precisely as displays, cameras, and editing workflows support wider gamuts.
- Watch next: Preserve embedded profiles, choose interpolation deliberately, test gamut mapping, and verify results across displays and print media.
