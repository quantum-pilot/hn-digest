# Faster asin() was hiding in plain sight

- Score: 172 | [HN](https://news.ycombinator.com/item?id=47336111) | Link: https://16bpp.net/blog/post/faster-asin-was-hiding-in-plain-sight/

## TL;DR
An engineer searched for a faster asin() and rediscovered a classic minimax-style rational approximation from older math tables and GPU docs. The method substantially outperforms naive Taylor or Padé-from-Taylor approaches, with bounded error over a defined interval. Commenters dive into Chebyshev, Remez, and minimax theory, debate the approximation’s provenance, and lament that numerical methods taught in school often differ from what real FPUs and math libraries actually use. There’s also amusement over wild bit-hack implementations.  

*Content unavailable; summarizing from title/comments.*

## Comment pulse
- Minimax and Chebyshev over Taylor → error-curve “wiggle” shows near-optimality; Remez or Chebyshev approximations usually beat Taylor and naive Padé.  
- Provenance matters → approximation resembles classic table entries from Abramowitz–Stegun, not Hastings; Cody–Waite and DLMF cited as authoritative function-approximation references.  
- Numerical methods education lags practice → curricula stress Taylor and CORDIC while FPUs use minimax polynomials; commenters share vectorization tricks and joke “evil” bit-hack asin().  

## LLM perspective
- View: Systematically mining classic references and GPU docs could surface many similar fast approximations for transcendental functions beyond asin.  
- Impact: Game engines, DSP code, and SIMD-heavy kernels gain speed by swapping libm calls for vetted minimax or rational approximations.  
- Watch next: Open-source libraries providing auto-generated approximations with error guarantees, plus tutorials to shift education from Taylor-centric to minimax-focused techniques.
