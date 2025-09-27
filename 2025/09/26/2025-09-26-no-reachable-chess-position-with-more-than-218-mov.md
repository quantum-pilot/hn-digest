# No reachable chess position with more than 218 moves

- Score: 337 | [HN](https://news.ycombinator.com/item?id=45382755) | Link: https://lichess.org/@/Tobs40/blog/there-is-no-reachable-chess-position-with-more-than-218-moves/a5xdxeqs

- TL;DR
  - A Lichess author proves, via integer programming, that the maximum number of legal moves available to the side to move in any reachable chess position is 218. He relaxes rules to prune the search, then adds constraints to eliminate “half‑piece” artifacts; Gurobi certifies optimality using bounds rather than brute force. Also confirmed: 144 is optimal without promotions; best illegal position has 288 moves; best legal but non‑reachable has 271. HN clarifies wording, debates MILP-as-proof, and praises Lichess.

- Comment pulse
  - Clarification: It's maximum legal next moves, not moves to reach a position → article’s phrasing confused many non‑chess readers.
  - Optimality claim → Gurobi supplies global bounds from relaxations/cuts; if modeling is correct, that’s effectively a proof — counterpoint: not a formal, inspectable proof object.
  - Lichess kudos → open source, ad‑free, strong variants, developer‑friendly; users urge donations compared to paywalled Chess.com features.

- LLM perspective
  - View: Framing chess move counts as MILP is a neat example of bounding combinatorial games without exhaustive enumeration.
  - Impact: Engine authors can cap per-position move encodings at 256; composers gain confirmed ceilings for themes like no-promotions.
  - Watch next: Release solver certificates or smaller verifiable proofs; attempt maxima for captures/checks; test alternative MIP cuts or SAT/SMT encodings.
