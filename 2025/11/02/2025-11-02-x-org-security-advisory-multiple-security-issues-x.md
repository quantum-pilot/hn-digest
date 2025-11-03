# X.org Security Advisory: multiple security issues X.Org X server and Xwayland

- Score: 127 | [HN](https://news.ycombinator.com/item?id=45790015) | Link: https://lists.x.org/archives/xorg-announce/2025-October/003635.html

- TL;DR
    - X.Org disclosed three long-standing bugs in the X server and Xwayland—two use-after-free (Present, XKB) and an XKB unsigned-short overflow—fixed in xorg-server 21.1.19 and xwayland 24.1.9. Found via Trend Micro ZDI, the flaws can enable crashes or elevation in configurations where X serves higher-privileged or remote clients. HN notes X’s insecure-by-design trust model, urges updates regardless, observes X11Libre mirrored fixes the same day, and debates using tools like Coverity versus developers prioritizing Wayland.

- Comment pulse
    - X’s trust model lets untrusted clients escalate via X server → elevation risk in multi-user/remote setups — counterpoint: still worth fixing EoP vulnerabilities.
    - X11Libre/xserver synced the patches the same day → not pre-mitigated but promptly updated.
    - Why no Coverity? → limited maintainer time; many X devs now focus on Wayland rather than deepening X maintenance.

- LLM perspective
    - View: Classic C pitfalls in decades-old subsystems; memory safety and bounds checks remain fragile despite mature code.
    - Impact: Distros must ship 21.1.19/24.1.9 or backports; highest risk in X-as-root, remote X11, or Xwayland sandbox escapes.
    - Watch next: Track backport status across Debian, Fedora, Ubuntu; look for CI fuzzing, Coverity adoption, and Xwayland isolation hardening.
