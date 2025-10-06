# Self hosting 10TB in S3 on a framework laptop and disks

- Score: 179 | [HN](https://news.ycombinator.com/item?id=45480317) | Link: https://jamesoclaire.com/2025/10/05/self-hosting-10tb-in-s3-on-a-framework-laptop-disks/

- TL;DR
    - A screenless Framework laptop plus a USB JBOD runs ZFS (raidz1) and Garage to self-host an S3-compatible store. After ~5 months, it’s holding 10TB, survived reboots and a clean Garage v1→v2 upgrade. Early ZFS instability came from putting Garage metadata on the USB pool; moving metadata to the laptop fixed it. HN dives into hardware casing options, Garage’s practicality with S3 tools, and ZFS approaches (mirrors vs separate pools with snapshots), alongside worries about USB/JBOD reliability.

- Comment pulse
    - Framework mainboard server works → low power, silent; dedicated cases and VESA mounts exist — counterpoint: USB/JBOD cabling risk; some prefer tower servers with mirrored disks.
    - Garage feels mature → setup once, then manage via awscli/rclone; S3-compatible API. Glacier pairing doesn’t fit because Garage needs mounted storage; ZeroFS suggested.
    - ZFS strategy trade-offs → OP used raidz1; others favor two single-disk pools with snapshots and zfs send/recv for flexibility, or classic mirrors for safer failures.

- LLM perspective
    - View: DIY S3 via Garage on repurposed laptops is viable if metadata stays on reliable storage; USB JBODs need careful handling.
    - Impact: Cuts storage costs for small projects; homelabbers keep S3 workflows without cloud lock-in; good for backups, archives, self-hosted app assets.
    - Watch next: Measure power use, USB errors, rebuild times; test Garage v2 durability; compare total cost vs S3/Glacier and document 3-2-1 compliance.
