# The ear does not do a Fourier transform

- Score: 321 | [HN](https://news.ycombinator.com/item?id=45762259) | Link: https://www.dissonances.blog/p/the-ear-does-not-do-a-fourier-transform

### TL;DR

The article explains that the cochlea separates frequencies spatially along the basilar membrane but preserves time information through a filter bank between wavelet and Gabor representations. High frequencies trade frequency precision for temporal precision, with the reverse at low frequencies; efficient-coding research suggests these filters reduce redundancy in natural sounds. HN commenters largely accept the physiology but challenge the headline: colloquially, this remains Fourier-like spectrum analysis with windowing, even if it is not the strict infinite-time transform. Speech occupying a distinct acoustic niche remains speculative.

### Comment pulse

- Time-frequency tradeoffs are fundamental → longer observation improves frequency precision while blurring when a sound occurred.
- The title invites a terminology dispute → strict Fourier transforms differ from the windowed, localized analysis many engineers mean informally.
- Biology may reflect natural statistics → environmental sounds, animal calls, and speech produce different efficient filter shapes.

### LLM perspective

- View: The useful correction is not frequency versus no frequency, but fixed global decomposition versus adaptive temporal localization.
- Impact: Auditory models and audio systems benefit from matching cochlear resolution rather than treating all bands uniformly.
- Watch next: Compare cochlear filter-bank models on speech intelligibility, masking, compression, and noisy-dialogue reproduction.
