# Microsoft Word for Windows 1.1a, Native X64 Port

- Score: 161 | [HN](https://news.ycombinator.com/item?id=49228663) | Link: https://github.com/jmarshall23/msword

- TL;DR  
  A developer has ported the original Microsoft Word for Windows 1.1a (codename Opus) to run natively as a 64‑bit Windows executable. It reuses the original C sources and resources, replacing only the 16‑bit assembly, segmented memory model, and Win16 APIs with a modern x64‑safe runtime and Win32 shims. The project is research‑oriented, with extensive tests for UI and behavior fidelity. HN comments mix nostalgia, easier alternatives, and some practical build/usability concerns.

- Comment pulse  
  - Old Office UIs (Word 5/97/98/2003) are fondly remembered; some say usability declined after the Ribbon—counterpoint: Wine, Abiword, Gnumeric keep “classic” workflows viable.  
  - For simply running 16‑bit Word, users suggest winevdm, which transparently hosts Win3.x apps on modern x64 Windows with much less engineering effort.  
  - Builders report a missing CMake helper script and wish for screenshots; others speculate omission might avoid copyright trouble with Microsoft branding.

- LLM perspective  
  - View: This is meticulous software archaeology, preserving not just binaries but build systems, tests, and original behavior on modern hardware.  
  - Impact: Useful for historians, UI/UX researchers, and systems programmers studying 16‑bit to 64‑bit migration patterns without emulation noise.  
  - Watch next: Similar source‑faithful ports of other early GUI apps; clearer licensing from rights holders; comparative UX studies vs. modern editors.
