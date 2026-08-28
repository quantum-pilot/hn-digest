# Bcachefs Goes to "Externally Maintained"

- Score: 227 | [HN](https://news.ycombinator.com/item?id=45074312) | Link: https://lwn.net/Articles/1035736/

### TL;DR

Linus Torvalds changed bcachefs's Linux maintainer status to “externally maintained.” LWN interprets the change as meaning new bcachefs work is unlikely to enter mainline soon, while immediate removal of the existing driver also appears unlikely. The brief notice provides no detailed roadmap. Discussion attributes the rupture to repeated disputes over patch classification, timing, risk, and maintainer judgment; bcachefs developer Kent Overstreet contests the simpler claim that he merely failed to follow merge rules and cites urgent recovery work after a serious data-loss bug.

### Comment pulse

- Users weighed remaining in-tree support against eventual out-of-tree maintenance, distribution packaging, and kernel-version drift.
- The filesystem's small maintainer base and maturity raised data-safety concerns despite praise for its capabilities.

### LLM perspective

- View: “Externally maintained” freezes the governance conflict without forcing immediate filesystem removal.
- Impact: Existing users retain code, but uncertain upstream flow increases operational and long-term maintenance risk.
- Watch next: A trusted integration path, maintainer succession, stable releases, and transparent recovery testing are now critical.
