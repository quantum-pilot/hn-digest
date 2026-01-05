# Understanding the bin, sbin, usr/bin, usr/sbin split (2010)

- Score: 168 | [HN](https://news.ycombinator.com/item?id=46487921) | Link: https://lists.busybox.net/pipermail/busybox/2010-December/074114.html

- TL;DR  
  Landley explains that Unix’s /bin vs /usr/bin (and related /sbin splits) came from 1970s PDP-11 disk limits: root filled one small pack, so OS binaries “leaked” into /usr on a second. Later features—initrd, shared libraries, big disks—made the distinction technically pointless, yet standards and distros preserved and elaborated it with /usr/local, /opt, tmp rules, etc. BusyBox mostly copies precedent; Landley now just symlinks legacy dirs to /usr, a simplification modern “usr-merge” distros echo.

- Comment pulse  
  - Filesystem split is accidental legacy from tiny disks; modern distros largely usr-merge, and some adopt app-centric layouts. — counterpoint: some still value separate boot-critical binaries.  
  - /usr/local vs /opt keep meaning on traditional Unix → base system vs local or commercial add-ons; Linux’s distro-kernel mix blurs this separation, confusing newcomers.  
  - Some lament initrd, usr-merge, and XDG ~/.local as needless layering; others note benefits: shared /usr mounts, clearer per-user directories, and documented rationale.

- LLM perspective  
  - Historical accidents ossify into “standards”; Linux filesystems show why periodic simplification, even with symlinks, is worth political pain.  
  - For admins and tool authors, relying on PATH and env vars beats hardcoding /bin paths, easing cross-distro and container portability.  
  - Container images, immutable OSes, and language-specific package managers may eventually sideline FHS debates by encapsulating their own hierarchies.
