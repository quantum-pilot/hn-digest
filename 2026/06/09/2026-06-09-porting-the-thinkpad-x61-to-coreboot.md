# Porting the ThinkPad X61 to Coreboot

- Score: 163 | [HN](https://news.ycombinator.com/item?id=48456245) | Link: https://blog.aheymans.xyz/post/thinkpad_x61/

### TL;DR

A Coreboot expert ported the undocumented ThinkPad X61 platform by pairing Claude Opus 4.6 with Ghidra, radare2, vendor-firmware dumps, serial logs, and repeated hardware flashes. The LLM reduced a projected three-to-six-month reverse-engineering effort to weeks, but required deep chipset knowledge and produced wrong register names, access widths, timings, and hard-coded assumptions. Expert review turned a machine-specific bring-up into upstreamable code; the author also added GM965 graphics initialization. HN saw major promise for reviving unsupported hardware, while stressing that reference code, recoverable test setups, and experienced reviewers—not prompts alone—made success possible.

### Comment pulse

- LLMs lower reverse-engineering activation energy → a prior Coreboot attempt stalled at RAM initialization, where undocumented platform behavior demanded months of work.
- Success remained expert-led → the model needed more than 20 corrections, physical traces, known-good dumps, and a specialist reviewer.
- Old ThinkPads reward preservation → commenters reported eight-year daily use, replaceable batteries, high-resolution panel swaps, and durable compact chassis.

### LLM perspective

- **View:** AI made an expert’s search loop faster; it did not supply the hardware model needed to judge plausible output.
- **Impact:** Firmware communities can revisit abandoned ports, but must budget hardware, recovery access, test matrices, and senior review.
- **Watch next:** Track X61 upstream acceptance, DIMM coverage, suspend and device testing, FSP experiments, and the promised Rust-based fstart port.
