# TIL: Apple Broke Time Machine Again on Tahoe

- Score: 154 | [HN](https://news.ycombinator.com/item?id=46848699) | Link: https://taoofmac.com/space/til/2026/02/01/1630

### TL;DR

After attempting an Obsidian restore, Rui Carmo found that both macOS Tahoe machines had silently stopped backing up to a Synology SMB share for about two months. He attributes the failure to changed SMB signing defaults. Editing the Mac’s nsmb.conf and adjusting Synology SMB3, opportunistic locking, leases, durable handles, signing and encryption settings appear to restore operation, though he is testing a containerized Samba target on ZFS for more control. Commenters reported mixed network-backup reliability and criticized silent failures, while some defended local Time Machine’s simplicity and snapshots.

### Comment pulse

- Longtime users contrasted an earlier reliable, approachable product with Tahoe-era regressions and broader concerns about Apple’s software quality.
- Network experiences diverged: some saw recurring sparsebundle corruption, while others ran SMB backups for years or found encrypted bundles more reliable.
- Several favored independent daily backups alongside hourly Time Machine, treating redundancy as protection from silent failure.

### LLM perspective

- View: A backup system that fails silently defeats its central promise even when a configuration workaround exists.
- Impact: NAS users may discover missing recent recovery points only during data loss, making secondary backup paths essential.
- Watch next: Apple acknowledgment, durable SMB compatibility fixes, visible backup-health alerts and long-term results from alternative Samba targets.
