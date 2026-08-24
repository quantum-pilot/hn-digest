# UEFI Bindings for JavaScript

- Score: 189 | [HN](https://news.ycombinator.com/item?id=46945348) | Link: https://codeberg.org/smnx/promethee

### TL;DR

Promethee is a proof-of-concept boot environment that loads script.js from a UEFI volume and exposes firmware services to it, making the script the bootloader. A tiny example locates the graphics-output protocol and paints a rectangle; the freestanding build supplies minimal libc stubs, uses Duktape-related source generation, and runs under QEMU. Commenters enjoyed the deliberately extreme abstraction, but clarified that this does not by itself make JavaScript a complete operating-system language: direct memory mapping, processor registers, ports, tables, and userspace setup would still require lower-level C or assembly support.

### Comment pulse

- Reactions split between delight at “complete dominion” and horror, with the project compared to the predicted “Metal” stage of software abstraction.
- Commenters agreed JavaScript could direct substantial OS logic—counterpoint: bootstrapping userspace and touching architectural state still needs a native runtime.
- A package-import joke met the observation that newer UEFI firmware already exposes networking, including HTTP and HTTPS.

### LLM perspective

- View: The demonstration works because its boundary is visible: firmware services become scriptable, while hardware control remains lower-level.
- Impact: Firmware experiments become approachable, but production boot paths inherit interpreter size, attack surface, and portability concerns.
- Watch next: API coverage, firmware compatibility, image size, error handling, security boundaries, debugging, persistence after ExitBootServices, and escape hatches.
