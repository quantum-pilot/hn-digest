# Fire destroys S. Korean government's cloud storage system, no backups available

- Score: 809 | [HN](https://news.ycombinator.com/item?id=45483386) | Link: https://koreajoongangdaily.joins.com/news/2025-10-01/national/socialAffairs/NIRS-fire-destroys-governments-cloud-storage-system-no-backups-available/2412936

- TL;DR
    - A fire at South Korea’s National Information Resources Service destroyed G-Drive, the mandated cloud for ~750k civil servants’ work files. Its “large-capacity, low-performance” design had no external backups, so most personal work data is lost. Ninety-six critical systems were hit; some official records may be recoverable via the separate OnNara system. HN reacts with disbelief at absent offsite redundancy, debates sovereignty vs. hyperscaler use, proposes straightforward local redundancy options, and raises (contested) suspicions about cyber involvement given timing of other investigations.

- Comment pulse
    - Mandating remote storage without offsite backups is mismanagement → DR needs offsite, tested copies; local tech (ZFS/NetApp/DRBD) suffices — counterpoint: keep data off foreign clouds.
    - Backups may exist on-site → agencies sometimes forbid offsite copies but keep hardened, fireproof vaults; absence would be an epically bad call.
    - Suspicion of cyberattack/cover-up → timing aligned with planned inspections; reports of an official’s suicide, alleged leaks — counterpoint: heavy speculation; await forensic and audit findings.

- LLM perspective
    - View: A single logical store without immutable, offsite backups is unacceptable; mandate 3-2-1(+1-0), regular restore tests, and exception reviews.
    - Impact: Expect stalled workflows, public service delays, procurement overhauls, and leadership accountability; security teams will reassess BCP, RPO/RTO, and third-party dependencies.
    - Watch next: Root-cause report (fire vs. compromise), recovery rates for OnNara/G-Drive, new architecture with cross-site immutability, air-gaps, WORM, and independent audits.
