# GrapheneOS says Pixel 11 has MTE support after all

- Score: 183 | [HN](https://news.ycombinator.com/item?id=49536384) | Link: https://grapheneos.social/@GrapheneOS/117194007157499435

### TL;DR

GrapheneOS states that Pixel 11 retains at least minimal hardware support for Arm Memory Tagging Extension, but says firmware fully disables it. The project suspects Google removed much of the CPU-cache acceleration to reduce cost, damaging performance enough to prevent enablement, while leaving open whether the remaining capability is usable. Commenters explain that MTE helps detect native memory errors such as use-after-free and buffer overflows. They offer competing, unverified explanations involving performance, crashes, priorities, hardware errata, or preparation for a different mechanism.

### Comment pulse

- Hardware presence is not practical support → shipped firmware reportedly leaves MTE disabled, making the optimistic headline conditional.
- Security trades against reliability → commenters report enforcement can crash applications and services that contain memory errors.
- Motive remains unknown → cost, performance, priorities, defects, and future replacement are suggestions, not established explanations.

### LLM perspective

- View: Bare hardware capability matters only if firmware, operating systems, and applications can enable it reliably.
- Impact: Pixel 11 users may lack an active memory-safety defense despite some underlying architectural support.
- Watch next: Test enablement, synchronous-mode overhead, crash rates, cache acceleration, firmware changes, and Google’s technical explanation.
