# Single log line is 49KB+ (ext4) / 110KB+ (btrfs) of systemd-journald disk writes

- Score: 141 | [HN](https://news.ycombinator.com/item?id=49290215) | Link: https://github.com/systemd/systemd/issues/40262

### TL;DR

An open systemd issue reports extreme journald write amplification: a roughly 752-byte expanded log record led to at least 55 KB of writes in an isolated ext4 test, while btrfs testing attributed about 110 KB to journald for one line. The experiment disabled compression, mounted dedicated loop filesystems, and compared block and cgroup counters; plain append-and-sync logging was far smaller. Investigation found journald writes mmap-backed persistent data for every entry, delaying only synchronization. Commenters blamed limited filtering and especially severe copy-on-write amplification.

### Comment pulse

- Persistent journald provides structured metadata, but critics called its indexing slow and per-source retention or cleanup controls inadequate.
- Volatile storage forwarded to rsyslog is one workaround; service-level LogFilterPatterns remain limited, cumbersome, and unpredictable.
- The original format promised metadata deduplication and compression, prompting debate over whether later changes or mmap behavior undermined that design.

### LLM perspective

- View: The costly unit is not retained bytes alone, but block churn from small mmap updates and filesystem metadata.
- Impact: Frequent logs can consume IOPS, amplify SSD wear, and cause slowdowns, especially on copy-on-write storage.
- Watch next: Root-cause profiling across filesystems, pwrite comparisons, batching changes, and the upstream response to issue 40262.
