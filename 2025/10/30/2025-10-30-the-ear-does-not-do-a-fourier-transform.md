# The ear does not do a Fourier transform

- Score: 321 | [HN](https://news.ycombinator.com/item?id=45762259) | Link: https://www.dissonances.blog/p/the-ear-does-not-do-a-fourier-transform

- TL;DR
    - The cochlea’s basilar membrane separates frequencies tonotopically, but hearing relies on a bank of time-localized, level-dependent filters—closer to wavelets/Gabor than a global Fourier transform. Resolution trades off: high frequencies favor timing; low frequencies favor pitch precision, consistent with time–frequency uncertainty. Lewicki’s ICA suggests these filters efficiently encode natural sounds; speech sits in a distinctive time–frequency niche, hinting at coevolution. HN debated clickbait vs. pedagogy, noted formal FT/DFT/STFT distinctions, pointed to Lyon’s CARFAC model, and discussed ecological ‘acoustic niche’ parallels and practical audio-mixing implications.

- Comment pulse
    - Ear is “Fourier-ish” → Windowed filter banks approximate STFT/DFT behavior; objections are definitional — counterpoint: cochlear filters are asymmetric, non-orthogonal, compressive; masking isn’t FFT-like.
    - Speech–ear coevolution hypothesis → Speech occupies a unique time–frequency niche; parallels with animal ‘acoustic niche’ partitioning suggest evolutionary tuning.
    - Pointers and practice → Lyon’s CARFAC model for realistic simulation; idea to mix media audio for intelligible dialogue by exploiting cochlear filter characteristics.

- LLM perspective
    - View: Replace STFT with gammatone/CARFAC-like filterbanks plus fast-acting compression for robustness to noise and level.
    - Impact: Improves ASR, hearing aids, speech enhancement, codec perceptual quality; guides dialogue mixing targeting human auditory resolution limits.
    - Watch next: Benchmarks comparing CARFAC vs STFT front-ends; psychophysical tests on masking/temporal resolution; open-source, real-time CARFAC implementations.
