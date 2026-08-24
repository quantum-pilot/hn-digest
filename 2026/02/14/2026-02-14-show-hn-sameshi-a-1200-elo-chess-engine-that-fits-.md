# Show HN: Sameshi – a ~1200 Elo chess engine that fits within 2KB

- Score: 177 | [HN](https://news.ycombinator.com/item?id=47014500) | Link: https://github.com/datavorous/sameshi

### TL;DR

Sameshi compresses a C chess engine into a 1.95 KB header using a 120-cell mailbox board, depth-five negamax, alpha-beta pruning, material-only evaluation, capture-first ordering, and legal check, mate, and stalemate validation. Across 240 constrained games against Stockfish levels rated 1320–1600, it scored about 1170 Elo, with a 95% confidence interval of 1110–1225. It omits castling, en passant, promotion, repetition, and the 50-move rule. Commenters admired the code-golf result but argued full chess rules matter and found an illegal pawn double-step bug.

### Comment pulse

- Critics proposed a harder target: retain full rules and UCI compatibility, noting earlier tiny engines achieved richer play in 2–4 KB.
- Testing exposed an illegal second double-step by a pawn; the author acknowledged the report and planned a patch.
- Engine developers recommended cutechess with SPRT or Ordo for Elo estimation and floated Elo-per-byte as a code-golf metric.

### LLM perspective

- View: The project succeeds as size-constrained engineering, while its omissions make Elo less informative about ordinary chess.
- Impact: Tiny-engine authors get a compact baseline; players encounter rule gaps that can alter tactics, legality, and outcomes.
- Watch next: Fix pawn state, add special moves, publish methodology, then compare strength per byte under identical rules.
