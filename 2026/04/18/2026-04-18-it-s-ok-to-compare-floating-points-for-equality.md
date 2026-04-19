# It's OK to compare floating-points for equality

- Score: 174 | [HN](https://news.ycombinator.com/item?id=47767398) | Link: https://lisyarus.github.io/blog/posts/its-ok-to-compare-floating-points-for-equality.html

- TL;DR  
    - The post argues that “never compare floats for equality” is over-applied dogma. Floating point is deterministic and many problems are better solved by exact comparisons on meaningful invariants (e.g., “is this exactly zero?”) or by redesigning the algorithm or data model, rather than sprinkling arbitrary epsilons that break transitivity and invariants. Epsilons are appropriate only when grounded in domain tolerances (noisy geometry, physical measurements, test harnesses), not as a generic fix for numerical unease.  

- Comment pulse  
    - Physical/engineering view → real-world quantities are inherently approximate; domain-driven tolerances are mandatory, even if floats were perfect — counterpoint: floats also serve non-physical domains.  
    - Computational geometry view → input meshes are noisy; kernels rely on “fuzzy” ops and tolerance ladders, and exact correctness is often unattainable.  
    - Numerical/solver view → machine epsilon is widely misused; equality-with-EPS is often equivalent to `==`; robust code needs relative+absolute tolerances and explicit error models.  

- LLM perspective  
    - View: Treat “float equality” as a design problem: what invariant or intent are you really testing, and at what scale?  
    - Impact: Libraries should prefer exact comparisons for structural invariants, and expose tunable tolerances for domain noise and user data.  
    - Watch next: Better educational material and APIs around ulps, relative error, and robust geometry/numerics patterns, not one-size-fits-all helpers.
