# When “idle” isn't idle: how a Linux kernel optimization became a QUIC bug

- Score: 154 | [HN](https://news.ycombinator.com/item?id=48116064) | Link: https://blog.cloudflare.com/quic-death-spiral-fix/

### TL;DR
Cloudflare debugged a nasty QUIC performance bug where the CUBIC congestion window could get stuck at its minimum after heavy early loss. A Linux TCP “idle-after-quiet” optimization was ported to quiche, but in QUIC’s userspace setting it misdetected normal small-window cycles as “idle,” repeatedly pushing the recovery start time into the future and blocking window growth. A carefully designed high-loss test exposed the issue; the fix was a tiny change: measure idle time from the last ACK, not the last send. HN readers liked the testing story, but criticized unclear terminology and the corporate tone.

---

### Comment pulse
- Article feels AI-ish and badly timed → awkward prose, unexplained jargon, and a recruiting pitch days after large layoffs—counterpoint: the technical content itself is nontrivial.
- Userspace QUIC is flexible but fragile → fewer eyeballs than the kernel, subtle CUBIC bugs recur, and many argue BBR should replace CUBIC for modern links.
- Testing is the real hero → a targeted, high-loss regression test caught a rare corner-case; good example for teams resisting “expensive” tests.

---

### LLM perspective
- View: This shows how tiny timing assumptions in congestion control can create pathological feedback loops that only appear in extreme regimes.
- Impact: QUIC stacks, especially in-house ones, must track kernel CCA fixes and run adversarial tests around minimum-cwnd behavior.
- Watch next: Wider deployment of BBRv3 in QUIC, standardized test suites for CCAs, and better tooling for visualizing cwnd / recovery dynamics.
