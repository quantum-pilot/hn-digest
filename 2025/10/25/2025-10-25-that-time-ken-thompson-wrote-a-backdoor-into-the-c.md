# That Time Ken Thompson Wrote a Backdoor into the C Compiler

- Score: 79 | [HN](https://news.ycombinator.com/item?id=45701884) | Link: https://micahkepe.com/blog/thompson-trojan-horse/

### TL;DR

Ken Thompson’s “Trusting Trust” attack teaches a compiler to recognize login source and inject a universal-password backdoor, then recognize its own source and reproduce the malicious compiler behavior. After the altered binary is built, clean compiler source still regenerates the compromise, defeating ordinary source review. Thompson reportedly built but did not distribute it. The article reconstructs the mechanism through quines, compiler bootstrapping, and recovered code. Hacker News notes binaries remain inspectable, but favors tiny-source bootstraps and diverse double-compilation over heroic decompilation.

### Comment pulse

- Source provenance alone is insufficient → a compromised compiler can emit malicious binaries while its visible source remains clean.
- Minimal bootstrap chains improve auditability → projects such as live-bootstrap and Guix reduce the opaque trusted seed.
- “Undetectable” is practical, not absolute → intensive binary analysis may find the implant, but compiler complexity favors verification strategies.

### LLM perspective

- View: The enduring lesson is that trust extends through every executable transformation, not merely the reviewed repository.
- Impact: Reproducible-build and bootstrap projects must account for compilers, assemblers, interpreters, and their ancestry.
- Watch next: Compare diverse double-compilation, independently built toolchains, binary reproducibility, and minimized bootstrap seeds.
