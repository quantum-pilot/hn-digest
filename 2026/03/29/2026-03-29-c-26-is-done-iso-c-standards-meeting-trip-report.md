# C++26 is done ISO C++ standards meeting, Trip Report

- Score: 153 | [HN](https://news.ycombinator.com/item?id=47565365) | Link: https://herbsutter.com/2026/03/29/c26-is-done-trip-report-march-2026-iso-c-standards-meeting-london-croydon-uk/

### TL;DR
C++26 has been finalized by the ISO committee, with Herb Sutter calling it the most impactful release since C++11. The standard centers on four pillars: powerful compile‑time reflection, safer defaults (no UB on uninitialized locals and a hardened standard library), language‑level contracts, and std::execution for structured async and parallelism. Implementations are already well underway, and C++29 work will push memory‑safety further. HN is enthusiastic about reflection and safety, but divided over contracts, complexity, and weak tooling/modules.

### Comment pulse
- Contracts add dangerous complexity → critics cite Bjarne Stroustrup calling them bloated and incomplete; supporters say standardizing contracts enables formal verification and matches existing practice.  
- Uninitialized-read change trades UB for checks → new “erroneous behavior” semantics improve safety but may incur runtime cost, with attributes to opt back to UB.  
- Modules and tooling seen as C++’s real problem → many want a Cargo-like ecosystem; some call modules a failed idea and dread growing language complexity.  

### LLM perspective
- View: C++26 shifts the language toward “safer by default” while preserving opt‑out performance paths; the main risk is cognitive overload.  
- Impact: Biggest wins will be from recompiling with hardened libraries and reduced UB, even if reflection and std::execution stay unused.  
- Watch next: Track adoption of contracts, safety profiles, and modules/packages; their ergonomics will decide whether C++26 feels empowering or exhausting.
