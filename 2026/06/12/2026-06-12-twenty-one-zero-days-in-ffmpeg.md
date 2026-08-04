# Twenty One Zero-Days in FFmpeg

- Score: 287 | [HN](https://news.ycombinator.com/item?id=48510046) | Link: https://depthfirst.com/research/21-zero-days-in-ffmpeg

### TL;DR

Depthfirst says its autonomous security agent found 21 previously undisclosed FFmpeg vulnerabilities for roughly $1,000, validating them with reproducible inputs rather than theoretical reports. Its showcase is a remotely reachable AV1-over-RTP heap overflow: one crafted 183-byte packet can overwrite a buffer-release function pointer and redirect execution when FFmpeg opens an attacker-controlled RTSP stream. HN found the result credible but unsurprising for a vast, performance-sensitive C parser. Commenters argued the real bottleneck is remediation, while disputing the post’s disclosure choices, exploitability implications, “zero-day” terminology, and promotional framing.

### Comment pulse

- Sandbox untrusted media → FFmpeg’s enormous attack surface and recurring memory bugs make direct exposure unreasonable despite deployment constraints.
- Fixes matter more than findings → maintainers face abundant reports but scarce patch labor; one commenter cited 94% acceptance for generated PRs.
- Disclosure enables mitigation → counterpoint: critics questioned publishing serious details, full exploitation without an ASLR leak, promotional framing, and the “zero-day” label.

### LLM perspective

- **View:** Proof-producing agents raise confidence, but measured security value depends on remediation throughput and exploitability triage.
- **Impact:** Media pipelines should isolate decoders, restrict network access, and minimize enabled formats before accepting user-controlled streams.
- **Watch next:** Track downstream patch uptake, regression tests, and whether the AV1 primitive becomes reliable code execution under ASLR.
