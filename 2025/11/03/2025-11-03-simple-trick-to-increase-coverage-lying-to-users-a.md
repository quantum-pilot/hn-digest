# Simple trick to increase coverage: Lying to users about signal strength

- Score: 427 | [HN](https://news.ycombinator.com/item?id=45795036) | Link: https://nickvsnetworking.com/simple-trick-to-increase-coverage-lying-to-users-about-signal-strength/

### TL;DR

Android’s carrier configuration includes an undocumented `KEY_INFLATE_SIGNAL_STRENGTH_BOOL` option that displays cellular signal one bar higher than the underlying calculation. The author found the flag enabled in configurations for AT&T and Verizon and argues that it damages trust alongside ambiguous 5G indicators. The setting changes presentation, not radio reception. Commenters noted that bars already vary by device, modem capability, thresholds, SIM state, and network mode, so comparisons are difficult; diagnostic screens exposing dBm provide a more direct measurement.

### Comment pulse

- Several commenters reported strong-looking bars with unusable service, though these anecdotes cannot isolate the configuration flag as the cause.
- Others argued newer radio hardware may legitimately extract usable service at weaker measured signal levels.

### LLM perspective

- View: A silent one-bar adjustment turns an already coarse indicator into a less trustworthy interface.
- Impact: Users may misdiagnose dead zones, device faults, or carrier coverage when display policies differ.
- Watch next: Whether Android documents the flag and exposes consistent signal-quality details to users.
