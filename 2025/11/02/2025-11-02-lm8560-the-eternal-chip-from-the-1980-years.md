# LM8560, the eternal chip from the 1980 years

- Score: 113 | [HN](https://news.ycombinator.com/item?id=45787842) | Link: https://www.tycospages.com/other-themes/lm8560-the-eternal-chip-from-the-1980-years/

- TL;DR
  - Deep dive into the LM8560, the low-power Sanyo MOS IC behind decades of red LED alarm clocks. It counts 50/60 Hz mains, drives a duplex LED display, and includes a 9V battery backup using a 900 Hz RC oscillator—cheap, calibration-free, and long-lived versus MCU flash. The author documents hidden key combos, common faults (line-noise overcounting, backup drift), fixes, and quartz add-ons; notes hobbyist downsides (proprietary display, shrink-DIP). HN reminisces, debates the “eternal” 555, and shares repairs and modern MCU alternatives.

- Comment pulse
  - 555 is the real “eternal chip” → shipping since 1972; ubiquitous across designs — counterpoint: many now default to MCUs to avoid analog RC math.
  - Vintage LM8560 clocks still run → a 1985 Luxor/Nokia unit works after antenna repair; mains-sync logic and 9V backup favor longevity.
  - Undocumented tricks matter → readers rediscovered second-display/reset combos to align time precisely on vintage units.

- LLM perspective
  - View: Specialized, fixed-function ICs can outlive trends: mains-synced timekeeping plus integrated LED drive beat MCUs for cost and simplicity.
  - Impact: Parts scarcity shifts value to repair: add line filtering, tune backup RC, but duplex displays and shrink-DIP limit hobbyist rebuilds.
  - Watch next: Track clone reliability and supply; open-source MCU emulators for duplex driving; grid-frequency regulation amid renewables affecting clock accuracy.
