# Backblaze has stopped backing up OneDrive and Dropbox folders and maybe others

- Score: 925 | [HN](https://news.ycombinator.com/item?id=47762864) | Link: https://rareese.com/posts/backblaze/

### TL;DR

After a decade as a satisfied Backblaze customer, the author discovered that the Personal Backup client no longer included his 383 GB OneDrive folder and, he says, had also omitted a .git directory needed for recovery. Release notes classify excluding OneDrive, Google Drive, Dropbox, Box, iDrive, and similar paths as an improvement to prevent performance, bandwidth, and unintended-upload problems, but users received no direct warning and public exclusions were incomplete. Commenters agreed silent changes broke trust, while debating cloud-only placeholder hazards, “unlimited” economics, and whether the .git claim was accurate.

### Comment pulse

- One family lost a Dropbox-overwritten file after learning Backblaze had stopped capturing it months earlier; several personal and business users planned cancellations.
- Cloud placeholders can trigger huge downloads and exhaust local storage — counterpoint: fully synchronized folders were reportedly excluded too, without user choice.
- Readers urged 3-2-1 backups and restore tests — counterpoint: an offsite provider’s undisclosed omissions undermine the very layer customers were buying.

### LLM perspective

- **View:** The exclusion may solve real technical problems, but silently changing backup scope is itself a severe reliability failure.
- **Impact:** Users cannot mitigate missing coverage they cannot see; sync corruption, ransomware, or account loss may erase the presumed fallback.
- **Watch next:** Direct customer notices, explicit configurable exclusions, local-versus-placeholder detection, restore audits, and clarification of .git behavior.
