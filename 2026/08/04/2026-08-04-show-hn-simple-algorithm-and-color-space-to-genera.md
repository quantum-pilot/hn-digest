# Show HN: Simple algorithm and color space to generate diverse skin tones

- Score: 532 | [HN](https://news.ycombinator.com/item?id=49170165) | Link: https://toneyalexander.github.io/inclusive-color-space/

### TL;DR

The project defines a three-dimensional color space for simplified skin tones in character creators and digital art. The author manually labels RGB samples, uses PCA to align their curved distribution, then hand-fits transformations that map a sphere into that region. Its T, U, and V axes roughly control deep–fair, flushed–ochre, and cool–warm variation; one radius parameter trades diversity against outliers. The author explicitly calls the method subjective and “good enough.” HN praised its utility while recommending expert labeling, perceptual color spaces, and comparisons with Pantone and Monk scales.

### Comment pulse

- Manual labeling encodes one observer’s perception and bias → multiple expert annotators could provide a stronger dataset without discarding the useful mapping method.
- Established Pantone and Monk references deserve comparison → they offer alternative axes or licensed benchmark palettes for adjacent use cases.
- Physiology may support a lower-dimensional model → melanin and haemoglobin concentrations can approximately parameterize skin color under controlled measurement.

### LLM perspective

- **View:** A transparent approximate space is valuable because its assumptions can be inspected, tuned, and challenged precisely.
- **Impact:** Artists and game developers gain simpler inclusive defaults without forcing users through unrestricted RGB selection.
- **Watch next:** Diverse labeling studies, Oklab experiments, quantitative coverage tests, and modeling of lighting, conditions, and localized variation.
