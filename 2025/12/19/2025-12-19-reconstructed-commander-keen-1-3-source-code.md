# Reconstructed Commander Keen 1-3 Source Code

- Score: 150 | [HN](https://news.ycombinator.com/item?id=46321982) | Link: https://pckf.com/viewtopic.php?t=18248

### TL;DR

A reconstruction project releases source for known Commander Keen 1–3 versions, spanning a November 1990 beta through the obscure 1.34 PSA release. Using exact historical Turbo C++ and assembler versions plus original-style executable compression can reportedly reproduce binaries byte-for-byte. A notable obstacle was Turbo C++ 1.x ordering uninitialized variables according to identifier hashes, solved by generating names that forced the required BSS layout. The author also alleges reused Softdisk routines, while commenters dispute whether reconstructed or decompiled code can legitimately receive a GPL license.

### Comment pulse

- Reverse engineers admired the variable-name search used to reproduce compiler-dependent BSS ordering when original identifiers were absent.
- Legal debate distinguished matching decompilation from clean-room reimplementation; commenters agreed asset-free distribution does not automatically settle copyright authority.

### LLM perspective

- View: Byte-identical reconstruction preserves toolchain behavior as much as game logic.
- Impact: Researchers can study and modify historically important code, but redistribution carries unresolved legal exposure.
- Watch next: Rights-holder response, independent build verification, and documentation supporting the alleged Softdisk code lineage.
