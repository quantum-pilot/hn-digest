# Maestro Technology Sells Used SSD Drives as New

- Score: 149 | [HN](https://news.ycombinator.com/item?id=45903888) | Link: https://kozubik.com/items/MaestroTechnology/

- TL;DR
  Rsync.net bought four “new” Intel D3-S4510/S4610 3.84TB SSDs from Amazon seller Maestro Technology for a ZFS special vdev; SMART revealed ~3 years’ prior use, so they returned them and warned others. HN reports similar experiences and weak Amazon enforcement, with reviews removed. Some argue the drives showed only 1–11% TBW consumed, but for a special vdev any endurance uncertainty is unacceptable. Debate centers on blaming the seller versus Amazon’s marketplace model and whether mission-critical hardware should ever be sourced from Amazon.

- Comment pulse
  - Amazon enables reseller fraud → reports ignored, reviews removed; suggest state AG complaints. — counterpoint: returns are easy; buying "Ships from/Sold by Amazon" reduces risk.
  - Wear minimal → DWPD math shows 1–11% TBW used. — counterpoint: ZFS special vdev needs pristine drives; prior use risks early exhaustion.
  - Mission-critical buys on Amazon are reckless → prefer authorized channels, no-commingle SKUs. — counterpoint: some routinely buy on Amazon, verify SMART on arrival without issues.

- LLM perspective
  - View: Marketplace supply chains are too porous for enterprise SSDs; always validate SMART, TBW, power-on hours, and serial provenance.
  - Impact: Operators favor authorized distributors, sealed boxes, serial verification; policies ban third-party marketplace listings for critical components.
  - Watch next: Amazon enforcement on used-as-new, AG/FTC cases; vendor safeguards on SMART counters; public endurance benchmarks for ex–data-center drives.
