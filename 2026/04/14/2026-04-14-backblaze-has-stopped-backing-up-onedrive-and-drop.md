# Backblaze has stopped backing up OneDrive and Dropbox folders and maybe others

- Score: 925 | [HN](https://news.ycombinator.com/item?id=47762864) | Link: https://rareese.com/posts/backblaze/

- TL;DR  
  Long‑time Backblaze customers discovered the client now silently skips OneDrive, Dropbox and possibly other folders (including .git), despite marketing implying “all data” unlimited backup. The change hides behind release notes and isn’t clearly exposed in exclusions, so many realize only after data loss or near‑misses. HN readers condemn the communication failure, question Backblaze’s “unlimited” consumer model and trustworthiness, debate technical challenges with cloud‑sync stubs, and recommend layered 3‑2‑1 strategies plus alternatives like Arq, restic+B2, or self‑managed backups.

- Comment pulse  
  - Silent exclusion of Dropbox/OneDrive/iCloud folders breaks Backblaze’s core promise → users report unrecoverable files and plan personal and company‑wide migrations to other backup tools.  
  - Defenders cite files‑on‑demand pitfalls and restores → critics note competitors like Arq offer per‑folder options instead of blanket exclusions—counterpoint: avoid stubs, separate sync and backup.  
  - Broader concerns: “unlimited” pricing under rising drive costs, opaque exclusions, and users over‑relying on one provider instead of verifying 3‑2‑1 backups and test restores.

- LLM perspective  
  - View: Silent, non‑configurable exclusions in backup software erode its single most important asset: user trust in worst‑case scenarios.  
  - Impact: Power users and small businesses will likely migrate to configurable tools (Arq, restic, Borg) or B2/S3‑backed self‑hosted solutions.  
  - Watch next: Expect clearer exclusion UIs, explicit sync‑folder policies, and possibly “sync‑aware” backup products that integrate via APIs instead of filesystem stubs.
