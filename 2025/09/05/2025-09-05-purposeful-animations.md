# Purposeful animations

- Score: 542 | [HN](https://news.ycombinator.com/item?id=45139088) | Link: https://emilkowal.ski/ui/you-dont-need-animations

- TL;DR
    - Animations should be purposeful: explain state changes, provide immediate feedback, or create spatial consistency; otherwise skip them. Frequency matters—don’t animate high-volume or keyboard-triggered actions. Keep motion fast (typically ≤300ms), with special cases like tooltips using initial delay but instant subsequent hovers. HN agrees on utility-over-delight, pushing for even snappier defaults (~200ms), with comparisons to Apple’s often sluggish, blocking animations. Some defend tasteful micro-animations for perceived quality, while others say simple cross-fades suffice, especially in B2B tools.

- Comment pulse
    - Primary use is clarifying state changes → reduces ambiguity. — counterpoint: tasteful micro-animations improve perceived quality even if not strictly necessary.
    - Apple OS animations feel slow and sometimes block input → users disable/speed them up; some transitions are interruptible but others still hinder workflows.
    - Keep durations short (~200ms) and avoid animating high-frequency, keyboard-initiated actions → faster, more connected interactions; simple cross-fades cover most cases.

- LLM perspective
    - View: Principle-based animation: purpose, frequency, speed, and interruptibility trump “delight”; use motion to explain state changes.
    - Impact: Expect enterprise and power-user tools to trim animations; design systems may default to ≤200ms and emphasize cancelability.
    - Watch next: OS-level settings for animation speed/interruptibility, guidance updates in Radix/Base UI, and benchmarks of perceived responsiveness vs duration.
