# How bad can a $2.97 ADC be?

- Score: 182 | [HN](https://news.ycombinator.com/item?id=45582462) | Link: https://excamera.substack.com/p/how-bad-can-a-297-adc-be

- TL;DR
    - Author tests $2.97 ADS1115 boards that act like real TI parts (16-bit output, working PGA), but show spec drift: slow or wildly wrong data rates and ~0.5% gain/offset error at 2.5 V. A linear calibration recovers ~10 µV accuracy. HN debates whether these are clones or off‑spec parts and challenges the article’s MCU ADC generalizations.

- Comment pulse
    - Counterfeits vs rejects → Sanding/decap to compare dies; many counterfeits are relabels/QC rejects; some suspect ADS1015 relabels — counterpoint: author measured true 16‑bit output.
    - MCU ADCs can achieve 10+ ENOB → With stable references and noise control; author’s blanket 8–9 ENOB claim and 3.3V-reference remark overgeneralize.
    - Price gap may be volume and margin → LCSC could buy direct and sell cheaper; several report reliable orders, not pervasive counterfeits.

- LLM perspective
    - View: Cheap ADS1115 modules mostly behave, but show gain and timing errors; per‑unit calibration can recover precision, yet variance risks reliability.
    - Impact: Good for hobbyists and non‑safety products; avoid in metrology/regulated gear unless traceable source and characterization across temperature and PGA ranges.
    - Watch next: Compare Adafruit board; measure INL/DNL, noise, temp drift, data‑rate accuracy across units; decap a cheap chip to verify die.
