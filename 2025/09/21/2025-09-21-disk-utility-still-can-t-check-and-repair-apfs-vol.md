# Disk Utility still can't check and repair APFS volumes and containers (2021)

- Score: 99 | [HN](https://news.ycombinator.com/item?id=45322623) | Link: https://eclecticlight.co/2021/11/19/disk-utility-still-cant-check-and-repair-apfs-volumes-and-containers/

- TL;DR
  - In macOS Monterey 12.0.1, Disk Utility’s First Aid often can’t unmount APFS volumes/containers, so checks fail even though fsck_apfs works. Workarounds: use Recovery; or manually Unmount, then run fsck_apfs (-n/-y; include/exclude snapshots; unlock encrypted with diskutil … -nomount), then remount. Apple now recommends checking volumes → container → disk. HN adds: fsck_apfs fixed resize/orphan issues for some; others lament Apple’s fragile filesystems and Time Machine over SMB; several say DU works after ejecting or in Recovery.

- Comment pulse
  - DU fails on APFS; manual Unmount + fsck_apfs -y after unlock fixes orphan/resize issues → runs checks off-line.
  - Apple FS stack fragile, especially TM over SMB → frequent corruption; users abandon TM — counterpoint: NFS works better; others succeed via Recovery.
  - Is bug narrow (mixed HFS+/APFS) or ongoing? → Some 2024 reports say “still impossible”; others say DU works after ejecting or in Recovery.

- LLM perspective
  - View: The failure is unmount/orchestration around fsck_apfs, not the checker; Recovery-mode avoids live-mount conflicts.
  - Impact: APFS and Time Machine users on external or network volumes face failed repairs, scary errors, and integrity drift.
  - Watch next: Verify fixes in Sonoma/Sequoia Disk Utility; Apple docs on order-of-operations; independent TM-over-SMB reliability benchmarks.
