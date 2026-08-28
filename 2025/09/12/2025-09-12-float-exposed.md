# Float Exposed

- Score: 384 | [HN](https://news.ycombinator.com/item?id=45217415) | Link: https://float.exposed/

### TL;DR

Float Exposed is an interactive-looking representation of floating-point values, showing sign, exponent, significand, raw bit patterns, hexadecimal and decimal forms, exact value, and distance to adjacent representable numbers across several formats. The frozen text captures labels and one example rather than the interface’s behavior, so discussion supplies much of the explanation. Commenters focused on scale-relative precision, shortest round-trippable decimal strings, specialized conversion algorithms, bitwise ordering caveats, accumulation error, and game-world failures when coordinates grow far from the origin.

### Comment pulse

- Suggested float-to-string algorithms included Dragon4, Grisu3, Ryu, and Dragonbox rather than repeated formatting and parsing.
- A correction noted integer ordering works directly for positive floats, but negative encodings require transformed comparison.

### LLM perspective

- View: Bit-level visualization makes floating-point spacing concrete, especially where mathematical intuition expects uniform precision.
- Impact: Understanding representation prevents serialization, comparison, accumulation, and large-coordinate bugs.
- Watch next: Explore subnormals, negative zero, infinities, NaNs, rounding modes, and representable spacing at different magnitudes.
