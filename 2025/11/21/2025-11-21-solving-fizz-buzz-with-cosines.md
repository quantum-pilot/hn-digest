# Solving Fizz Buzz with Cosines

- Score: 105 | [HN](https://news.ycombinator.com/item?id=46006598) | Link: https://susam.net/fizz-buzz-with-cosines.html

### TL;DR

The author turns the familiar divisibility exercise into an intentionally elaborate Fourier construction. Indicator functions for multiples of three and five select four outputs, then roots-of-unity identities convert those indicators into a constant plus three cosine terms. Because the selection pattern repeats every 15 integers, a discrete Fourier transform independently produces the same finite series. A short Python program rounds the expression to index the desired output. The result is mathematically exact for integer inputs in theory, delightfully impractical, and potentially limited by floating-point precision.

### Comment pulse

- Fourier analysis fits exactly → the selector is a function on a 15-element cyclic group.
- The implementation is playful, not robust → floating-point cosine errors may eventually select the wrong symbol.

### LLM perspective

- View: This is a recreational derivation that teaches periodic indicators through deliberate overengineering.
- Impact: A toy interview problem becomes an accessible demonstration of finite Fourier representation.
- Watch next: Exact arithmetic variants, numerical failure thresholds, polynomial alternatives, and generalized divisibility games.
