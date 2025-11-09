# My friends and I accidentally faked the Ryzen 7 9700X3D leaks

- Score: 276 | [HN](https://news.ycombinator.com/item?id=45855933) | Link: https://old.reddit.com/r/pcmasterrace/comments/1orc6jl/my_friends_and_i_accidentally_faked_the_ryzen_7/

- TL;DR
  - Friends tinkering with Zen 5 edited a Ryzen 7 9700X’s identifiers and heavily PBO-overclocked it; a Passmark run then appeared as a “9700X3D” leak. Some outlets echoed it; others noticed the X3D-inconsistent clocks and urged caution. HN debates span: fakes are trivial when databases trust CPUID strings, leak amplification rewards speed, and journalism quality varies. Enthusiasts note such low‑level hacking is common, and editable metadata means verification—not headlines—should drive interpretation.

- Comment pulse
  - Faking benchmark “leaks” is easy → edit /proc/cpuinfo, boost clocks with PBO; Passmark ingests strings uncritically — counterpoint: several outlets flagged the clock inconsistency.
  - Leak economy rewards speed over verification → hobbyist runs become headlines; Twitter personalities parroted claims without context; readers should reassess sources.
  - Not all coverage was bad → multiple mainstream articles noted discrepancies and prior 9850X3D/9950X3D2 rumors, tempering the narrative.

- LLM perspective
  - View: Treat device identifiers as untrusted input; corroborate with microcode version, AGESA, OPN codes, power limits, and multi-benchmark consistency.
  - Impact: Consumers and aggregators risk misinformation; chip vendors and benchmark platforms face credibility hits when spoofed entries propagate.
  - Watch next: Benchmark databases adding attestation: MSR cross-checks, BIOS-signed reports, telemetry hashes; AMD announcements on X3D SKUs and AGESA changes.
