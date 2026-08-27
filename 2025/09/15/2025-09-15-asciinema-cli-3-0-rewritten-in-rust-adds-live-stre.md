# Asciinema CLI 3.0 rewritten in Rust, adds live streaming, upgrades file format

- Score: 319 | [HN](https://news.ycombinator.com/item?id=45251375) | Link: https://blog.asciinema.org/post/three-point-o/

### TL;DR

Asciinema CLI 3.0 is a Rust rewrite with faster startup, static binaries, a revised asciicast v3 format, and local or server-relayed terminal streaming. Delta timestamps simplify editing, while new metadata, comments, and exit events enrich recordings. Recording is now explicitly local-first: `rec` requires a filename, and uploading is a separate command with a chosen server. HN users praised accessible, text-based terminal captures and self-hosting, though some questioned repeated language rewrites and criticized exporting searchable recordings as large, unseekable GIFs.

### Comment pulse

- Live streaming proved resource-efficient but stress-sensitive → launch traffic pushed the small two-VM service near saturation before scaling.
- Text recordings preserve selection, seeking, and compact transfer → GIF exports improve embedding convenience at substantial accessibility and bandwidth cost.
- Rust renewed maintainer motivation → critics saw language churn, while supporters prioritized continued development over implementation language.

### LLM perspective

- View: The most consequential change is explicit local ownership, not the implementation-language switch.
- Impact: Demonstrators and support teams gain live sharing without surrendering recordings to a hosted service.
- Watch next: Streaming load, package availability, v3 tooling compatibility, and accidental-disclosure safeguards.
