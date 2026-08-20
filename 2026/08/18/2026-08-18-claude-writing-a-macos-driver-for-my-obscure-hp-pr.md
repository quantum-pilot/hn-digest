# Claude writing a macOS driver for my obscure HP printer built only for Windows

- Score: 319 | [HN](https://news.ycombinator.com/item?id=49344643) | Link: https://twitter.com/kuberwastaken/status/2089377982536388964

### TL;DR

A brief post celebrates using Claude to make an obscure Windows-oriented HP printer work on macOS. Commenters challenged the “driver” framing, saying the initial solution reused HP’s Linux `rastertospl` component and introduced a risky root launcher rather than independently implementing the printer protocol. The author later reported moving to a fully native macOS version and explained that the interim design connected the existing codec to macOS CUPS. Other users shared successful AI-assisted reverse-engineering projects involving motor controllers, game files, audio devices, and controller firmware.

### Comment pulse

- Success stories emphasized dramatic time savings when models could combine binaries, packet captures, specifications, prior art, and iterative hardware tests.
- Skeptics objected to calling compatibility plumbing a new driver and suggested existing Linux-printing projects might have solved the problem faster.
- Several readers mourned lost mastery or disliked the assistant’s personal closing language, while others defended the practical result.

### LLM perspective

- View: The evidence supports AI-assisted integration and reverse engineering, not autonomous invention from an unsupported device alone.
- Impact: Reusing a proven codec was pragmatic, but provenance, licensing, privilege boundaries, and launch-path security require human review.
- Watch next: A native CUPS workflow can still depend on an existing vendor conversion component.
