# The struggle of resizing windows on macOS Tahoe

- Score: 577 | [HN](https://news.ycombinator.com/item?id=46579864) | Link: https://noheger.at/blog/2026/01/11/the-struggle-of-resizing-windows-on-macos-tahoe/

### TL;DR

macOS Tahoe keeps a 19×19-pixel corner-resize target while dramatically rounding the visible window. A square corner would place 62% of that target inside the window; Tahoe instead leaves about 75% outside, so users instinctively clicking the visible corner often miss and must grab empty space beyond it. HN treated this as form overriding usability, linking it to other Tahoe regressions and similar Windows behavior. Some preferred older explicit resize grips, while others noted those interfaces restricted resizing to one corner and carried their own costs.

### Comment pulse

- System regression → upgraders report focus loss, freezes, and visual glitches, prompting some to stay on Sequoia or reconsider Linux.
- Affordance tradeoff → Aqua-style grips were obvious and scrollbars visible — counterpoint: older designs limited resizing direction and consumed space.
- Organizational critique → commenters blame design incentives and weak iteration for preserving aesthetic decisions after testing exposes usability failures.

### LLM perspective

- View: A control’s interactive geometry should reinforce its visible boundary, especially for high-frequency precision tasks.
- Impact: Small target mismatches accumulate into daily friction and erode confidence in an entire operating-system release.
- Watch next: Test hit-area changes across scaling factors, input devices, window shapes, and accessibility settings.
