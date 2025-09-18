# What are OKLCH colors?

- Score: 859 | [HN](https://news.ycombinator.com/item?id=45010876) | Link: https://jakub.kr/components/oklch-colors

- TL;DR
  - OKLCH is a perceptually uniform CSS color model (Lightness, Chroma, Hue) built on OKLab, making consistent palettes, predictable tints/shades, and wide‑gamut (P3) colors easier than HSL/RGB. It’s broadly supported with @supports fallbacks and relative color formulas. HN praises the intro, but flags gradient pitfalls: prefer OKLab interpolation to avoid circular‑hue detours and out‑of‑gamut darkening; linearize sRGB before mixing; and expect cyan shifts near gamut limits. Many practitioners use OKLCH for UI controls and OKLab for the math.

- Comment pulse
  - For gradients, OKLab beats OKLCH → straight‑line interpolation avoids circular‑hue detours and edge‑of‑gamut artifacts; Tailwind v4 adopted OKLab. — counterpoint: linearize sRGB also mitigates issues.
  - Use OKLCH as human‑friendly controls → L/C/H sliders map intuitively; compute in OKLab for mixing; CSS relative colors enable formulas like oklch(from var(...) calc(...)).
  - Example debate: OKLCH blue tints shift cyan → saturation‑invariant lightness meets gamut limits; displays differ; some saw no green cast, suggesting calibration differences.

- LLM perspective
  - View: Treat OKLCH as a design-space; perform math in OKLab or linear RGB to avoid gamut and interpolation pitfalls.
  - Impact: Front-end tooling and design systems will consolidate on OKLab interpolation with OKLCH inputs; fewer hardcoded palettes via relative color functions.
  - Watch next: Browser defaults for gradient spaces, standardized in-gamut mapping algorithms, P3+ display adoption, and practical max‑chroma utilities in CSS tooling.
