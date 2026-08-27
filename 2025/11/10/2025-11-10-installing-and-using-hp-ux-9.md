# Installing and using HP-UX 9

- Score: 116 | [HN](https://news.ycombinator.com/item?id=45873904) | Link: https://thejpster.org.uk/blog/blog-2025-11-08/

### TL;DR

The author restored a diskless 1989 HP 9000 Model 340 and network-booted it from a PA-RISC Model 705 running HP-UX 9. A second 68K installation placed architecture-specific binaries into the same shared root through context-dependent filesystems: apparent files become hidden directories selecting content by machine context. The author also repaired a failed X11R5 library installation by manually creating the required context. Commenters recalled analogous AFS mechanisms and praised HP-UX documentation, administration, clustering, and resource management despite awkward proprietary tooling.

### Comment pulse

- Former AFS users compared its architecture-dependent paths with HP-UX’s filesystem-level selection across heterogeneous workstations.
- Administrators remembered strong man pages, LVM, Ignite-UX, and production robustness, while preferring GNU command-line tools.
- Commenters framed context-dependent files as inventive vendor-specific Unix engineering that never escaped its original ecosystem.

### LLM perspective

- View: Context-dependent filesystems elegantly hid heterogeneity, but their invisible path semantics made maintenance and portability hazardous.
- Impact: Preservation work documents operational knowledge needed to revive hardware whose original peripherals and instructions are disappearing.
- Watch next: Repeatable cluster images, archived manuals, replacement interfaces, and whether remaining kernel drivers still support this hardware.
