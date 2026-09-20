# Btrfs/ZFS/bcachefs under workloads classic benchmarks skip

- Score: 149 | [HN](https://news.ycombinator.com/item?id=49768833) | Link: https://bartosz.fenski.pl/modern-fs-benchmark/

### TL;DR

A 598-run benchmark compares Btrfs, ZFS, Bcachefs, Ext4, and XFS configurations across project-specific I/O, metadata, snapshot, degraded, near-full, and corruption workloads. Bcachefs led the author's composite index and many small-write tests; ZFS excelled in several cold-read and compression cases; Btrfs led some tree-copy and snapshot operations; Ext4 deletion was fastest. Results come from noisy cloud VMs using loop devices on shared backing storage, so the author stresses relative patterns, tuning effects, and workload fit—not universal rankings.

### Comment pulse

- Reliability and recovery outweigh peak speed → filesystem choice also depends on failure behavior, repair tools, and operational confidence.
- The test bed limits generalization → shared runners and loop-backed devices cannot reproduce independent disks or every hardware failure mode.
- Bcachefs performance attracts interest → its responsiveness looks strong — counterpoint: kernel status and project governance still concern potential adopters.

### LLM perspective

- View: The useful result is workload sensitivity; configuration choices can move rankings more than filesystem labels.
- Impact: Operators should benchmark representative data paths and include recovery procedures before selecting storage stacks.
- Watch next: Dedicated-hardware repetitions should test whether the cloud-derived ratios survive HDD, SSD, and degraded-array conditions.
