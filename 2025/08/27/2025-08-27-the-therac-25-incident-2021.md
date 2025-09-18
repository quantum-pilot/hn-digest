# The Therac-25 Incident (2021)

- Score: 449 | [HN](https://news.ycombinator.com/item?id=45036294) | Link: https://thedailywtf.com/articles/the-therac-25-incident

- TL;DR
  A detailed retelling of the Therac‑25 overdoses: a software‑only radiotherapy machine reused assembly code, lacked hardware interlocks, and harbored fatal bugs—a race from fast cursor edits and a one‑byte overflow—delivering tens of thousands of rads while reporting underdoses. AECL assumed software couldn't fail, had no test plan, and issued a taped‑keycap workaround until FDA forced fixes. The broader lesson: safety emerges from process, testing, reporting culture, and independent failsafes. HN highlights medicine’s justified distrust of early IT, parallels to Horizon/737 MAX, and looming AI/agent risks.

- Comment pulse
  - Design for failure: assume software misbehaves; enforce independent hardware interlocks and dose cutoffs to cap harm — counterpoint: culture/process still determine whether issues get fixed.
  - Medicine’s distrust of computers had causes: early EMRs were clunky, unsafe, nonredundant; outages forced paper; many EMRs aren’t regulated as medical devices.
  - Systemic overtrust: managers assumed software can’t fail; echoes in UK Post Office scandal and autonomy claims; developers warn new AI/agents may repeat Therac-like harms.

- LLM perspective
  - View: Treat ML/agents as untrusted components; enforce hard limits with physical interlocks, watchdogs, and runtime monitors.
  - Impact: Regulators will push IEC 62304/ISO 14971 rigor into EMRs and AI-enabled devices; vendors must build testable safety cases.
  - Watch next: Public benchmarks of safety incidents, mandatory near-miss reporting, and third‑party audits; adoption of runtime dose sensors and human-in-the-loop gates.
