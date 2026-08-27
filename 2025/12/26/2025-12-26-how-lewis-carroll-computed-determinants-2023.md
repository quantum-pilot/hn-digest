# How Lewis Carroll computed determinants (2023)

- Score: 208 | [HN](https://news.ycombinator.com/item?id=46395106) | Link: https://www.johndcook.com/blog/2023/07/10/lewis-carroll-determinants/

### TL;DR

Charles Dodgson, better known as Lewis Carroll, devised condensation for calculating determinants by repeatedly replacing adjacent 2×2 blocks with their determinants, shrinking an n×n matrix to one value. From the second reduction onward, each result is divided by the corresponding interior entry from two stages earlier. The method takes cubic time like Gaussian elimination, preserves integers when the input is integral, and exposes parallel work, unlike factorial-time cofactor expansion. Rows or columns may need rearrangement to prevent zero denominators, a complication Dodgson addressed in 1867.

### Comment pulse

- Historical terminology sparked interest → “cipher” once meant zero, with cognates surviving across Arabic-influenced European and Asian languages.
- Condensation surprised determinant learners → many had encountered only tedious cofactor expansion, despite modern linear algebra offering alternatives.
- Dodgson’s paper remains approachable → changing mathematical notation makes that accessibility more notable than Carroll’s readable literature.

### LLM perspective

- View: Condensation is pedagogically valuable because a simple local operation achieves globally competitive asymptotic complexity.
- Impact: Students gain a bridge from hand arithmetic to exact and parallel numerical algorithms.
- Watch next: Compare pivoting strategies, numerical stability, and practical parallel performance against modern elimination implementations.
