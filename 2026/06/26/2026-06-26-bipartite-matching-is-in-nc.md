# Bipartite Matching Is in NC

- Score: 107 | [HN](https://news.ycombinator.com/item?id=48637433) | Link: https://scottaaronson.blog/?p=9851

### TL;DR

A five-author paper claims a deterministic NC algorithm for bipartite matching, potentially settling an open problem from the 1980s. Given two groups and allowed pairings, it can both decide whether everyone can be matched and construct the matching in polylogarithmic time using polynomially many parallel processors. Earlier parallel methods required randomness and succeeded only with high probability; the new work derandomizes the Mulmuley–Vazirani–Vazirani approach. HN celebrated the result, clarified NC as polynomial-size, polylog-depth constant-fan-in circuits, and connected matching to multi-party board-game trades.

### Comment pulse

- Constant fan-in matters → allowing unbounded fan-in changes the circuit class from NC to AC.
- Efficiently solvable need not mean efficiently parallelizable → whether NC equals P is unproved, analogous in status to P versus NP.
- Math trades supply a concrete use → acceptable exchanges form a matching problem that replaced slower bespoke calculations for board-game swaps.

### LLM perspective

- **View:** The result separates randomness from parallelizability: randomized shallow circuits were known, but deterministic shallow circuits were the missing piece.
- **Impact:** Parallel-algorithm theory gains a canonical derandomization; practical systems may benefit only after constants and processor requirements are understood.
- **Watch next:** Verify proof, simplify the construction, bound processor counts, and test whether techniques extend to matching in general graphs.
