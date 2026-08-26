# Understanding the bin, sbin, usr/bin, usr/sbin split (2010)

- Score: 168 | [HN](https://news.ycombinator.com/item?id=46487921) | Link: https://lists.busybox.net/pipermail/busybox/2010-December/074114.html

### TL;DR

Rob Landley traces Unix’s bin and usr/bin split to a PDP-11 with two 1.5 MB disks: the root disk filled, so system directories spilled onto the user disk mounted at usr; a third disk later moved homes elsewhere. Boot-critical tools stayed on root so usr could be mounted. He argues initramfs, shared libraries, and modern storage erased that rationale. HN noted major Linux distributions now perform a usr merge, while disputing parts of his account about local, opt, base systems, and later filesystem conventions.

### Comment pulse

- Accidental constraints often acquire elaborate rationales → compatibility and institutional memory preserve structures after their original hardware problem disappears.
- The modern usr merge collapses duplicate directories → symlinks retain legacy paths for software and scripts that hard-code them.
- Historical objections remain substantive → local and opt conventions, writable mounts, base systems, and separate partitions developed distinct operational purposes.

### LLM perspective

- View: Filesystem layouts are compatibility contracts; obsolete origins persist when changing paths costs more than preserving aliases.
- Impact: Users see confusing duplication, while distributions simplify internals without breaking software expecting historical locations.
- Watch next: Check distribution merge status, boot assumptions, package policy, and remaining applications dependent on legacy paths.
