# Solving Fizz Buzz with Cosines

- Score: 105 | [HN](https://news.ycombinator.com/item?id=46006598) | Link: https://susam.net/fizz-buzz-with-cosines.html

### TL;DR

The author deliberately overengineers Fizz Buzz by treating its output selector as a period-15 function. Indicator functions for divisibility by three and five are rewritten with complex exponentials and then reduced to a discrete Fourier series containing three cosine terms. Rounding that expression yields an index selecting the number, “Fizz,” “Buzz,” or “FizzBuzz” from an array. A second derivation applies the discrete Fourier transform directly. The construction is pedagogical and playful, demonstrating exact Fourier representation rather than offering a sensible implementation.

### Comment pulse

- Readers proposed direct Fourier and polynomial alternatives, continuing the joke through increasingly elaborate solutions.
- One commenter warned floating-point behavior may break the implementation for sufficiently large integers.

### LLM perspective

- View: The useful lesson is that finite periodic programs can be recast exactly as frequency components.
- Impact: Absurd constraints turn a trivial exercise into an approachable tour of indicator functions and Fourier analysis.
- Watch next: Where floating-point rounding first diverges from the mathematically exact selector.
