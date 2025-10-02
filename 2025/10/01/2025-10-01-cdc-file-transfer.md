# CDC File Transfer

- Score: 363 | [HN](https://news.ycombinator.com/item?id=45433768) | Link: https://github.com/google/cdc-file-transfer

- TL;DR
    - Google’s archived cdc-file-transfer open-sources Stadia’s high-speed Windows→Linux sync/stream tools. It uses content-defined chunking (CDC) for deduped diffing (“cdc_rsync”) and on-demand streaming to a FUSE filesystem (“cdc_stream”). The project reports remote diffing up to 30× faster than rsync (≈1500 MB/s vs 50 MB/s), aided by Windows-native binaries and CDC-based algorithms (updated to “regression chunking”). HN debates CDC variants (FastCDC vs lookahead/gearhash), clarifies rsync’s fixed-block approach, and shares primers for understanding CDC.

- Comment pulse
    - CDC with lookahead improves FastCDC → go-cdc adds “lazy matching”-style lookahead, potentially better boundaries and throughput for build caches and sync.
    - Rsync lacks CDC boundaries → fixed-size blocks with rolling hash; CDC diffing plus native Windows IO explains speedups — counterpoint: rsync stagnates, unlikely to integrate.
    - Want CDC intuition? → readers share clear intros on chunking and gear hashing to fill gaps left by the README.

- LLM perspective
    - View: CDC’s boundary detection is algorithmic; ML-chosen boundaries add complexity with unclear win; prioritize hashing tweaks and lookahead first.
    - Impact: Faster remote diffs speed up Windows-based devs targeting Linux: game assets, Bazel/CMake builds, WSL/SSH workflows, CI artifact syncing.
    - Watch next: Benchmark FastCDC vs regression vs go-cdc on real trees; test over WAN; explore rsync module/patch; maintain non-archived fork with releases.
