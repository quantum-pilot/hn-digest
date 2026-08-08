# When “idle” isn't idle: how a Linux kernel optimization became a QUIC bug

- Score: 154 | [HN](https://news.ycombinator.com/item?id=48116064) | Link: https://blog.cloudflare.com/quic-death-spiral-fix/

### TL;DR

Cloudflare found a quiche CUBIC bug that left QUIC downloads stuck at the two-packet congestion-window minimum after severe loss. A test injecting 30% loss for two seconds failed roughly 60% of runs after loss stopped, logging 999 state transitions over 6.7 seconds. The ported Linux optimization mistook each ACK-drained window for application idleness, shifted recovery time forward by an RTT, and suppressed growth indefinitely. Tracking the last ACK rather than only the last send restored 100% passes. HN praised the targeted test while questioning upstream parity and article clarity.

### Comment pulse

- User-space transport ports must track upstream follow-up fixes closely — counterpoint: QUIC implementations have also discovered bugs later corrected in kernel TCP.
- The failure validates adversarial state-space testing: ordinary throughput dashboards and static review would not expose recovery behavior at minimum window.
- Readers criticized undefined “CCA” terminology and the hiring pitch, especially given recent layoffs and reportedly scarce engineering openings.

### LLM perspective

- View: `bytes_in_flight == 0` describes a transient state, not necessarily application idleness; semantic shortcuts become protocol bugs at boundary conditions.
- Impact: A tiny timestamp correction restores post-loss throughput for quiche users without abandoning the original CUBIC epoch-shift optimization.
- Watch next: Production recovery telemetry, broader minimum-window tests, differential checks against Linux CUBIC, BBRv3 rollout, and synchronization of ported fixes.
