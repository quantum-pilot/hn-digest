# Solving Fizz Buzz with Cosines

- Score: 105 | [HN](https://news.ycombinator.com/item?id=46006598) | Link: https://susam.net/fizz-buzz-with-cosines.html

## TL;DR
The author redefines FizzBuzz as a mathematically precise sequence indexed by a function \(f(n)\in\{0,1,2,3\}\) choosing between `n`, “Fizz”, “Buzz”, and “FizzBuzz”. They first express \(f(n)\) using divisibility indicator functions \(I_m(n)\), then replace each \(I_m\) with a finite sum of complex exponentials, which simplifies to cosines via Euler’s formula. The result is a closed-form finite Fourier series in cosines whose rounded value gives the correct index for any integer \(n\), implemented in a compact Python one-liner.

---

## Comment pulse
- This is essentially a discrete Fourier transform on a length‑15 periodic sequence; author used divisibility shortcuts instead of brute-force DFT coefficients.  
- Thread veers into other overengineered FizzBuzzes: TensorFlow, arcane “technical interview” parodies, lazy lists, even joking about quantum encodings.  
- Discussion notes numerical limits (cos-based formula failing around \(2^{50}\)), FFT misuses for pattern detection, and polynomial‑interpolation or LLM-generated “recreational math” alternatives.

---

## LLM perspective
- View: Neat showcase of encoding discrete logic (divisibility) into smooth analytic structure via roots of unity and Fourier series.  
- Impact: Useful as a pedagogical example connecting number theory, signals, and programming—more math inspiration than practical code pattern.  
- Watch next: Similar constructions for other modular games, visualizations on cyclic groups, or auto-deriving such series with CAS tools.
