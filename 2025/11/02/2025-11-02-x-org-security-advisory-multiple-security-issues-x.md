# X.org Security Advisory: multiple security issues X.Org X server and Xwayland

- Score: 127 | [HN](https://news.ycombinator.com/item?id=45790015) | Link: https://lists.x.org/archives/xorg-announce/2025-October/003635.html

### TL;DR

X.Org disclosed three flaws fixed in xorg-server 21.1.19 and Xwayland 24.1.9: a Present-extension use-after-free on an error path, an Xkb client-resource removal use-after-free, and an unchecked unsigned-short overflow in XkbSetCompatMap. The first dates to Xorg 1.15; the Xkb issues date to X11R6. Commenters reported that XLibre applied identical fixes on the advisory date. Discussion distinguished X11's broad same-session trust problems from these potential privilege-boundary bugs and debated why mature static-analysis tooling had not caught them earlier.

### Comment pulse

- Readers cautioned that X11 permits screen capture and input injection, yet separate privilege contexts still make these fixes important.
- XLibre reportedly patched all three issues immediately rather than having mitigated them beforehand.

### LLM perspective

- View: Legacy trust design does not make memory-safety flaws irrelevant; it can compound their reachable consequences.
- Impact: Distributions and Xwayland users need patched releases wherever untrusted or partially trusted clients can connect.
- Watch next: Vendor backports, exploit analysis, regression testing, downstream XLibre parity, and broader sanitizer or static-analysis coverage.
