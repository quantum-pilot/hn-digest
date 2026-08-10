# Microsoft Word for Windows 1.1a, Native X64 Port

- Score: 161 | [HN](https://news.ycombinator.com/item?id=49228663) | Link: https://github.com/jmarshall23/msword

### TL;DR

This project compiles Microsoft Word 1.1a’s original C sources and resources into a native 64-bit Windows executable rather than emulating Win16 or reimplementing the editor. Fixed-width C/C++ replaces 16-bit assembly, an x64 runtime maps segmented handles safely, and modern Win32 adapters cover startup, messaging, graphics, files, and resources. CMake rebuilds historical assets, while tests exercise runtime structures, startup, formatting, dialogs, and saving. Commenters welcomed the preservation effort but reported a missing CMake helper, requested screenshots, and noted easier compatibility options such as winevdm.

### Comment pulse

- Original behavior remains authoritative → platform adaptations are isolated while legacy assembly stays available as reference.
- Build reproducibility drew concern → one commenter found GenerateMenuHelpHeader.cmake absent from the repository.
- Legal reuse remains uncertain → historical notices remain, but the repository has no top-level license.

### LLM perspective

- **View:** A native port is most valuable as executable documentation of legacy architecture and migration techniques.
- **Impact:** Researchers can study original Word behavior without a 16-bit runtime, assuming the build is complete.
- **Watch next:** Missing-file fix, reproducible CI builds, screenshots, license clarification, and broader UI compatibility tests.
