# Turns are Better than Radians (2022)

- Score: 332 | [HN](https://news.ycombinator.com/item?id=49369408) | Link: https://www.computerenhance.com/p/turns-are-better-than-radians

## TL;DR
Muratori argues most code needlessly converts normalized angles to radians to call `sin`/`cos`, only for libraries to immediately rescale them again. Using “turns” (0–1 for a full circle) or half‑turns lets callers keep angles in natural [0,1] form, saving multiplications and improving precision for common angles (0.25, 0.5, 0.75 are exact). Commenters agree this is practical for graphics and phase accumulators, but stress that radians remain essential for calculus, Taylor series, and symbolic math.

---

## Comment pulse
- Radians are mathematically special → Euler’s formula and simple trig derivatives rely on radian scaling, otherwise derivatives gain messy 2π factors — counterpoint: that’s irrelevant for pure numeric evaluation.

- Use depends on application → turns are great for normalized phases and graphics; radians better when you differentiate, optimize, or use small‑angle/Taylor expansions.

- Alternative designs → represent angles as (sin, cos) tuples or half‑angle parameters to avoid repeated trig calls, trading API simplicity for fewer expensive evaluations.

---

## LLM perspective
- View: Separate “math-native” radians from “machine-native” turns; expose both in libraries rather than arguing for a single universal unit.

- Impact: Graphics, DSP, and game engines gain micro‑optimizations and cleaner code; scientific computing keeps radians for analysis and derivations.

- Watch next: Benchmarks comparing radian vs turn interfaces, hardware/ISA support for turn-based trig, and language-level APIs indicating angle conventions explicitly.
