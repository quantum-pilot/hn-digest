# Google's Liquid Cooling

- Score: 400 | [HN](https://news.ycombinator.com/item?id=45016720) | Link: https://chipsandcheese.com/p/googles-liquid-cooling-at-hot-chips

### TL;DR

A Hot Chips 2025 account describes Google’s rack-scale liquid cooling for increasingly power-hungry TPUs. Six coolant distribution units exchange heat between a closed machine loop and facility water, with five sufficient so one can be serviced without downtime. Manifolds feed serial chip loops sized for the warmest downstream device; split-flow cold plates and bare-die cooling improve transfer. Google reportedly found pump power below five percent of comparable fan power. Leak testing, filtration, alerting, scheduled maintenance, quick disconnects, and standardized response procedures address reliability at datacenter scale.

### Comment pulse

- Readers noted that mainframes and dense high-performance systems have used liquid cooling for decades.
- Discussion distinguished direct chip cooling from rack-door or liquid-to-air approaches.
- Engineers debated serial versus parallel flow, coolant temperatures, thermal impedance, and facility chiller requirements.

### LLM perspective

- View: The noteworthy achievement is maintainable fleet-scale integration, not the basic idea of water cooling.
- Impact: Direct liquid loops reduce fan energy and unlock denser accelerators while creating shared failure domains.
- Watch next: Track leak rates, pump redundancy, water temperature, heat reuse, and maintenance without compute outages.
