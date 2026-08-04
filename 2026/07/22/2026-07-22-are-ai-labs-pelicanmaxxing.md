# Are AI Labs Pelicanmaxxing?

- Score: 351 | [HN](https://news.ycombinator.com/item?id=49010129) | Link: https://dylancastillo.co/posts/pelicanmaxxing.html

### TL;DR

A $80 experiment tested whether seven frontier models were secretly optimized for the famous pelican-riding-a-bicycle SVG prompt. Across 1,008 outputs spanning eight animals, six vehicles, and three samples per cell, pelicans ranked sixth and bicycles second-last; their pairing placed 42nd of 48. Difficulty-adjusted regressions found no significant lab-specific boost after multiple-comparison correction. All 21 target scenes faced right, but rightward orientation was common overall. HN readers largely applaud the quantitative check while noting that broad SVG optimization, limited samples, one LLM judge, and other benchmark contamination remain undetected.

### Comment pulse

- Right-facing bicycles likely reflect training imagery → sales photos expose the drivetrain side, while left-to-right motion cues may reinforce the composition.
- Generalization evidence is useful but bounded → adjacent animal-vehicle performance weakens hard-coding claims — counterpoint: three samples cannot exclude direct or broader training.
- Contamination may move elsewhere → commenters spotted unusually coherent otters inside planes, possibly echoing another known image benchmark.

### LLM perspective

- View: Benchmark-specific optimization should be tested through controlled neighborhoods, not inferred from one celebrated output.
- Impact: Informal eval authors gain a practical template: factorial variants, repeated samples, difficulty controls, and public artifacts.
- Watch next: Add human judges, more seeds, paraphrased prompts, held-out combinations, temporal model snapshots, and explicit SVG-generation baselines.
