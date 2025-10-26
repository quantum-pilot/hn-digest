# That Time Ken Thompson Wrote a Backdoor into the C Compiler

- Score: 79 | [HN](https://news.ycombinator.com/item?id=45701884) | Link: https://micahkepe.com/blog/thompson-trojan-horse/

- TL;DR
  - Ken Thompson’s “Trusting Trust” shows how a C compiler can be “trained” to insert a login backdoor and self-replicate, defeating source audits. This article walks through quines, a “learning” compiler example, the recovered codenih/repronih code path, and the multi-stage bootstrapping that hides evidence; it notes Thompson said it wasn’t distributed and cites defenses like DDC. HN pivots to bootstrappable toolchains (Guix, live-bootstrap) as mitigations, debates how “undetectable” it really is, and clarifies details like “\v” being ASCII 11.

- Comment pulse
  - Start from minimal, auditable seeds → Guix’s 357‑byte seed and live-bootstrap rebuild trust by constructing compilers stepwise from trivial programs.
  - Backdoor is hard, not impossible, to find → Large compilers resist analysis; avoid compromise via bootstrapping and reproducible builds — counterpoint: “undetectable” was overstated.
  - History and details matter → Trojan horses predate Thompson by decades; “\v” is ASCII vertical-tab (code 11), not Gödelian encoding.

- LLM perspective
  - View: Treat compilers and build tools as part of the threat model; verify them, not just the sources they process.
  - Impact: Push mainstream distros toward bootstrappable chains, DDC-verified toolchains, and routinely published, reproducible compiler rebuilds.
  - Watch next: Public DDC audits of GCC/Clang, minimal bootstrap seeds landing in releases, hardware/firmware attestation linked to reproducible toolchain outputs.
