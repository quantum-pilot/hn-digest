# Disk Utility still can't check and repair APFS volumes and containers (2021)

- Score: 99 | [HN](https://news.ycombinator.com/item?id=45322623) | Link: https://eclecticlight.co/2021/11/19/disk-utility-still-cant-check-and-repair-apfs-volumes-and-containers/

### TL;DR

This 2021 article says macOS Disk Utility often failed to check or repair APFS volumes because it could not unmount them, even though its separate Unmount action worked. It recommends Recovery mode for boot volumes or manually unmounting and running `fsck_apfs`, using `-n` to check and `-y` to repair, with special handling for encrypted volumes and snapshots. Commenters reported the command fixed orphan-inode problems that Disk Utility did not, while others disputed the present-tense title because their newer systems sometimes worked.

### Comment pulse

- Direct `fsck_apfs` can succeed where the GUI fails → one encrypted-volume repair required unlocking without mounting first.
- APFS reliability remains contested → commenters shared corruption experiences, while others reported successful checks on newer macOS releases.
- Historical framing matters → the source documents Monterey 12.0.1, not every current APFS configuration.

### LLM perspective

- View: The article provides a targeted workaround, not proof that every modern Disk Utility repair path remains broken.
- Impact: Mac administrators gain recovery options but must handle device identifiers and repair flags carefully.
- Watch next: Reproduce across current macOS versions, mixed-partition disks, encrypted volumes, and Time Machine containers.
