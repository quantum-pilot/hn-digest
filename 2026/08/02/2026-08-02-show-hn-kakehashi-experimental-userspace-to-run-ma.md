# Show HN: Kakehashi – Experimental userspace to run macOS binaries on Linux ARM

- Score: 159 | [HN](https://news.ycombinator.com/item?id=49145937) | Link: https://github.com/wie-project/kakehashi

## TL;DR
Experimental project “Kakehashi” aims to run macOS command‑line binaries natively on Linux ARM by recreating a macOS-like userspace/ABI, similar in spirit to Wine for Windows. Early prototypes work for 7‑Zip (multi‑threaded, but ~5.2× slower than native), curl (200+ options tested), and Xcode’s Git (basic commands). HN discussion centers on overlap with Darling, feasibility of expanding to broader macOS tooling (and maybe GUIs/AU plugins), performance vs. VM-like approaches, and legal/distribution trade‑offs.

*Content unavailable; summarizing from title/comments.*

---

## Comment pulse
- macOS-on-Linux userspace like Wine is plausible → Darling shows precedent; combining efforts might avoid duplication — counterpoint: Kakehashi explicitly isn’t derived from Darling, suggesting differing architectures/goals.  

- Users want “real macOS” semantics → questions about matching specific macOS versions, filesystem quirks, uname output, and running scripts expecting Darwin-like tools and behavior.  

- Using a copied macOS rootfs might be easier → could avoid re‑implementing frameworks, but then it’s effectively a VM, with more overhead and messy redistribution/licensing.

---

## LLM perspective
- View: A focused CLI-first layer is tractable; GUI/framework parity with macOS will be the real cliff.  
- Impact: ARM devs on Linux (e.g., Apple Silicon with Asahi, SBCs) gain access to macOS-only toolchains and vendor CLIs.  
- Watch next: performance benchmarks vs. native/VM, broader binary compatibility matrix, and any collaboration/contrast with Darling’s eventual ARM64 support.
