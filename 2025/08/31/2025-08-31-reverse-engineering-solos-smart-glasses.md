# Reverse engineering Solos smart glasses

- Score: 166 | [HN](https://news.ycombinator.com/item?id=45087803) | Link: https://jfloren.net/b/2025/8/28/0

TL;DR
An engineer sniffed Android’s Bluetooth logs to decode Solos (2018) HUD glasses: a Bluetooth RFCOMM stream with a 0x1d60 header sends RLE‑encoded RGB565 frames (428×240) and optional offsets. A Python tool now pushes arbitrary images as a DIY wearable HUD. A puzzling “length” field is half the byte count—likely 16‑bit words or legacy from raw RGB565. HN discusses practicality and safety; some cite Engo/Form and Monocle alternatives, while others welcome a cheap wireless display for notifications/navigation.

Comment pulse
- Length anomaly → field likely in 16‑bit words, inherited from raw RGB565 days. — counterpoint: early protocol probably sent u16 pixels without RLE.
- Use cases → cyclists/swimmers split: bike computers suffice for many; others praise Engo 2 HUD and Form goggles’ metrics but dislike subscriptions.
- Safety/comfort → some worry about a bright micro‑display near the eye while riding — counterpoint: with the insert, impact protection and distraction feel acceptable.

LLM perspective
- View: Low-bandwidth RLE over RFCOMM is enough for practical HUDs; old hardware becomes useful again.
- Impact: Makers gain a $30 wireless display; add cron-generated dashboards, notifications, and maps without modifying firmware.
- Watch next: Document remaining commands (audio enable, navigation), clarify length semantics, measure max frame rate/latency, publish a reusable library and spec.
