# Fedora Asahi Remix is now working on Apple M3

- Score: 397 | [HN](https://news.ycombinator.com/item?id=46769051) | Link: https://bsky.app/profile/did:plc:okydh7e54e2nok65kjxdklvd/post/3mdd55paffk2o

### TL;DR

An early Fedora Asahi Remix bring-up now reaches a KDE desktop on Apple’s M3 hardware using software rendering. The internal display currently relies on a framebuffer rather than the display controller, while keyboard, trackpad, Wi-Fi, and NVMe storage work. GPU acceleration remains the major gap because Apple changed the instruction set and compiler work is still underway. Commenters celebrated the young contributor and broader M1/M2 progress, but stressed that a bootable desktop is not yet a feature-complete workstation or competitive local-AI platform.

### Comment pulse

- M3 support is a meaningful milestone → core input, networking, storage, and a visible desktop establish a base for driver work.
- Desktop output is not GPU readiness → software rendering proves bring-up, while graphics acceleration and efficient local model workloads remain unfinished.
- Later chips may stay difficult → commenters cite stronger page-table protections on M4 and a newer GPU generation on M5.

### LLM perspective

- View: The breakthrough is platform enablement, not daily-driver parity.
- Impact: Contributors can test more M3 subsystems; ordinary users should still expect missing acceleration and incomplete hardware support.
- Watch next: DCP support, accelerated GPU drivers, compiler progress, installation readiness, and published M3 compatibility matrices.
