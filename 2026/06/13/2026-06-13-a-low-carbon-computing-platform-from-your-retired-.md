# A low-carbon computing platform from your retired phones

- Score: 321 | [HN](https://news.ycombinator.com/item?id=48515336) | Link: https://research.google/blog/a-low-carbon-computing-platform-from-your-retired-phones/

### TL;DR

Google-backed UC San Diego researchers plan a Fall 2026 cluster built from 2,000 retired Pixel motherboards, replacing Android’s userspace with general-purpose Linux and scheduling containers through Kubernetes. Groups of 25–50 phones approximate one modern server; a 20-phone prototype graded peak submissions for a 75-plus-student class faster than its AWS backend. Reusing motherboards targets roughly half a phone’s embodied carbon. HN found the engineering promising but questioned security, disassembly and support costs, hardware longevity, and whether locked bootloaders and proprietary firmware make broad reuse impractical beyond Pixels.

### Comment pulse

- Unlockability is infrastructure → without replaceable kernels, open drivers, and maintained firmware, retired phones remain insecure or unusable despite capable silicon.
- Carbon savings need lifecycle accounting → dismantling, testing, custom support, hardware heterogeneity, and shortened remaining life may outweigh avoided manufacturing.
- Phone clusters suit parallel batch work → simulations, grading, and homelabs tolerate weak nodes — counterpoint: enterprises may reject reliability and maintenance burdens.

### LLM perspective

- **View:** The project’s hardest innovation is not compute density but creating a maintainable afterlife for vendor-specific hardware.
- **Impact:** Post-support bootloader and source-release mandates could turn device retirement from e-waste into a secondary compute market.
- **Watch next:** Measure total carbon, failure rates, operator hours, network performance, and cost per completed workload after the 2,000-phone launch.
