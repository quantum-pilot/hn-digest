# No leap second will be introduced at the end of December 2026

- Score: 221 | [HN](https://news.ycombinator.com/item?id=48846281) | Link: https://datacenter.iers.org/data/latestVersion/bulletinC.txt

### TL;DR

IERS Bulletin C 72 confirms that UTC will not receive a leap second at the end of December 2026. The UTC–TAI offset remains −37 seconds, unchanged since January 1, 2017, until further notice. IERS reviews Earth-rotation measurements every six months and either announces a June or December adjustment or confirms none is needed. HN discussion explained why scheduling is not deterministic: atmosphere, oceans, core dynamics, ice, groundwater, and mass redistribution perturb rotation. Unix time ignores leap seconds, while some operators smear adjustments gradually; GPS remains 18 seconds ahead of UTC.

### Comment pulse

- Rotation is measurable but not fully predictable → weather, oceans, ice, groundwater, core motion, and human water movement alter angular momentum.
- Unix time abstracts the problem → leap seconds are not uniquely representable, so precise systems need explicit policies such as clock smearing.
- Offsets remain easy to confuse → UTC trails TAI by 37 seconds and GPS by 18; GPS trails TAI by 19.

### LLM perspective

- **View:** This bulletin announces operational continuity, not a change: systems should retain their current offsets and leap-second configuration.
- **Impact:** No December insertion avoids the recurring synchronization, timestamp ambiguity, and distributed-system hazards associated with a UTC step.
- **Watch next:** Review the next semiannual Bulletin C and verify time libraries, satellite offsets, smear policies, and stale leap tables.
