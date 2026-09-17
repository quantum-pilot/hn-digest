# Backups Aren't Simple

- Score: 259 | [HN](https://news.ycombinator.com/item?id=49732513) | Link: https://filipovski.net/2026/09/16/backups-arent-simple.html

### TL;DR

A family-photo mishap becomes a tour through why copying files is only the beginning of backup design. Real protection needs point-in-time snapshots, explicit recovery objectives, retention rotation, deduplication, permissions, database-consistent exports, media diversity, offsite copies, encryption, and checksums. Object storage adds metadata and small-file cost complications, making established tools such as Borg or Restic preferable to fragile custom scripts. The final requirement is periodic restore testing. HN stories reinforced immutable or unplugged copies and the distinction among redundancy, backup, and archival.

### Comment pulse

- Restore is the real feature → successful jobs mean little until representative data and systems can be recovered under pressure.
- Backup operations can destroy data → one copy should remain unplugged or immutable while another is updated, rotated, or pruned.
- Different goals require different mechanisms → redundancy preserves availability, backups recover prior states, and archives retain long-lived inactive records.

### LLM perspective

- View: Backup complexity comes from independent failure modes, not from copying bytes.
- Impact: Individuals and small operators need tested policies, not merely extra disks or cloud-sync subscriptions.
- Watch next: Automate restore drills, monitor missed snapshots, verify database consistency, and document recovery-point and recovery-time targets.
