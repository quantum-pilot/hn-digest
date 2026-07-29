# Steel Bank Common Lisp version 2.6.7

- Score: 184 | [HN](https://news.ycombinator.com/item?id=49086971) | Link: https://sbcl.org/all-news.html?2.6.7

- TL;DR  
SBCL 2.6.7 tightens its already-strong Common Lisp implementation with a new SB-MANUAL contrib that embeds the full manual as structured docstrings, enabling interactive browsing via SLIME and MGL-PAX and generating Texinfo/HTML/PDF from a single source. The release broadens SIMD support (ARM64 SB-SIMD, AVX-512 on x86-64, faster UTF‑8 conversions), fixes several compiler and numeric edge-case bugs, and tunes performance in areas like sparse sets and complex-constant handling. HN discussion ranges from SBCL’s history and SIMD model to dreams of a Lisp-centric infrastructure world and notes on arenas and Windows support.

---

- Comment pulse  
  - Name and heritage → “Steel Bank” plays on Carnegie/Mellon fortunes (steel, banking) and “SB” as “Sanely Bootstrappable,” contrasting with CMUCL’s bootstrap issues.  
  - SIMD model → New ARM64/AVX-512 support lives in SB-SIMD; users call explicit intrinsics, not auto-vectorization — counterpoint: still yields serious speedups in numeric kernels.  
  - Ecosystem/infrastructure → Speculation about a Lisp-first world (image-based deploys, REPL in pods, sexpr diffs); today SBCL is fast and solid on Windows, but arenas remain underdocumented.

---

- LLM perspective  
  - View: Moving the manual into docstrings plus markdown-like structure pushes SBCL toward “live documentation” tightly coupled to the running image.  
  - Impact: Power users, library authors, and tooling (SLIME, MGL-PAX, custom browsers) gain richer, queryable, cross-linked documentation without leaving the REPL.  
  - Watch next: Auto-vectorization atop SB-SIMD, proper arena documentation and APIs, and real-world benchmarks exploiting new AVX-512/ARM64 paths and UTF‑8 SIMD.
