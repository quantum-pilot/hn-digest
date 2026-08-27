# How bad can a $2.97 ADC be?

- Score: 182 | [HN](https://news.ycombinator.com/item?id=45582462) | Link: https://excamera.substack.com/p/how-bad-can-a-297-adc-be

### TL;DR

The author tested four inexpensive ADS1115 breakout boards and found that they exposed 16-bit readings, a working programmable-gain amplifier, and selectable sample rates. However, three ran slower than the datasheet’s tolerance at the lowest rate, one had severely broken timing, and measurements showed roughly 0.5% gain error. A simple linear correction reportedly reduced error to about 10 µV. The author suspects clones or out-of-spec parts, but leaves identification unresolved pending comparison with a pricier board.

### Comment pulse

- Readers proposed decapping or sanding chips to distinguish clones, rejects, and relabeled parts.
- Several challenged the article’s broad MCU-ADC claims and noted that board layout, references, noise, and test setup affect effective resolution.

### LLM perspective

- View: The experiment demonstrates usable cheap hardware, not a verified counterfeit supply chain.
- Impact: Hobbyists may gain precision after calibration, but timing defects make incoming-part testing essential.
- Watch next: The controlled comparison with a reputable board should separate device error from setup effects.
