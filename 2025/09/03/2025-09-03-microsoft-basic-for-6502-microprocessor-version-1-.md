# Microsoft BASIC for 6502 Microprocessor – Version 1.1

- Score: 289 | [HN](https://news.ycombinator.com/item?id=45118392) | Link: https://github.com/microsoft/BASIC-M6502

### TL;DR

Microsoft published the complete 6,955-line assembly source for its 8 KB 6502 BASIC 1.1 interpreter, copyrighted 1976–1978. Conditional assembly targeted the Apple II, Commodore PET, Ohio Scientific systems, KIM-1, and a PDP-10 simulation, while the runtime supplied floating-point math, strings, arrays, garbage collection, interactive commands, and configurable I/O. The repository frames the code as foundational to Microsoft's licensing business and early personal computing. Commenters highlight the hidden `WAIT 6502,X` “MICROSOFT!” message and playful historical Git timestamps.

### Comment pulse

- Readers use the release with hobbyist 6502 builds, extending memory and adapting BASIC to custom breadboard computers.
- Some question archival details: non-source files share artificial dates, and the repository does not clearly date its modern licensing metadata.

### LLM perspective

- View: The source is valuable less as a polished archive than as inspectable evidence of portable software under extreme constraints.
- Impact: Modern builders can study how one compact interpreter crossed hardware boundaries and supported Microsoft's early licensing model.
- Watch next: Provenance notes, authorship metadata, build instructions, verified platform binaries, and separation of historical files from modern documentation.
