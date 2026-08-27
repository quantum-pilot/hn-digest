# CDC File Transfer

- Score: 363 | [HN](https://news.ycombinator.com/item?id=45433768) | Link: https://github.com/google/cdc-file-transfer

### TL;DR

Google’s archived CDC File Transfer repository contains former Stadia tools for synchronizing and streaming large directory trees from Windows to Linux. `cdc_rsync` uses content-defined chunking to reuse unchanged file regions, while the streaming components expose a local directory through a remote FUSE filesystem and fetch chunks as needed. Repository text claims its remote diffing reached up to 1,500 MB/s versus 50 MB/s for rsync in tests. The project is Apache-licensed but read-only, with its last displayed commit dating to 2023.

### Comment pulse

- Readers debated how its chunking differs from rsync’s fixed destination blocks plus rolling-hash matching.
- Several explored alternative CDC algorithms and whether lookahead could improve FastCDC.
- Commenters appreciated Stadia’s open-sourced residue while noting many existing options for game streaming itself.

### LLM perspective

- View: The useful artifact is specialized data movement, not a revival of Stadia as a service.
- Impact: Reusing content-defined chunks can sharply shorten large iterative Windows-to-Linux transfers when files shift internally.
- Watch next: With the repository archived, adopters must assess maintenance, security, and compatibility ownership themselves.
