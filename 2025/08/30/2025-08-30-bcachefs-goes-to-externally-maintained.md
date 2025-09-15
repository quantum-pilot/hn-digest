# Bcachefs Goes to "Externally Maintained"

- Score: 227 | [HN](https://news.ycombinator.com/item?id=45074312) | Link: https://lwn.net/Articles/1035736/

TL;DR
- Linus reclassified bcachefs as “externally maintained,” signaling no near-term mainline updates while keeping the code in-tree. The backdrop: protracted conflict over process and trust between Kent Overstreet and kernel leadership after a high-severity bug/recovery patch dispute. HN worries center on DKMS-style pain, bus-factor risk, and the broader Linux FS landscape (btrfs stability, ZFS practicality, Debian packaging fallout). Possible paths: a proxy maintainer, an out-of-tree cadence, or eventual in-tree stagnation and removal.

Comment pulse
- Use a proxy maintainer → Could upstream patches while insulating conflict — counterpoint: underlying trust/process disputes mean a go‑between won’t fix fundamentals.
- DKMS concern → Out-of-tree means rebuild friction; distros could carry modules or use CKMS, but users still fear breakage.
- FS landscape anxiety → btrfs maturity disputed; some just use ZFS; bus-factor-1 worries and Debian orphaning amplify risk perception.

LLM perspective
- View: Prefer a seasoned kernel liaison to gate changes, plus a narrow, well-documented in-tree sync policy.
- Impact: Users face module management; distros decide to ship bcachefs out-of-tree; testing/QA shifts further upstream.
- Watch next: Who volunteers as maintainer; distro packaging (DKMS/CKMS) quality; kernel decisions on pruning if updates stall.
