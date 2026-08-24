# Doom has been ported to an earbud

- Score: 318 | [HN](https://news.ycombinator.com/item?id=46753484) | Link: https://doombuds.com

### TL;DR

DOOMBuds runs the shareware game on open-firmware PineBuds Pro hardware and lets one queued web visitor control it remotely. The earbud’s 300 MHz Cortex-M4F can execute the game, but JPEG encoding limits output to about 18 frames per second. MJPEG compression fits video through a 2.4 Mbps UART link; Bluetooth was too slow. Disabling a coprocessor exposes 992 KB of RAM, aggressive code reductions overcome the game’s nominal 4 MB requirement, and a 1.7 MB Squashware asset file fits the 4 MB flash.

### Comment pulse

- General-purpose chips are economical, not wasteful → mass-produced microcontrollers reduce design cost and ease updates — counterpoint: their capability can appear excessive.
- Doom remains the standard stunt → open source, modest requirements, engine history, and cultural momentum make ports comparable.

### LLM perspective

- View: The impressive work is resource budgeting and streaming, not merely launching a familiar executable.
- Impact: Open firmware turns disposable-looking peripherals into approachable embedded-systems laboratories.
- Watch next: Technical write-up, reproducible builds, power and thermal behavior, and Bluetooth alternatives.
