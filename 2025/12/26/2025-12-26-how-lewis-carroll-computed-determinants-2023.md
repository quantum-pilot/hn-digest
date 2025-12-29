# How Lewis Carroll computed determinants (2023)

- Score: 208 | [HN](https://news.ycombinator.com/item?id=46395106) | Link: https://www.johndcook.com/blog/2023/07/10/lewis-carroll-determinants/

### TL;DR
Lewis Carroll (Charles Dodgson) devised “condensation,” an algorithm for determinants that repeatedly replaces an n×n matrix with an (n−1)×(n−1) matrix of 2×2 minors, then divides by interior entries from two steps earlier. It matches Gaussian elimination’s O(n³) complexity but keeps all intermediate values integral for integer matrices and is highly parallelizable. One must permute/adjust rows and columns to avoid zeros in the interior. HN discussion branches into etymology of “cipher,” alternate expositions, and the modern role of determinants in linear algebra.

---

### Comment pulse
- Cipher discussion → “cipher” once meant zero; many modern words (e.g., Turkish “sıfır,” Dutch “cijfer”) trace back via Arabic “sifr” — counterpoint: Arabs themselves borrowed zero/numerals from Indians.  
- Exposition and style → Readers note Terry Tao’s write-up on Dodgson condensation and joke about Carroll’s mathematical prose versus Jabberwocky and slower-changing literary conventions.  
- Determinants in teaching → Some hated cofactor expansion; others note modern courses (e.g., Axler) minimize determinants, favoring determinant-free proofs for core linear algebra.

---

### LLM perspective
- View: Condensation is a conceptually neat, historically charming determinant algorithm that exposes structure via local 2×2 operations.  
- Impact: Best suited for education, symbolic math, and exploring parallel implementations, rather than as a default numerical workhorse.  
- Watch next: Benchmark numerical stability against LU; design robust pivot/preconditioning rules to handle zeros or tiny interior elements.
