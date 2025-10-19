# StageConnect: Behringer protocol is open source

- Score: 175 | [HN](https://news.ycombinator.com/item?id=45625251) | Link: https://github.com/OpenMixerProject/StageConnect

TL;DR
- OpenMixerProject released a GPL-3.0 Arduino library for Behringer’s StageConnect over Analog Devices A2B (AD242x), carrying 32 channels of uncompressed 48 kHz/32‑bit audio over a single XLR. Targets setups like WING↔DP48 with control via virtual I2C; docs note A2B filter tuning and ~15 m cable guidance (Behringer allows longer). HN asks about latency/distance and debates Behringer’s role: strong value and support vs lingering quality concerns and ethics of cloning versus innovation.

Comment pulse
- Practicality → A2B suggests ~15 m per link; Behringer permits longer. Latency figures aren’t stated; commenters ask about repeaters for distance.
- Value vs quality → Budget mixers deliver powerful routing/IO; some report PSU and control failures yet keep them for capability and price.
- Ethics/innovation → Cloning broadens access and lowers cost — counterpoint: it can undercut innovators, reduce R&D, and homogenize gear.

LLM perspective
- View: Open protocol and Arduino library lower barriers to building StageConnect-compatible stage boxes and controllers.
- Impact: DIY/audio vendors can add A2B interfaces, reducing reliance on proprietary cards like Dante or Ultranet.
- Watch next: Publish latency/cable benchmarks, interoperability matrices, and reference schematics; maybe permissive licensing for docs to foster vendor participation.
