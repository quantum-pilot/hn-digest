# Show HN: Sameshi – a ~1200 Elo chess engine that fits within 2KB

- Score: 177 | [HN](https://news.ycombinator.com/item?id=47014500) | Link: https://github.com/datavorous/sameshi

- TL;DR  
    - Sameshi is a tiny C chess engine whose entire logic lives in a 1.95KB header, yet still plays around 1200 Elo using a 120‑cell mailbox board, negamax with alpha‑beta, material‑only evaluation and basic move ordering. To keep the size budget it omits castling, en passant, promotion and draw rules, though it fully validates checks, mates and stalemates. Hacker News readers debate what “real” chess requires, trade links to even smaller engines, report a pawn‑movement bug, and swap Elo‑testing tools.

- Comment pulse  
    - Minimalism vs completeness → Some want full modern rules and UCI compliance as the true challenge, citing 4K‑era and Nanochess‑style micro‑engines as precedents.  
    - Implementation quirks → A tester finds a double two‑square pawn‑advance bug; others note castling logic is tricky and suggest reusing text or GUI frontends.  
    - Metrics and gamesmanship → Commenters share cutechess and Ordo for Elo estimation, and propose a “1 Elo per byte” code‑golf challenge for ultra‑tiny engines.

- LLM perspective  
    - View: Treat these engines as demoscene‑style compression of chess knowledge, prioritizing elegance and constraints over feature completeness.  
    - Impact: Encourages hobbyists to understand core search and evaluation ideas deeply enough to reimplement them under strict space limits.  
    - Watch next: Benchmarks comparing strength vs bytes across engines, plus attempts at fully rules‑complete micro‑engines and builds for retro hardware.
